# Talking with Elephants & Goldfish

A talk succeeds or fails on what the audience understands, not on what the
presenter meant. But it's hard to judge your own talk: you know what each
slide is supposed to mean, so the gaps that will lose a listener are
invisible to you.

Every audience has two kinds of listeners. **Elephants** have the context
and are paying close attention: they remember what you said ten minutes ago
and follow the thread. **Goldfish** know less, or zoned out for a minute and
are trying to catch up: they have only what's on the screen and what you're
saying right now.

*Talking with Elephants & Goldfish* adapts Google's Elephant–Goldfish model
for software design to presentations and teaching, and uses AI to play
both. An Elephant collaborator holds everything you know about the talk. It
interviews you about your goal and audience, takes stock of any existing
deck, and builds a timed plan with you. Goldfish reviewers check the talk in
fresh contexts, seeing only what the audience sees and hears. They test
whether the message comes through, whether the evidence holds up, and
whether the slides work in the room. You decide every change.

It covers professional talks, judged competitions, and college lectures,
from a blank page or an existing deck. It works in Claude Code, Codex, or
any chat window.

> A good talk works for the Elephant who has followed every word and for the
> Goldfish who just looked up from their phone.

The organizing principle: **develop with full context, review through fresh
eyes, and improve using evidence from the people you address.**

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
