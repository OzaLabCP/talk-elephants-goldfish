# Talking with Elephants & Goldfish

A model for preparing, reviewing, delivering, and improving professional
talks and educational lectures: **develop with full context, review through
fresh eyes, and improve using evidence from the people you address.**

- `talking-with-elephants-and-goldfish.md`: the full model
- `starting_prompts.md`: prompts to paste into any AI chat
- `skills/`: agent skills that carry out the model step by step

## Skills

Use them in this order. Each can also be used on its own.

| Skill | What it does | Writes |
| - | - | - |
| `teg-inventory` (Part A) | For an existing deck: describes each section and reconstructs what the original was for | `inventory.md` |
| `teg-intake` | Interviews you, one question at a time, about your goal, audience, and constraints | `brief.md` |
| `teg-inventory` (Part B) | Recommends keep, reframe, replace, remove, or move for each section, against the new brief | `inventory.md` |
| `teg-plan` | Builds the timed experience plan, one section at a time, with your approval | `experience_plan.md` |
| `teg-review` | Runs fresh-context reviews (big picture first), proposes a response to each finding, and records your decisions | `reviews/`, `review_record.md` |

Starting from a topic or notes rather than a deck? Begin with `teg-intake`
and skip the inventory.

The skills use the `SKILL.md` format that Claude Code, Codex, and other
agent tools read. To use one in a plain chat window, paste in its
`SKILL.md` and any files it refers to. Fresh reviews need a separate
context; `skills/teg-review/harnesses.md` explains how in each tool,
including a manual mode for chat windows.

## Credit

Adapted from Dave Rensin's Elephant–Goldfish Model and Google's
[elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)
project (Apache-2.0). The workflow structure and the fix, contest, escalate,
and decline rules for review findings follow that project. The text here is
written for talks and lectures.
