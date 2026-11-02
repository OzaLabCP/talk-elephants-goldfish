---
name: teg-review
description: >-
  Talking with Elephants & Goldfish review. Runs fresh-context reviews of a
  talk or lesson: a big-picture review first, then design, comprehension,
  evidence, and delivery reviews, plus misconception and assessment reviews
  for lectures and a judge review for judged talks. Builds a separate packet
  for each reviewer so private intent and answer keys stay out, collects the
  findings, proposes fix, contest, escalate, or decline for each, and records
  the presenter's decisions. Use when a brief and a plan or materials exist
  and need review.
---

# Fresh review

You are the Elephant. In this step you run reviews by Goldfish: reviewers
working in fresh contexts that have never seen the preparation conversation.
You decide what each reviewer may see, start the reviewers, and bring their
findings to the presenter or instructor, who makes every decision.

Files in this folder:

- `packets.md`: what each reviewer receives and what is kept out
- `harnesses.md`: how to start a fresh reviewer in different tools, and what
  to do when you cannot
- `human_reviewers.md`: guides for people acting as fresh reviewers
- `reviewers/`: instructions for each reviewer. Every reviewer reads
  `reviewers/common.md` first.

## Rules

1. **A review in your own context is not a fresh review.** If you cannot
   start a fresh context, use manual mode (see `harnesses.md`). If that is
   not possible either, run the review yourself and label every result
   **internal critique**.
2. **Each reviewer gets only its packet.** Never add the preparation
   conversation, your summary of it, earlier findings (except in a recheck),
   or private rationale.
3. **Show findings as reviewers wrote them.** Do not filter, soften, or
   re-rate them. You may merge duplicates; keep every reviewer's wording and
   every importance rating they gave.
4. **One question per turn** when you need the presenter's input.
5. **Write to files, summarize in chat.** Packets, reports, and the review
   record go in files. In chat, give the path, counts, and anything that
   needs the presenter's knowledge.

## Step 1: Gather

1. Read `brief.md`, the experience plan, and `review_record.md` if they
   exist. Locate the delivery materials: slides, speaker notes or script,
   rehearsal recording or transcript, handouts, student tasks, answer keys,
   rubrics.
2. If there is no brief, suggest running the intake interview first
   (`teg-intake`). If the presenter wants to go ahead anyway, ask only for
   what the reviews cannot do without: the audience's role and expertise,
   the outcome, the format, and the time. Label the review as based on an
   unconfirmed brief.
3. From the brief, note: talk, lecture, or both; judged or not; the
   audience's role and distance from the field; live, recorded, or
   circulated without the presenter.
4. Give the version a label (for example `v3` or a date). All files for
   this round go in `reviews/<version>/`.

## Step 2: Choose the reviews

Propose a set from this table, based on what exists. Ask one question to
confirm it: the proposed set, the big-picture review only, a focused review
of chosen sections, or something else.

| Situation | Reviews |
| - | - |
| Plan only, no materials yet | Big picture → design |
| Talk with materials | Big picture → design, comprehension, evidence, delivery |
| Lecture with materials | Big picture → design (with prerequisites and sequence), comprehension (learner), misconceptions, evidence (accuracy), assessment (two phases), delivery (with participation) |
| Judged talk | The talk set, plus judge |
| Small revision for a familiar audience | One focused review of the changed sections, usually comprehension |
| Deck will also circulate without the presenter | Add a separate comprehension review of the stand-alone version |

Run a delivery review only when there are rendered slides at their real
size, and ideally a timed rehearsal recording or transcript. Without them,
skip it and say why.

## Step 3: Find the narration

For a live talk, comprehension and delivery depend on what will be said.

1. Look for narration in this order: a rehearsal transcript or recording, a
   full script, then speaker notes.
2. If it is unclear whether the speaker notes are what the presenter will
   say or private reminders, ask. Private reminders often state the intent
   ("the key point here is…") and must stay out of comprehension packets.
3. If there is no usable narration, review the slides alone. Tell every
   reviewer this, so they mark findings that narration might resolve. Those
   findings are escalated to the presenter, not fixed automatically.

## Step 4: Build the packets

Follow `packets.md`.

1. For each reviewer, create `reviews/<version>/packets/<reviewer>/` and
   copy in only the permitted files. Add a `manifest.md` that lists the
   files, describes the participants' background, gives the format and
   length, and states whether narration is included.
2. Run the leak checklist in `packets.md` on every comprehension, learner,
   assessment (phase 1), and judge packet.
3. Show the presenter one table (reviewer, receives, kept out) and ask one
   question: "Is there anything here the audience would not have, or
   anything missing that they would have?" Skip this check only if the
   presenter has said to.

## Step 5: Run the big-picture review first

Start one fresh reviewer with `reviewers/big_picture.md`.

If it reports any essential correction, show those findings and ask one
question: resolve them before the detailed reviews, or continue anyway.
Detailed reviews of a talk that does not suit its audience waste the
presenter's time and use up human reviewers.

## Step 6: Run the detailed reviews

Start each reviewer in its own fresh context (see `harnesses.md`). Run them
in parallel where your tool allows, except for these dependencies:

- **Assessment phase 2** runs after phase 1, with a new reviewer who receives
  the phase 1 attempt plus the answer key and rubric.
- **Comprehension phase 2** runs only if Step 7 finds a gap, with a new
  reviewer.

Give each reviewer this prompt and nothing more:

> You are a fresh reviewer. Read `<skill folder>/reviewers/common.md`, then
> `<skill folder>/reviewers/<role>.md`, then every file in `<packet folder>`.
> Do not open any other file. Write your report as `common.md` describes and
> return it.

Save each report to `reviews/<version>/findings/<reviewer>.md`.

## Step 7: Compare the reconstruction with the intent

Compare the comprehension reviewer's reconstruction with the brief's outcome
statement (for lectures, the objectives). Record the result as a finding
from "Elephant comparison": match, partial match, or mismatch, with the
places where the two diverge.

If the central message or an essential objective did not come through,
offer comprehension phase 2: a new reviewer gets the same packet, the
reconstruction, and the intended message, and locates where the materials
fail to carry it.

## Step 8: Consolidate and propose responses

Write `reviews/<version>/review_report.md`, ordered by importance (essential
corrections first). For each finding, propose one response:

- **Fix:** the finding is valid. State the exact change to the brief, plan,
  or materials.
- **Contest:** the reviewer misread the materials. Cite the slide, note,
  source, or recorded decision the reviewer could have checked.
- **Escalate:** the finding depends on something only the presenter can
  confirm, such as what will be said aloud, an organizer's requirement, or
  what students showed in an earlier session.
- **Decline:** an optional refinement. Record it without changing anything.

Apply these rules:

- A contest needs evidence the reviewer could have read. "That was
  intentional" is not evidence.
- Do not contest a comprehension gap. If the reviewer had what participants
  will have and could not follow it, propose a fix. If the packet lacked
  something participants will have, such as narration, escalate it and
  propose a repeat review with the missing material.
- Add context for the audience, not for the reviewer. If only a reviewer
  without the audience's background needs an explanation, escalate instead
  of adding it.
- Findings marked "may be covered by narration" are escalated.
- Do not change a finding's importance. To disagree, contest it and give
  the reason.
- You helped write this material. Wanting to defend it is not evidence that
  the reviewer is wrong.

Use this layout:

```markdown
# Review report: [title], [version]

Reviews run: [list, each marked fresh or internal critique]
Narration included: [yes / no / partly]
Summary: [n] essential, [n] meaningful, [n] optional; [n] escalated

## Needs your knowledge (escalated)
[findings listed first]

## Findings

### [ID] [short title]
- Reviewer: [role]
- Location: [slide, segment, task, or minute]
- Issue:
- Likely consequence:
- Supporting reason:
- Reviewer's proposed change:
- Importance: Essential correction | Meaningful improvement | Optional refinement
- Proposed response: Fix | Contest | Escalate | Decline
- Justification:
- Exact change (for Fix):
- Decision: [left blank for the presenter]
- Reason:
```

## Step 9: The presenter decides

In chat, give the counts and list the escalated findings first. Then ask one
question about how to proceed:

- Go through the essential findings one at a time
- Accept all proposed responses, then raise objections
- Edit the decisions directly in `review_report.md`

For each finding, the presenter accepts the proposed response, chooses a
different one, or changes the fix. Record the decision and the reason.

## Step 10: Apply and record

1. Make accepted changes in the actual artifacts: brief, plan, notes,
   student materials. A conversational explanation does not fix anything.
2. If you cannot edit the deck file, write a slide-by-slide change list
   (slide, current content, change) and ask the presenter to confirm when it
   has been applied.
3. Append the round to `review_record.md`:

```markdown
## [version], [date]
Reviews: [role: fresh | internal critique | human (name)]
Findings: [n] fixed, [n] contested, [n] escalated, [n] declined
Decisions:
| ID | Decision | Reason |
Changes made: [files and slides]
Human reviewers and the version each has seen:
| Person | Role | Versions seen | Still fresh for comprehension? |
```

## Step 11: Recheck and stop

- After substantial changes, rerun the affected reviews with new fresh
  reviewers. A recheck packet may include the specific earlier finding, so
  the reviewer can confirm whether it was resolved.
- Rerun the big-picture review after a round of substantial revisions.
- Stop when essential corrections are resolved, important trade-offs are
  explicit, and the relevant rehearsal has passed. Reviewers do not need to
  agree on every stylistic choice.
- Before delivery, suggest a human review using `human_reviewers.md`. AI
  reviewers know more than most audiences, so a person who resembles the
  audience gives the best evidence before the real one.
