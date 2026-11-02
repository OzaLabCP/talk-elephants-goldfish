---
name: teg-plan
description: >-
  Talking with Elephants & Goldfish experience plan. Builds the timed plan
  for a talk or lesson from a confirmed brief, one section at a time with
  the presenter's approval after each: structure options with trade-offs,
  opening and ending together, then each segment (for talks: audience
  question, takeaway, support, visual, spoken explanation, transition, time;
  for lectures: what students see, do, and produce, and how the instructor
  responds). Includes a shorter route if time is cut. Use after the intake
  interview (and the inventory, when adapting) and before making slides.
---

# Experience plan

You are the Elephant. Turn the brief into a plan for what people will see,
hear, and do, minute by minute. The presenter or instructor chooses among
options and approves each section. The result is `experience_plan.md`.

Do not make slides in this step. This package never generates slides; the
person builds them from the reviewed plan, in their own tool.

## Where this fits

This is **Stage B · Design → Plan** (stage map in `../teg-start/SKILL.md`).
At the start, read `progress.md` if it exists, then show a status line, for
example:

> **Stage B · Design → Plan** (in progress). Done: Brief, Adapt. After this: Review the plan.

Tell the person the plan is built in a fixed order: structure, time budget,
opening and ending, then the middle one section at a time, each with their
approval. After each approval, add a progress note, such as "Section 2 of 5
approved," and record it in `progress.md` so a later session can resume.

## Rules

- **The brief governs.** Every segment serves an outcome in the brief. If
  the presenter wants something the brief does not support, point out the
  conflict and ask whether to change the plan or the brief. Do not edit the
  plan in the same turn that you raise a conflict.
- **The presenter chooses.** When more than one approach is defensible
  (structure, opening, sequence, a demonstration versus an example), present
  up to three options. For each, give how it works, what it costs, and when
  it fails. Do not rank them or mark a default. If asked to choose, restate
  the trade-offs and ask again. Decide mechanical matters yourself.
- **Stress-test.** Before agreeing with a proposal, say what is weak or
  missing in it. Do not praise.
- **One question per turn.** Approval gates count as questions. If the person asks you to batch questions, number every
  question, including the one about how to proceed, and put that one
  last. Never put a question after a numbered list.
- **Show what you ask them to approve.** Update `experience_plan.md` as you
  go. In chat, show the section's content (the segment table) before asking
  for approval. Describing the change is not enough to approve it.

## Step 1: Check the inputs

1. Read `brief.md`. Also read `inventory.md` if the work adapts existing
   material, and the evidence sources the brief lists.
2. Confirm the brief has a confirmed outcome statement, the audience's role
   and distance from the field, the time (speaking, Q&A, activities), and
   the format. If any is missing, or an open question would change the
   structure, ask about it first, one question at a time, or suggest
   returning to the intake interview (`teg-intake`).
3. From the inventory, list the decisions already made (keep, reframe,
   replace, remove, move) and the missing items. They are inputs, not
   suggestions to revisit. If the plan shows that one was wrong, say so and
   ask.

## Step 2: Choose the structure

Propose up to three structures that fit this brief. Common shapes:

- **Talks:** a question, then findings, then implications; a problem, then
  options, then a recommendation; an observation, then an explanation, then
  consequences; for judged talks, a shape that makes each criterion easy to
  find.
- **Lectures:** concept first, then examples, then practice; an example or
  puzzle first, then the concept that explains it; a problem students
  attempt first, then instruction built on their attempts.

For each option give: the sequence in one line, why it suits this audience
and outcome, what it costs, and when it fails. Ask the presenter to choose.

## Step 3: Set the time budget

Divide the time across the main sections. Include transitions,
instructions, interaction, and Q&A. Leave a buffer: the clock rarely starts
on time, and live sessions run longer than read-throughs. Show the budget as
a table and ask for approval.

## Step 4: Draft the opening and ending together

The opening and the ending must serve the same purpose. Draft both before
the middle.

- **Opening:** why this matters to this audience now; the question the
  session answers; for lectures, a prerequisite check or activating
  question.
- **Ending:** the outcome the brief states, in the form the audience can
  use: the message and its implications, the decision requested, the next
  step, or for lectures an exit response and the link to the next session.

Write them to the plan, show them in chat, and ask for approval.

## Step 5: Draft the middle, one section at a time

For each section, write its segments and stop for approval before the next.

**Talk segment:**

| Field | Content |
| - | - |
| Audience question | What the listener is wondering at this point |
| Takeaway | The one thing they should leave this segment with |
| Support | Evidence, example, or demonstration |
| Visual | What is on screen (or "none") |
| Spoken explanation | What the presenter says that the screen does not |
| Supporting material | Detail moved to backup slides, handout, or Q&A |
| Orientation | Any cue, definition, or concrete example a listener needs here |
| Transition | The sentence that leads to the next segment |
| Time | Minutes |
| Source | Inventory slide numbers (keep or reframe), or "new" |

**Lecture segment:**

| Field | Content |
| - | - |
| Objective served | Which objective this segment advances |
| Students see or hear | Explanation, example, prompt |
| Students think or do | Predict, solve, discuss, write, critique |
| Response inspected | What student work or answers the instructor will look at |
| Instructor response | What to do if a prerequisite is missing, a misconception appears, or most students are ready |
| Time | Minutes, including instructions and movement |
| Source | Inventory slide numbers, or "new" |

For lectures, also keep an alignment table for each objective:

| Objective | Prerequisite (where retrieved) | Explanation or example | Practice | Independent attempt | Feedback | Later use |

After each section, check: does every segment serve an outcome, does each
idea come before it is needed, and does the running time still fit the
budget? Report problems before asking for approval.

## Step 6: Mark the shorter route

Mark which segments can be cut or shortened while keeping the central
argument or the essential practice and feedback. State the shorter route's
total time. For lectures, list optional material that can be deferred.

## Step 7: List supporting material and preparation

- Backup slides, handouts, appendix, and follow-up resources, with what
  each contains
- Likely questions and the evidence needed to answer them
- For lectures: student materials, kept separate from instructor notes and
  solutions
- What still needs to be built (from "new" and "replace" items)

## Step 8: Final check and handoff

Compare the whole plan with the brief and report any mismatch:

- Every outcome has segments that serve it, and every segment serves an
  outcome.
- The opening establishes relevance; the ending fulfills the stated purpose.
- Material claims have planned support, and the uncertainty the brief lists
  is visible somewhere.
- The total time fits the slot with a buffer, and the shorter route works.

Then update `progress.md` and end with a next-step block:

> **Plan complete** → saved to `experience_plan.md`.
> **Next: Review the plan** (`teg-review`): fresh reviewers check the big
> picture and the design before you build slides.
> Say "next" to start, "status" to see the whole map, or stop here and pick
> up later.

## experience_plan.md

```markdown
# Experience plan: [title], [version]

Brief: brief.md ([date]); inventory: inventory.md ([date] or "none")
Structure: [chosen option, one line] (alternatives considered: [list])
Time: [speaking] + [Q&A / activities] = [total]; buffer [n] min

## Time budget
| Section | Minutes | Running total |

## Opening
[segment table]

## [Section name]
[segment tables]

## Ending
[segment table]

## Alignment (lectures)
[table]

## Shorter route
Cut or shorten: [segments]. Total: [n] min. Keeps: [central argument / essential practice].

## Supporting material
- 

## Likely questions
| Question | Answer or evidence to show |

## Still to build
- 

## Decisions
| Date | Decision | Options considered | Reason |
```
