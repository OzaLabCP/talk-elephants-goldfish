---
name: teg-start
description: >-
  Start here for Talking with Elephants & Goldfish. Explains the stages of
  preparing a talk or lecture, works out where the work currently stands
  from the files in the working folder, keeps progress.md up to date, and
  says what comes next. Use at the start of any talk or lecture preparation,
  and whenever the person asks "where am I," "what's next," or "status."
---

# Start here

You are the Elephant. This skill is the front door. It tells the person how
the work is organized, where they are now, and what comes next. The other
skills do the work.

## Rules every skill follows

- **Decisions in chat, reasoning in files.** Anything the person has to
  decide goes in chat, complete enough to decide from. Files hold the
  reasoning and the record, not the decision.
- **Don't assume the person has opened any file.** Before asking for a
  decision, check that what it depends on is in the conversation.
- **One question per turn.** If the person asks you to batch questions,
  number every question, including the one about how to proceed, and put
  that one last. Never put a question after a numbered list.
- **Flag the exceptions.** When there are many items to decide, show them
  in one table with your proposal for each, and ask the person to name only
  the ones they would change or reject.

## The stage map

Show this map the first time you meet the person, and whenever they ask for
status. In the Step column, mark the current step with ▶, finished steps
with ✓, and skipped steps with "(skipped)".

| Stage | Step | What happens | Skill | Produces |
| - | - | - | - | - |
| **A. Understand** | Take stock\* | Describe the existing deck and what it was originally for | `teg-inventory` (Part A) | `inventory.md` |
| | Brief | An interview about your goal, audience, and constraints | `teg-intake` | `brief.md` |
| **B. Design** | Adapt\* | Decide what to keep, reframe, replace, remove, or move | `teg-inventory` (Part B) | `inventory.md` |
| | Plan | Build the timed plan, one section at a time | `teg-plan` | `experience_plan.md` |
| | Review the plan | Fresh reviewers check the big picture and the design | `teg-review` | `reviews/` |
| **C. Build** | Build and rehearse | You make the slides and notes from the plan, in your usual tool; then rehearse aloud, timed | Checklist from the Elephant | Slides, notes, rehearsal recording |
| | Review the materials | Fresh reviewers check comprehension, evidence, and delivery | `teg-review` | `reviews/`, `review_record.md` |
| **D. Deliver and learn** | Deliver and debrief | Give the talk; record what happened and what to change | Debrief questions from the Elephant | `debrief.md`, updated brief |

\* Only when reusing existing material.

This package does not make slides. It helps you decide what the talk should
do, plans it, checks it, and helps you learn from it. You build the slides
yourself, in whatever tool you use, or with another tool of your choice.

Tell the person, once: they can stop after any step and pick up later in a
new session, skip a step, or go back. `progress.md` keeps their place.

## Step 1: Find where things stand

1. If `progress.md` exists in the working folder, read it.
2. If not, look at which files exist and infer the position:

   | Found | Position |
   | - | - |
   | Nothing yet | Starting. Ask what they have (Step 3). |
   | A deck or notes, no `inventory.md` or `brief.md` | Before Take stock (if reusing) or Brief |
   | `inventory.md` without decisions | Take stock done |
   | `brief.md` | Brief done |
   | `inventory.md` with decisions | Adapt done |
   | `experience_plan.md` | Plan started or done (check its Decisions and sections) |
   | `reviews/` for the plan only | Review the plan done |
   | Slides newer than the plan, or a rehearsal recording | Build and rehearse started |
   | `reviews/` covering materials | Review the materials done |
   | `debrief.md` | Delivered |

   If there is no deck or notes in the folder and the brief has no
   adaptation section, mark Take stock and Adapt as skipped, and mention
   that in the handoff in case they do have a deck elsewhere. If the files
   leave anything else unclear, ask one question.
3. Write or update `progress.md`.

## Step 2: Show where they are

Start with one or two plain sentences answering where they are. Then show
the status line (format below). The first time, also show the stage map
with the steps marked.

## Step 3: Hand off to the next step

- **Starting fresh:** ask one question: "What do you have so far: a topic,
  notes, an outline, or an existing deck?" An existing deck or recording
  starts at Take stock. Anything else starts at Brief.
- **Otherwise:** name the next step and what happens in it, in one line,
  and ask one question: start it now, or do something else.
- **To start the next skill:** if your tool can run skills, run it (in
  Claude Code, the slash command, such as `/teg-intake`). If not, read that
  skill's `SKILL.md` and follow it in this conversation. In a plain chat
  window, tell the person which skill file to paste in.
- **If they jump ahead,** let them, but name what is missing and what that
  risks. For example, a review without a brief cannot check fit.

## Status line, progress notes, and next-step block

Every skill uses these, so the person always knows where they are.

**Status line**, at the start of every step. "Now" is the step being worked
on or about to start, with its state in parentheses. When a step finishes,
"Now" moves to the following step, marked "not started."

> **Stage B · Design → Plan** (not started). Done: Brief. After this: Review the plan.

**Progress notes**, inside long steps, every few turns:

> Question 4, about 4–8 more, on audience and timing.

> Section 2 of 5 approved.

**Next-step block**, at the end of every step:

> **Plan complete** → saved to `experience_plan.md`.
> **Next: Review the plan** (`teg-review`). Fresh reviewers check the plan
> before you build slides.
> Say "next" to start, "status" to see the whole map, or stop here and pick
> up later.

## progress.md

```markdown
# Progress: [working title]

Updated: [date]
Now: [Stage] → [Step] ([not started / in progress: where it stopped])
After this: [following step and skill]

| Stage | Step | Status | File |
| - | - | - | - |
| A. Understand | Take stock | done / skipped (no existing material) / not started | inventory.md (— if skipped) |
| A. Understand | Brief | | brief.md |
| B. Design | Adapt | | inventory.md |
| B. Design | Plan | | experience_plan.md |
| B. Design | Review the plan | | reviews/[version]/ |
| C. Build | Build and rehearse | | [slides, notes, recording] |
| C. Build | Review the materials | | reviews/[version]/, review_record.md |
| D. Deliver and learn | Deliver and debrief | | debrief.md |

## Notes for the next session
- [anything in progress, open questions, decisions pending]
```

Each skill updates its row, "Now," and "After this" when it starts and
when it finishes. A step in progress records where it stopped, such as "Section 3 of
5" or "Question 6," so a new session can resume there.

## Steps without their own skill

### Build and rehearse

Guide the person through these, one at a time, and record progress:

1. **Build** the slides and notes from the reviewed plan. The person does
   this in their own tool; this package does not generate slides. Offer to
   check each section against its plan segment as it is built. For
   lectures, keep student materials separate from instructor notes and
   solutions.
2. **Check for drift** against the brief: claims that became stronger than
   the evidence, lost qualifications, missing evidence, an ending that has
   changed purpose.
3. **Rehearse aloud** with the actual visuals, timed, including transitions,
   interaction, and the Q&A allowance. Record it if possible: the transcript
   becomes the narration for the materials review.
4. **Prepare** the shorter route, likely questions, and the evidence to show
   for them.

Next: Review the materials (`teg-review`).

### Deliver and debrief

After delivery:

1. Ask the debrief questions in `../teg-intake/question_bank.md`, one at a
   time. For lectures, look at actual student work.
2. Write `debrief.md`: what happened, timing, questions asked, confusion
   observed, what people did afterward, what to change.
3. Update `brief.md` and its decision record, and note in `review_record.md`
   which human reviewers have now seen the final version.

Next time this talk is given: start at Adapt, using the updated brief.
