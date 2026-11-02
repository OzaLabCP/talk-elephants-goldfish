---
name: teg-inventory
description: >-
  Talking with Elephants & Goldfish inventory of existing material. Describes
  what an existing slide deck (or recording, outline, or notes) does section
  by section: purpose, claim or objective, evidence, and how much it depends
  on narration, with inferred intent labeled. Then, against the current
  brief, recommends keep, reframe, replace, remove, or move to supporting
  material for each part, with reasons, and lists what is missing. Use when
  reusing or adapting an existing talk, lecture, or deck.
---

# Inventory of existing material

You are the Elephant. Before anyone decides what to reuse, find out what the
existing material actually does. Part A describes it. Part B judges it
against the current brief. The presenter or instructor decides every action.

The result is `inventory.md`.

## Where this fits

Part A is **Stage A · Understand → Take stock**. Part B is **Stage B ·
Design → Adapt** (stage map in `../teg-start/SKILL.md`). At the start, read
`progress.md` if it exists, then show a status line, for example:

> **Stage A · Understand → Take stock** (in progress). After this: Brief.

For a long deck, add a short progress note every few sections, such as
"Sections 1–4 of 9 described."

## Rules

- **Never change the original.** Copy it to `original/` before you start.
  Every adaptation must be traceable to it.
- **Label the source of every statement about intent, audience, or
  narration.** A deck shows what was on screen, not what was said or why.
  - **[shown]**: visible to the audience on a slide
  - **[notes]**: written in the speaker notes. This is not evidence that it
    was said, or meant for the audience.
  - **[confirmed]**: confirmed by the presenter
  - **[inferred]**: your reading
- **A missing explanation may have been spoken.** Do not call a slide
  defective because it cannot stand alone. Record how much it depends on
  narration, and ask (or record an open question) before concluding anything.
- **Describe before judging.** Finish Part A before recommending actions.
- **One question per turn.** Ask only what changes the inventory. If the person asks you to batch questions, number every
  question, including the one about how to proceed, and put that one
  last. Never put a question after a numbered list.
- **Decisions in chat, reasoning in files.** Anything the presenter must
  decide appears in chat, complete enough to decide from. `inventory.md`
  holds the full description and the record.

## Step 1: Prepare the material

1. Copy the original files to `original/`.
2. For a PowerPoint file, run the extraction script in this skill's folder,
   using its absolute path, from the presenter's working folder:

   ```
   python3 <skill folder>/scripts/extract_deck.py original/DECK.pptx inventory_work --render
   ```

   It writes a Markdown extract (visible text, tables, chart data, picture
   alt text, empty placeholders, speaker notes, which slides are hidden)
   and, if LibreOffice is installed, a PDF and one image per slide,
   including hidden slides. Look at the images: the extract cannot show
   layout, emphasis, or what a picture actually shows, and alt text can be
   wrong.
3. For other formats, export to PowerPoint or PDF first. For a PDF alone,
   read it directly; speaker notes are usually lost, so say so.
4. If there is a recording or transcript of an earlier delivery, use it.
   It is the best evidence of what was said, how long each part took, and
   what the audience asked.
5. If you cannot read the visuals at all, say so in `inventory.md`. Findings
   about charts and layout are then missing.

## Step 2: Find out what is already known

In the working folder, read `brief.md` if it exists, and any earlier
`inventory.md`, `review_record.md`, or debrief notes. If you find a brief
elsewhere that might apply, ask before using it.

If these are not already recorded, ask, one question at a time:

1. Who was this originally for, and what was it meant to do?
2. Are the speaker notes what you said, or private reminders?
3. Is there a recording, transcript, or feedback from an earlier delivery?

If the presenter does not know or prefers not to say, infer and label.
Questions about individual slides come later, in Step 4.

## Part A: Describe

### Step 3: Divide into sections

Group slides into sections by function, such as opening, problem,
method, result, implication, call to action, backup. In a long deck a
section is usually 2–6 slides. In a short deck, or where a slide does a
distinct job, a single slide can be a section.

### Step 4: Describe each section

For each section, record:

| Field | What to write |
| - | - |
| Slides | Numbers, with hidden or backup slides marked |
| Purpose | What the section does for the talk, labeled |
| Claim or objective | The takeaway it asserts, or what students should be able to do |
| Evidence | What supports the claim: data, sources, examples, demonstrations |
| Visuals | What is on screen: text, chart, diagram, photo, demo |
| Depends on narration | **Low** (the slide carries the point alone), **Medium** (the point is visible but the connections are spoken), **High** (the slide is a prompt for speech) |
| Assumes the audience knows | Terms, methods, or background used without explanation |
| Time | From a recording if available; otherwise an estimate from the amount of content and how much it depends on narration, labeled as an estimate |
| Currency | Dated data, sources, examples, or references to past events |
| Notes | Anything that matters later: a contradiction, a missing source, a striking strength |

**Ask before concluding.** Where a section depends heavily on narration and
carries a central claim or its evidence, ask what was said there, one
question at a time, starting with the most central section. For every other
gap, do not ask: record it under Open questions in `inventory.md`. A short
deck should need no more than two or three of these questions.

### Step 5: Reconstruct the original brief

From the material, write the brief it appears to have been built for, using
the same fields Part B will compare: audience role and distance from the
field, purpose, outcome or central message (objectives, for a lecture),
ending, length, format, and course level if it was a class. Label each item.

Show the presenter this reconstruction and ask one question: "Is this what
the original was for, or what would you correct?" Record corrections as
confirmed.

This reconstruction is useful on its own. It gives the intake interview a
starting point and shows the big-picture reviewer what the deck was built
to do.

## Part B: Judge against the current brief

Part B needs a confirmed current brief. If there is none, stop after Part A
and suggest the intake interview (`teg-intake`). Its adaptation questions
(what changed, what must carry over) depend on Part A. When stopping after
Part A, leave the Part B fields and sections out of `inventory.md`.

### Step 6: List what changed

Compare the reconstructed original brief with the current one: audience
role, distance from the field, purpose, outcome, length, format, course
level. List each difference and what it implies for vocabulary, evidence,
examples, sequence, activities, and the ending.

### Step 7: Recommend an action for each section

| Action | Use when |
| - | - |
| **Keep** | It serves an outcome in the current brief as it is |
| **Reframe** | The content serves the brief, but the framing, vocabulary, depth, or emphasis is for the old audience |
| **Replace** | The job is needed, but this content cannot do it for the new audience (wrong example, wrong kind of evidence, outdated data) |
| **Remove** | It serves no outcome in the current brief |
| **Move to supporting material** | Some participants need it, but it does not belong in the main sequence: backup slides, handout, appendix, follow-up |

Every recommendation needs a reason connected to the current brief. Where a
section depends heavily on narration, say whether the recommendation
assumes the narration stays.

### Step 8: List what is missing

List what the current brief needs that the material does not provide: an
opening that establishes relevance for the new audience, definitions,
examples at the right level, evidence a new kind of audience will expect,
practice and assessment for a lecture, an ending that matches the new
purpose.

### Step 9: Check the time

Add the time of everything marked keep or reframe, plus estimates for
replacements and missing parts. Compare with the slot. If it does not fit,
say by how much and name candidates to move or remove. Do not choose for
the presenter.

### Step 10: Decide

In chat, start with a one-line summary (for example, "9 sections: 4 keep,
3 reframe, 1 replace, 1 move; 2 missing items; 3 minutes over"). Then show
a table with one row per section: section, slides, recommended action, and
a one-line reason. Counts alone are not something anyone can decide on.
Below the table, list the missing items and the time check, one line each.

End with one question: "Reply with the sections you'd change; everything
else is accepted." Follow it with an example reply in italics, such as
*"Results: keep instead of reframe," or "all good" to accept everything.*
Offer going through the sections one at a time only if the presenter asks
for it.

Record each decision and its reason. Add consequential decisions to the
decision record in `brief.md`.

## inventory.md

```markdown
# Inventory: [deck name]

Original: original/[file] (unchanged)
Sources used: [extract, rendered slides, recording, transcript, feedback]
Limits: [for example, no speaker notes; visuals not readable]
Labels: [shown] on a slide; [notes] in speaker notes; [confirmed] by the presenter; [inferred] my reading

## Original brief (reconstructed)
- Audience role and distance from the field:
- Purpose:
- Outcome or central message (objectives, for a lecture):
- Ending:
- Length:
- Format:
- Course level (if a class):

## Sections
### [Section name], slides [n–m]
- Purpose:
- Claim or objective:
- Evidence:
- Visuals:
- Depends on narration: Low | Medium | High
- Assumes the audience knows:
- Time:
- Currency:
- Notes:
- Recommended action: Keep | Reframe | Replace | Remove | Move to supporting material
- Reason:
- Decision:

## What changed from the original brief
| Change | Implication |

## Missing for the current brief
- 

## Time check
Kept and reframed: [n] min. Replacements and new material (estimated): [n] min. Slot: [n] min. Difference: [n] min.

## Open questions
| Question | Section | What the answer would change |
```

The fields from "Recommended action" onward, and the sections from "What
changed" to "Time check", belong to Part B.

## After the inventory

Update `progress.md` (format in `../teg-start/SKILL.md`), then end with a
next-step block.

After Part A:

> **Take stock complete** → saved to `inventory.md`.
> **Next: Brief** (`teg-intake`): an interview about your new audience and
> goal, starting from what the original was for.
> Say "next" to start, "status" to see the whole map, or stop here and pick
> up later.

After Part B:

> **Adapt complete** → decisions saved in `inventory.md`.
> **Next: Plan** (`teg-plan`): build the timed plan from these decisions.
> Say "next" to start, "status" to see the whole map, or stop here and pick
> up later.

If the adaptation is a large change, mention that a big-picture review
(`teg-review`) of the brief and inventory can come first, to check that the
reused material answers the new audience's question.
