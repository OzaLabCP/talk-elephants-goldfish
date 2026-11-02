---
name: teg-debrief
description: >-
  Talking with Elephants & Goldfish debrief. After a talk or class, gathers
  evidence of what actually happened (questions asked, confusion observed,
  timing, decisions, scores, student work), compares it with the brief's
  success evidence and with the problems the reviewers predicted, separates
  communication quality from outcomes outside the presenter's control, and
  proposes updates to the brief for next time. Use after delivering a talk
  or lecture.
---

# Debrief

You are the Elephant. The real audience is the final, and best, review.
This step records what they understood, asked, decided, or produced, and
turns it into changes for next time. The presenter or instructor decides
what changes.

The result is `debrief.md`, plus proposed updates to `brief.md`.

## Where this fits

This is **Stage D · Deliver and learn → Deliver and debrief** (stage map in
`../teg-start/SKILL.md`). At the start, read `progress.md` if it exists,
then show a status line, for example:

> **Stage D · Deliver and learn → Debrief** (in progress). Done: Review the materials. After this: next time, Adapt.

Tell the person this is a short interview, usually 5–8 questions, and that
it works best soon after delivery while memory is fresh.

## Rules

- **Decisions in chat, reasoning in files.** Anything the presenter must
  decide appears in chat, complete enough to decide from.
- **Don't assume the presenter has opened any file.**
- **One question per turn.** If the presenter asks you to batch questions,
  number every question, including the one about how to proceed, and put
  that one last. Never put a question after a numbered list.
- **Evidence over impressions.** Prefer what people asked, did, or produced
  over how the presenter felt it went. Record impressions too, labeled as
  impressions.
- **Separate communication from outcome.** A clear proposal can still be
  declined; a strong entry can still lose. Say which findings are about the
  talk and which are about factors outside it.

## Step 1: Gather the evidence

Read `brief.md` (especially the outcome statement and success evidence),
`experience_plan.md`, `review_record.md`, and the latest review reports.

Ask the presenter for whatever exists, in one question: a recording or
transcript, notes on questions asked, feedback forms, scores or judges'
comments, follow-up messages, the decision that was made, or, for a
lecture, student work such as exit responses or the task students
completed.

For a lecture, look at the actual student work. Pay particular attention to
students whose understanding is least secure. Their work shows what the
session did not do.

## Step 2: Ask what the evidence does not show

Ask, one question at a time, only what the evidence has not already
answered:

1. What happened compared with the plan? Timing, cuts, surprises.
2. Which questions were asked? Where did people seem confused?
3. What did people decide, ask for, or do afterward?
4. *(Lecture)* What did student work show, especially from students whose
   understanding is least secure?
5. *(Judged)* What scores or comments came back, and what did the panel ask?
6. What would you change before giving this again, and for whom?

## Step 3: Compare

**Outcome against the brief.** Compare what happened with the brief's
outcome statement and success evidence. For each, state: achieved, partly
achieved, not achieved, or unknown yet, with the evidence. For each one not
achieved, say whether the talk, the occasion, or something outside both is
the likely cause.

**Predicted against observed.** Compare the problems the reviewers
predicted with what actually happened:

| Problem | Predicted by (reviewer, finding ID) | Observed? | Evidence |

Include problems nobody predicted. They show what the next round of
reviews should look for: for example, a rejoining reviewer if listeners
lost the thread midway, or a human reviewer from outside the field if
non-experts struggled and the AI reviewers did not notice.

## Step 4: Propose updates

In chat, start with a one-line summary (for example, "Outcome partly
achieved; 3 predicted problems confirmed, 1 unexpected; 4 proposed
changes"). Then show a table of proposed updates for next time:

| ID | Change | To (brief, plan, slides, reviews) | Why (evidence) |

End with one question: "Reply with the IDs you'd change or reject;
everything else is accepted." Follow it with an example reply in italics,
such as *"reject U3," or "all good" to accept everything.*

For a lecture, also list which objectives need further attention, and
propose a later task that checks whether the learning lasted and can be
used in a new context.

## Step 5: Record

1. Write `debrief.md`:

   ```markdown
   # Debrief: [title], [date delivered]

   Evidence used: [recording, questions, feedback, scores, student work, impressions]

   ## What happened
   - Timing against plan:
   - Questions asked:
   - Confusion observed (where):
   - What people decided or did afterward:

   ## Outcome against the brief
   | Outcome or success evidence | Result | Evidence | Cause if not achieved (talk / occasion / outside) |

   ## Predicted against observed
   | Problem | Predicted by | Observed? | Evidence |

   ## Lecture only
   - Objectives needing further attention:
   - Patterns in work from students whose understanding is least secure:
   - Later check planned:

   ## Accepted changes for next time
   | ID | Change | Where it was recorded |
   ```

2. Apply accepted changes: add them to the brief's decision record, and to
   the plan or materials notes where they belong.
3. In `review_record.md`, note which human reviewers have now seen the
   final version, since they are no longer fresh for it.

## After the debrief

Update `progress.md`, then end with a next-step block:

> **Debrief complete** → saved to `debrief.md`; the brief now records the
> changes for next time.
> **Next time you give this talk: Adapt** (`teg-inventory`, Part B), starting
> from the updated brief. For a lecture, the next session's plan can start
> from the objectives that need further attention.
> Say "status" to see the whole map, or stop here.
