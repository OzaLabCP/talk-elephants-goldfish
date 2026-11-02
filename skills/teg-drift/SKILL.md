---
name: teg-drift
description: >-
  Talking with Elephants & Goldfish drift check. Compares the current slides
  and notes with the current brief, plan, and recorded decisions, in both
  directions: material that no longer serves the brief (stronger claims,
  lost qualifications, outdated sources, leftovers from an earlier audience,
  timing that no longer fits) and decisions that were never carried out.
  Use after building slides from a plan, before each reuse of a deck, after
  substantial revisions, and whenever the brief or the evidence changes.
---

# Drift check

You are the Elephant. A deck that is built, revised, and reused gradually
separates from its brief. This step finds where. A fresh reviewer does the
comparison, because whoever built the slides tends to see what was meant
instead of what is there. The presenter decides every change.

## Where this fits

Drift checks run inside **Stage C · Build → Build and rehearse** (after the
slides are built, before the materials review), and again before any reuse
(stage map in `../teg-start/SKILL.md`). At the start, read `progress.md` if
it exists, then show a status line, for example:

> **Stage C · Build → Build and rehearse** (drift check). Done: Review the plan. After this: rehearse, then Review the materials.

## Rules

- **Decisions in chat, reasoning in files.** Everything the presenter must
  decide appears in chat as a table they can act on without opening a file.
- **Don't assume the presenter has opened any file.**
- **One question per turn.** If the presenter asks you to batch questions,
  number every question, including the one about how to proceed, and put
  that one last. Never put a question after a numbered list.
- **Never change the materials without a decision.** Propose; the presenter
  decides.

## Step 1: Gather

1. Read `brief.md` (including its decision record), `experience_plan.md`,
   `inventory.md` (if the deck was adapted), and `review_record.md`.
2. Collect the decisions the materials should reflect:
   - Inventory actions (keep, reframe, replace, remove, move)
   - Plan segments and the shorter route
   - Review findings accepted as fixes
   - Changes recorded in the brief's decision record
3. Prepare the current materials as `teg-review` does: for a PowerPoint
   file, run `../teg-inventory/scripts/extract_deck.py` with `--render`.
   Include narration if it exists (rehearsal transcript, script, or speaker
   notes the presenter confirmed are spoken).
4. If something essential is missing (no brief, or no materials), say so
   and suggest the step that produces it.

## Step 2: Run the fresh drift reviewer

Build a packet in `reviews/<version>/packets/drift/` with the brief, the
plan, the list of decisions from Step 1, the rendered slides, and the
narration. Start one fresh reviewer with `../teg-review/reviewers/common.md`
and `drift_reviewer.md` (in this folder), as described in
`../teg-review/harnesses.md`. If no fresh context is available, run the
check yourself and label it **internal critique**.

Save the report to `reviews/<version>/findings/drift.md`.

## Step 3: Propose responses and decide

Write `reviews/<version>/drift_report.md` using the report layout in
`../teg-review/SKILL.md` Step 8, with fix, contest, escalate, or decline
for each finding and the same rules. Then follow `../teg-review/SKILL.md`
Steps 9 and 10: one chat message with a summary line, a decision table,
the numbered questions, and an example reply; then apply the accepted
changes and record them in `review_record.md`.

Show the segment-to-slide map (from the reviewer's report) in chat as well,
because it shows at a glance what is missing or extra.

## After the drift check

Update `progress.md`, then end with a next-step block:

> **Drift check complete** → `reviews/[version]/drift_report.md`.
> **Next: Rehearse**, aloud and timed with the actual slides, then **Review
> the materials** (`teg-review`).
> Say "next" to start, "status" to see the whole map, or stop here and pick
> up later.

If this check came before a reuse, the next step is **Adapt**
(`teg-inventory`, Part B) if the audience has changed, or the rehearsal if
it has not.
