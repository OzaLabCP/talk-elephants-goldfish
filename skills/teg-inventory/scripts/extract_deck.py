#!/usr/bin/env python3
"""Extract a PowerPoint deck into a Markdown inventory source.

Writes one Markdown file with, for every slide: number, hidden flag, layout,
title, visible text, tables, charts (type, series, categories), pictures
(with alt text), and speaker notes. Optionally renders the slides to a PDF
and PNG images so a reviewer can see layout and type size.

Usage:
    python3 extract_deck.py DECK.pptx OUT_DIR [--render]

Requires python-pptx. Rendering also requires LibreOffice (soffice) and
pdftoppm (poppler-utils).
"""

import argparse
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


def walk(shapes):
    for shape in shapes:
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(shape.shapes)
        else:
            yield shape


def extract(deck_path: Path) -> str:
    prs = Presentation(str(deck_path))
    out = [f"# Deck extract: {deck_path.name}", ""]
    out.append(f"Slides: {len(prs.slides)}")
    out.append("Source: visible slide content and speaker notes, extracted automatically. "
               "Layout, type size, and images are not shown here; see the rendered PDF if present.")
    out.append("")
    for i, slide in enumerate(prs.slides, start=1):
        hidden = slide._element.get("show") == "0"
        title = ""
        if slide.shapes.title is not None and slide.shapes.title.has_text_frame:
            title = slide.shapes.title.text_frame.text.strip()
        out.append(f"## Slide {i}{' (HIDDEN)' if hidden else ''}: {title or '[no title]'}")
        out.append(f"Layout: {slide.slide_layout.name}")
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
                body.append(f"Picture {pictures}: " + (f"alt text: {desc}" if desc else "no alt text"))
        out.append("")
        out.append("Visible content:")
        out.extend(body or ["- [none extracted]"])
        notes = ""
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame is not None:
            notes = slide.notes_slide.notes_text_frame.text.strip()
        out.append("")
        out.append("Speaker notes:")
        out.append(notes if notes else "[none]")
        out.append("")
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
        subprocess.run(["pdftoppm", "-png", "-r", "80", str(pdf), str(img_dir / "slide")],
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
    args = ap.parse_args()
    if args.deck.suffix.lower() != ".pptx":
        sys.exit("Only .pptx is supported. Export other formats (Keynote, Google Slides) to .pptx or PDF first.")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    md_path = args.out_dir / (args.deck.stem + "_extract.md")
    md_path.write_text(extract(args.deck), encoding="utf-8")
    print(f"Extract: {md_path}")
    if args.render:
        print(render(args.deck, args.out_dir))


if __name__ == "__main__":
    main()
