#!/usr/bin/env python3
"""Extract a PowerPoint deck into a Markdown inventory source.

Writes one Markdown file with, for every slide: number, hidden flag, layout,
title, visible text, tables, charts (type, series, categories), pictures
(with alt text), speaker notes, and measurements for slide design review:
smallest text size, word count, overlapping or off-slide shapes, and picture
resolution. Optionally renders the slides to a PDF and PNG images so a
reviewer can see layout.

Usage:
    python3 extract_deck.py DECK.pptx OUT_DIR [--render]
        [--screen-width-ft W --back-row-ft D [--screen-height-ft H]]

With the room options, it also estimates how far away each slide's
smallest text can be read, using a common display-legibility guideline:
capital letters at least 16 minutes of arc tall at the viewer's eye.

Requires python-pptx. Rendering also requires LibreOffice (soffice) and
pdftoppm (poppler-utils).
"""

import argparse
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE
except ImportError:
    sys.exit("python-pptx is not installed. Install it with: pip install python-pptx")


def shape_text(shape):
    if not shape.has_text_frame:
        return ""
    lines = []
    for para in shape.text_frame.paragraphs:
        text = "".join(run.text for run in para.runs).strip()
        if text:
            lines.append("  " * para.level + "- " + text)
    return "\n".join(lines)


def table_md(table):
    rows = []
    for r in table.rows:
        rows.append("| " + " | ".join(c.text.strip().replace("\n", " ") for c in r.cells) + " |")
    if len(rows) > 1:
        rows.insert(1, "|" + " - |" * len(table.columns))
    return "\n".join(rows)


def chart_md(chart):
    parts = [f"Chart type: {chart.chart_type}"]
    try:
        if chart.has_title and chart.chart_title.has_text_frame:
            parts.append(f"Chart title: {chart.chart_title.text_frame.text.strip()}")
    except Exception:
        pass
    try:
        plot = chart.plots[0]
        cats = [str(c) for c in plot.categories]
        if cats:
            parts.append("Categories: " + ", ".join(cats))
        series = list(plot.series)
        for ser in series:
            vals = ", ".join("" if v is None else f"{v:g}" for v in ser.values)
            parts.append(f"Series '{ser.name}': {vals}")
        if not chart.has_title and len(series) == 1:
            parts.append(f"Chart title: none set; slide software usually shows the series name "
                         f"('{series[0].name}') as an automatic title")
    except Exception as exc:  # chart data can be missing or unusual
        parts.append(f"(Chart data not readable: {exc})")
    return "\n".join("- " + p for p in parts)


def alt_text(shape):
    try:
        return shape._element.xpath("./*[1]/p:cNvPr")[0].get("descr") or ""
    except Exception:
        return ""


NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "p": "http://schemas.openxmlformats.org/presentationml/2006/main"}
EMU_PER_INCH = 914400
SMALL_TEXT_PT = 18      # heuristic: check text below this size against the room
MANY_WORDS = 75         # heuristic: slides above this word count are text-heavy
HIGH_PPI = 300          # heuristic: a large image shown small (a shrunk screenshot?)
LOW_PPI = 96            # heuristic: a small image stretched (may look blurry)
CAP_HEIGHT = 0.65       # capital-letter height as a share of font size (Calibri is about 0.64)
MIN_ARCMIN = 16         # minimum capital-letter height, in minutes of arc, for comfortable reading


def room_scale(prs, room):
    """How many times larger the slide appears on the screen."""
    slide_w = prs.slide_width / EMU_PER_INCH
    slide_h = prs.slide_height / EMU_PER_INCH
    scale = room["screen_w_ft"] * 12 / slide_w
    if room.get("screen_h_ft"):
        scale = min(scale, room["screen_h_ft"] * 12 / slide_h)
    return scale


def readable_ft(size_pt, scale):
    """Farthest distance, in feet, at which text of this size meets the guideline."""
    cap_in = size_pt / 72 * CAP_HEIGHT * scale
    return cap_in / math.tan(math.radians(MIN_ARCMIN / 60)) / 12


def needed_pt(distance_ft, scale):
    """Smallest text size, in points, that meets the guideline at this distance."""
    cap_in = distance_ft * 12 * math.tan(math.radians(MIN_ARCMIN / 60))
    return cap_in / (CAP_HEIGHT * scale) * 72


def _lvl_size(container, level):
    """Size in points from a:lvlNpPr/a:defRPr inside a list style, if set."""
    if container is None:
        return None
    node = container.find(f"a:lvl{level + 1}pPr/a:defRPr", NS)
    if node is not None and node.get("sz"):
        return int(node.get("sz")) / 100
    return None


def _placeholder_chain(shape, slide):
    """Layout and master placeholders that this placeholder inherits from."""
    chain = []
    try:
        idx = shape.placeholder_format.idx
        ptype = shape.placeholder_format.type
    except Exception:
        return chain
    layout = slide.slide_layout
    for ph in layout.placeholders:
        if ph.placeholder_format.idx == idx or (idx != 0 and ph.placeholder_format.type == ptype):
            chain.append(ph)
            break
    for ph in layout.slide_master.placeholders:
        if ph.placeholder_format.type == ptype:
            chain.append(ph)
            break
    return chain


def _master_style(shape, slide):
    master = slide.slide_layout.slide_master._element
    styles = master.find("p:txStyles", NS)
    if styles is None:
        return None
    name = "p:otherStyle"
    if shape.is_placeholder:
        t = str(shape.placeholder_format.type)
        name = "p:titleStyle" if "TITLE" in t and "SUB" not in t else "p:bodyStyle"
    return styles.find(name, NS)


def _font_scale(text_frame):
    node = text_frame._txBody.find("a:bodyPr/a:normAutofit", NS)
    if node is not None and node.get("fontScale"):
        return int(node.get("fontScale")) / 100000
    return 1.0


def text_sizes(shape, slide, prs):
    """(size_pt, exact, text) for each non-empty run in a shape's text frame."""
    results = []
    if not shape.has_text_frame:
        return results
    tf = shape.text_frame
    scale = _font_scale(tf)
    own_list = tf._txBody.find("a:lstStyle", NS)
    chain = _placeholder_chain(shape, slide) if shape.is_placeholder else []
    master_style = _master_style(shape, slide)
    default_style = prs._element.find("p:defaultTextStyle", NS)
    for para in tf.paragraphs:
        level = para.level
        para_default = para._p.find("a:pPr/a:defRPr", NS)
        for run in para.runs:
            if not run.text.strip():
                continue
            size, exact = None, True
            if run.font.size is not None:
                size = run.font.size.pt
            elif para_default is not None and para_default.get("sz"):
                size = int(para_default.get("sz")) / 100
            else:
                exact = False
                candidates = [own_list]
                candidates += [ph.text_frame._txBody.find("a:lstStyle", NS) for ph in chain if ph.has_text_frame]
                candidates += [master_style, default_style]
                for c in candidates:
                    size = _lvl_size(c, level)
                    if size:
                        break
                if not size:
                    size = 18.0
            results.append((round(size * scale, 1), exact and scale == 1.0, run.text.strip()))
    return results


def _bbox(shape):
    if None in (shape.left, shape.top, shape.width, shape.height):
        return None
    return (shape.left, shape.top, shape.left + shape.width, shape.top + shape.height)


def measurements(slide, prs, room=None):
    """Lines describing text size, word count, overlaps, off-slide shapes, and pictures."""
    sw, sh = prs.slide_width, prs.slide_height
    sizes, words = [], 0
    for shape in walk(slide.shapes):
        for size, exact, text in text_sizes(shape, slide, prs):
            sizes.append((size, exact, shape.name, text))
            words += len(text.split())
        if getattr(shape, "has_table", False) and shape.has_table:
            for row in shape.table.rows:
                for cell in row.cells:
                    for para in cell.text_frame.paragraphs:
                        for run in para.runs:
                            if run.text.strip():
                                size = run.font.size.pt if run.font.size is not None else 18.0
                                sizes.append((size, run.font.size is not None, shape.name, run.text.strip()))
                                words += len(run.text.split())
    lines, flags = [], []
    smallest = None
    if sizes:
        smallest = min(sizes, key=lambda x: x[0])
        mark = "" if smallest[1] else "≈"
        snippet = smallest[3][:40]
        lines.append(f"- Smallest text: {mark}{smallest[0]:g} pt in '{smallest[2]}' (\"{snippet}\")")
        if smallest[0] < SMALL_TEXT_PT:
            flags.append(f"text below {SMALL_TEXT_PT} pt")
        if room:
            scale = room_scale(prs, room)
            reach = readable_ft(smallest[0], scale)
            lines.append(f"- Smallest text is readable to about {reach:.0f} ft "
                         f"(back row: {room['back_ft']:g} ft)")
            if reach < room["back_ft"]:
                flags.append("too small for the back row")
    lines.append(f"- Words on slide: {words}")
    if words > MANY_WORDS:
        flags.append("many words")
    if any(getattr(s_, "has_chart", False) and s_.has_chart for s_ in walk(slide.shapes)):
        lines.append("- Chart text is not measured; check it on the rendered slide.")

    boxes = []
    for shape in slide.shapes:
        b = _bbox(shape)
        if b is None:
            continue
        area = (b[2] - b[0]) * (b[3] - b[1])
        if area <= 0:
            continue
        if b[0] < 0 or b[1] < 0 or b[2] > sw or b[3] > sh:
            lines.append(f"- '{shape.name}' extends beyond the slide edge")
            flags.append("off-slide shape")
        if area >= 0.9 * sw * sh:
            continue  # background-sized shape; overlaps with it are expected
        if shape.is_placeholder and shape.has_text_frame and not shape.text_frame.text.strip():
            continue
        boxes.append((shape.name, b, area))
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            (n1, b1, a1), (n2, b2, a2) = boxes[i], boxes[j]
            w = min(b1[2], b2[2]) - max(b1[0], b2[0])
            h = min(b1[3], b2[3]) - max(b1[1], b2[1])
            if w > 0 and h > 0:
                share = w * h / min(a1, a2)
                if share > 0.05:
                    lines.append(f"- Possible overlap: '{n1}' and '{n2}' ({share:.0%} of the smaller)")
                    flags.append("overlap")

    for shape in walk(slide.shapes):
        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE and shape.width:
            try:
                px_w, px_h = shape.image.size
            except Exception:
                continue
            inches = shape.width / EMU_PER_INCH
            ppi = px_w / inches if inches else 0
            note = ""
            if ppi >= HIGH_PPI:
                note = "; large image shown small: if it is a screenshot, its text may be too small"
                flags.append("shrunk image")
            elif ppi < LOW_PPI:
                note = "; small image stretched: may look blurry"
                flags.append("low-resolution image")
            lines.append(f"- Picture '{shape.name}': {px_w}×{px_h} px shown {inches:.1f} in wide "
                         f"({ppi:.0f} px per inch{note})")
    return lines, flags, smallest, words


def walk(shapes):
    for shape in shapes:
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(shape.shapes)
        else:
            yield shape


def extract(deck_path: Path, room=None) -> str:
    prs = Presentation(str(deck_path))
    out = [f"# Deck extract: {deck_path.name}", ""]
    out.append(f"Slides: {len(prs.slides)}. Slide size: "
               f"{prs.slide_width / EMU_PER_INCH:.2f} × {prs.slide_height / EMU_PER_INCH:.2f} in")
    out.append("Source: visible slide content, speaker notes, and measurements, extracted "
               "automatically. Layout and images are not shown here; see the rendered PDF if present.")
    out.append("")
    summary, slides_out = [], []
    for i, slide in enumerate(prs.slides, start=1):
        m_lines, m_flags, smallest, words = measurements(slide, prs, room)
        size_txt = "—" if smallest is None else f"{'' if smallest[1] else '≈'}{smallest[0]:g}"
        reach_txt = ""
        if room and smallest is not None:
            reach_txt = f" {readable_ft(smallest[0], room_scale(prs, room)):.0f} |"
        summary.append(f"| {i} | {size_txt} |{reach_txt} {words} | {', '.join(dict.fromkeys(m_flags)) or ''} |")
        out_slide = slides_out
        hidden = slide._element.get("show") == "0"
        title = ""
        if slide.shapes.title is not None and slide.shapes.title.has_text_frame:
            title = slide.shapes.title.text_frame.text.strip()
        out_slide.append(f"## Slide {i}{' (HIDDEN)' if hidden else ''}: {title or '[no title]'}")
        out_slide.append(f"Layout: {slide.slide_layout.name}")
        body, pictures = [], 0
        for shape in walk(slide.shapes):
            if slide.shapes.title is not None and shape.shape_id == slide.shapes.title.shape_id:
                continue
            if shape.has_text_frame:
                t = shape_text(shape)
                if t:
                    body.append(t)
                elif shape.is_placeholder:
                    body.append(f"[empty placeholder: {shape.name}]")
            if getattr(shape, "has_table", False) and shape.has_table:
                body.append("Table:\n" + table_md(shape.table))
            if getattr(shape, "has_chart", False) and shape.has_chart:
                body.append("Chart:\n" + chart_md(shape.chart))
            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                pictures += 1
                desc = alt_text(shape)
                if not desc:
                    alt = "no alt text"
                elif re.search(r"\.(png|jpe?g|gif|bmp|tiff?|svg|emf|wmf)$", desc, re.I):
                    alt = f"alt text is a file name ({desc})"
                else:
                    alt = f"alt text: {desc}"
                body.append(f"Picture '{shape.name}': {alt}")
        out_slide.append("")
        out_slide.append("Visible content:")
        out_slide.extend(body or ["- [none extracted]"])
        notes = ""
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame is not None:
            notes = slide.notes_slide.notes_text_frame.text.strip()
        out_slide.append("")
        out_slide.append("Speaker notes:")
        out_slide.append(notes if notes else "[none]")
        out_slide.append("")
        out_slide.append("Measurements:")
        out_slide.extend(m_lines)
        out_slide.append("")
    out.append("## Measurements summary")
    out.append("")
    out.append("Sizes marked ≈ are inherited from the layout or master, or reduced by automatic "
               "shrinking. Flags use rough thresholds (text below "
               f"{SMALL_TEXT_PT} pt, over {MANY_WORDS} words, images at {HIGH_PPI}+ or under "
               f"{LOW_PPI} px per inch); judge them against the room.")
    out.append("")
    out.append("Text inside pictures, such as screenshots, is not measured: see the picture "
               "resolution flags. Automatic shrinking can differ between PowerPoint and "
               "LibreOffice, so line breaks and overlaps may differ from the rendered images.")
    out.append("")
    if room:
        scale = room_scale(prs, room)
        shape_note = ("fitted to the screen's width and height" if room.get("screen_h_ft")
                      else "assumed to fill the screen's width (screen height not given)")
        out.append(f"Room: screen {room['screen_w_ft']:g} ft wide"
                   + (f" × {room['screen_h_ft']:g} ft high" if room.get("screen_h_ft") else "")
                   + f", back row {room['back_ft']:g} ft away. The slide is {shape_note}, "
                   f"so it appears {scale:.1f} times its size. Guideline: capital letters at least "
                   f"{MIN_ARCMIN} minutes of arc tall, with capitals {CAP_HEIGHT:.0%} of the font "
                   f"size. Text must be at least about {needed_pt(room['back_ft'], scale):.0f} pt "
                   f"to be read comfortably from the back row.")
        out.append("")
        out.append("| Slide | Smallest text (pt) | Readable to (ft) | Words | Flags |")
        out.append("| - | - | - | - | - |")
    else:
        out.append("| Slide | Smallest text (pt) | Words | Flags |")
        out.append("| - | - | - | - |")
    out.extend(summary)
    out.append("")
    out.extend(slides_out)
    return "\n".join(out)


def render(deck_path: Path, out_dir: Path) -> str:
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        return "Rendering skipped: LibreOffice (soffice) not found."
    # Render from a copy with every slide unhidden, so slide images match slide numbers.
    prs = Presentation(str(deck_path))
    for slide in prs.slides:
        if slide._element.get("show") is not None:
            del slide._element.attrib["show"]
    copy = out_dir / (deck_path.stem + ".pptx")
    if copy.resolve() == deck_path.resolve():
        copy = out_dir / (deck_path.stem + "_render.pptx")
    prs.save(str(copy))
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(out_dir), str(copy)],
                   check=True, capture_output=True, timeout=300)
    copy.unlink()
    pdf = out_dir / (copy.stem + ".pdf")
    if not pdf.exists():
        return "Rendering failed: no PDF produced."
    msg = f"Rendered PDF: {pdf}"
    if shutil.which("pdftoppm"):
        img_dir = out_dir / "slides"
        img_dir.mkdir(exist_ok=True)
        subprocess.run(["pdftoppm", "-png", "-r", "120", str(pdf), str(img_dir / "slide")],
                       check=True, capture_output=True, timeout=300)
        msg += f"\nSlide images: {img_dir}"
    else:
        msg += "\nImages skipped: pdftoppm not found."
    msg += ("\nNote: LibreOffice rendering can differ from PowerPoint in fonts and layout. "
            "Hidden slides are included in the rendering so image numbers match slide numbers; "
            "the extract marks which slides are hidden.")
    return msg


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--render", action="store_true", help="also render to PDF and PNG images")
    ap.add_argument("--screen-width-ft", type=float, help="projected image width, in feet")
    ap.add_argument("--screen-height-ft", type=float, help="projected image height, in feet (optional)")
    ap.add_argument("--back-row-ft", type=float, help="distance from the screen to the back row, in feet")
    args = ap.parse_args()
    room = None
    if args.screen_width_ft and args.back_row_ft:
        room = {"screen_w_ft": args.screen_width_ft, "screen_h_ft": args.screen_height_ft,
                "back_ft": args.back_row_ft}
    elif args.screen_width_ft or args.back_row_ft:
        sys.exit("Give both --screen-width-ft and --back-row-ft (and optionally --screen-height-ft).")
    if args.deck.suffix.lower() != ".pptx":
        sys.exit("Only .pptx is supported. Export other formats (Keynote, Google Slides) to .pptx or PDF first.")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    md_path = args.out_dir / (args.deck.stem + "_extract.md")
    md_path.write_text(extract(args.deck, room), encoding="utf-8")
    print(f"Extract: {md_path}")
    if args.render:
        print(render(args.deck, args.out_dir))


if __name__ == "__main__":
    main()
