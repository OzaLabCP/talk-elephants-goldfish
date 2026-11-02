---
name: teg-review
description: >-
  Talking with Elephants & Goldfish review. Runs fresh-context reviews of a
  talk or lesson: a big-picture review first, then design, comprehension,
  rejoining, evidence, and delivery reviews, plus misconception and assessment reviews
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

## Where this fits

This skill runs at two points (stage map in `../teg-start/SKILL.md`):

- **Stage B · Design → Review the plan**, when there is a plan but no
  materials yet
- **Stage C · Build → Review the materials**, when slides, notes, or student
  materials exist

At the start, read `progress.md` if it exists, then show a status line, for
example:

> **Stage C · Build → Review the materials** (in progress). Done: Build and rehearse. After this: Deliver and debrief.

While reviewers run, say which have finished, such as "Big picture done; 3
of 4 detailed reviews done."

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
4. **One question per turn** when you need the presenter's input. If the
   presenter asks you to batch questions, number every question, including
   the one about how to proceed, and put that one last. Never put a
   question after a numbered list.
5. **Decisions in chat, reasoning in files.** Packets, full reports, and the
   review record go in files. Everything the presenter must decide appears
   in chat as a table they can act on without opening a file. Give file
   paths only for detail they may want.

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
| Live talk or class longer than about 10 minutes | Add one or two rejoining reviews (below) |

**Rejoining reviews** stand in for the listener who zoned out and just
looked up. Each one hears the opening, misses a stretch, and rejoins
partway through. Choose one or two rejoin points where losing the thread
would cost the most: usually the start of the results or main argument, and
the section after the densest explanation. Each rejoin point needs its own
fresh reviewer. Skip this review for a deck that circulates without the
presenter: a reader can turn back.

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
- **Rejoining reviews** can run in parallel with the others, one fresh
  reviewer per rejoin point.

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
  what students showed in an earlier session; or it is a comprehension
  finding you doubt, which a recheck could settle (see the rules below).
- **Decline:** an optional refinement. Record it without changing anything.

Apply these rules:

- A contest needs evidence the reviewer could have read. "That was
  intentional" is not evidence.
- Investigate a comprehension gap before dismissing it. A reported gap is
  a signal, not proof: the reviewer may have misread, or may lack knowledge
  this audience has. Do not contest it on your own reading or on the
  presenter's confidence alone. If you doubt it, escalate it and propose a
  check that can settle it: an independent recheck by a new fresh reviewer
  (see "Recheck packets" in `packets.md`), or feedback from a person who
  resembles the audience (`human_reviewers.md`). Contest it only with that
  evidence. If the recheck also finds the gap, propose a fix.
- If the packet lacked something participants will have, such as
  narration, escalate the finding and propose a repeat review with the
  missing material.
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

Put everything to be decided in one chat message, in this order:

1. **A one-line summary:** the number of findings by importance, and how
   many need the presenter's answer.
2. **A decision table,** one row per finding, essential findings first: ID,
   location, the proposed change in one line, importance, proposed response.
   For an escalated finding, the response column says "see Q1," "see Q2,"
   and so on. If there are more than about 25 rows, show the essential and
   escalated findings in full and group the rest by section, one line each.
3. **Numbered questions:** first the escalated questions, each naming its
   finding and answerable in a word or a line; then, last, "Reply with the
   IDs you'd change or reject; everything else is accepted."
4. **An example reply,** in italics, using this message's own numbers,
   plus the shortcut "all good" to accept everything.

All the questions sit together at the end, just above where the presenter
types, so one short reply answers them all. Offer going through findings
one at a time only if the presenter asks for it.

For example:

> **Review of v2: 6 findings.** 2 essential, 3 meaningful, 1 optional. 2 need your answer.
>
> | ID | Where | Proposed change | Importance | Response |
> | - | - | - | - | - |
> | F1 | Slide 5 | Replace "works for all California vineyards" with "worked at our site; the trial tests whether it holds elsewhere" | Essential | Fix |
> | F2 | Slide 4 | Add error bars and say the yield numbers aloud | Essential | Fix |
> | F3 | Slide 3 | Define VWC and MAD in plain words | Meaningful | see Q1 |
> | F4 | Slide 6 | Name the partner roles you need | Meaningful | Fix |
> | F6 | Slide 4 | "Conventional" means calendar watering | Meaningful | see Q2 |
> | F5 | Slide 2 | Connect 600,000 acres to the 18% | Optional | Decline |
>
> 1. F3: Will you define VWC and MAD out loud, or should the slide do it?
> 2. F6: Do you say "calendar watering" when this slide is up?
> 3. Reply with the IDs you'd change or reject; everything else is accepted.
>
> *Example reply: "1 out loud · 2 no · 3 reject F5." Or "all good" to accept everything.*

For each ID the presenter names, ask what they want instead if it is not
clear: a different response or a different fix. Record every decision and
its reason in `review_report.md`. For findings nobody named, the reason is
"accepted as proposed."

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

When the round is finished, update `progress.md` and end with the
next-step block that applies:

> **Review the plan complete** → `reviews/[version]/review_report.md`.
> **Next: Build and rehearse**: make the slides and notes from the plan,
> then rehearse aloud.
> Say "next" to start, "status" to see the whole map, or stop here and pick
> up later.

> **Review the materials complete** → `reviews/[version]/review_report.md`.
> **Next: Deliver and debrief**, after a human review if there is time.
> Say "next" to start, "status" to see the whole map, or stop here and pick
> up later.
