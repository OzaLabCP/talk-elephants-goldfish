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

## Quick start (about 5 minutes)

**1. Install it once.** In a terminal:

```bash
claude plugin marketplace add OzaLabCP/talk-elephants-goldfish
```

```bash
claude plugin install teg@teg
```

Inside Claude Code 2.1.275 or later, one command does both:
`/plugin install teg --marketplace OzaLabCP/talk-elephants-goldfish`.

To take stock of an existing PowerPoint deck, the package uses Python 3
with `python-pptx` (`pip install python-pptx`). LibreOffice is optional; it
lets the package render slide images so reviewers can see layout.

**2. Make a folder for the talk.** Put any existing material in it: a deck,
notes, an outline. The package writes its files there (`brief.md`,
`experience_plan.md`, `progress.md`, and so on).

**3. Start Claude Code in that folder and send a first message,** for
example:

```text
/teg:teg-start I'm adapting my 20-minute conference talk, talk.pptx, for a campus research showcase: 8 minutes, faculty and staff from every college.
```

Saying what you have and who it's for saves a question. `/teg:teg-start` on
its own works too.

**4. Expect a first response like this:**

> You're at the start, with an existing deck to adapt. First I'll take stock
> of `talk.pptx`: what each section does and what the original talk was
> for. Then I'll interview you about the new audience. I've saved your
> place in `progress.md`.
>
> **Stage A · Understand → Take stock** (not started). After this: Brief.
>
> | Stage | Steps |
> | - | - |
> | A. Understand | ▶ Take stock · Brief |
> | B. Design | Adapt · Plan · Review the plan |
> | C. Build | Build and rehearse · Review the materials |
> | D. Deliver and learn | Deliver and debrief |
>
> You can stop after any step and pick up later.
>
> Start taking stock of `talk.pptx` now?

Reply "yes" and it begins. Every step ends by naming the next one, and you
can say "status" at any time to see the map.

**Codex:** install with these two commands, then start a new session in
the talk folder and send `Use the teg-start skill.` followed by what you
have and who it's for.

```bash
codex plugin marketplace add OzaLabCP/talk-elephants-goldfish
```

```bash
codex plugin add teg@teg
```

**Any other tool or chat window:** paste in the contents of
`skills/teg-start/SKILL.md`, then your first message. Paste each step's
`SKILL.md` as you reach it.

Install the whole package, not single skills: the skills refer to each
other's files.

## How it works: four stages

Start with **`teg-start`**. It shows this map, works out where you are, and
hands you to the right step. Every step ends by telling you what comes next,
and `progress.md` in your folder keeps your place between sessions.

| Stage | Step | Skill | Produces |
| - | - | - | - |
| **A. Understand** | Take stock (existing deck only) | `teg-inventory` Part A | `inventory.md` |
| | Brief | `teg-intake` | `brief.md` |
| **B. Design** | Adapt (existing deck only) | `teg-inventory` Part B | `inventory.md` |
| | Plan | `teg-plan` | `experience_plan.md` |
| | Review the plan | `teg-review` | `reviews/` |
| **C. Build** | Build and rehearse | you build; `teg-drift` checks it against the plan | slides, notes, drift report |
| | Review the materials | `teg-review` | `reviews/`, `review_record.md` |
| **D. Deliver and learn** | Deliver and debrief | `teg-debrief` | `debrief.md`, updated brief |

You can stop after any step, skip steps, or go back. The package does not
generate slides: it helps you decide what the talk should do, plans it,
checks it, and helps you learn from it. You build the slides in your own
tool.

**How decisions work.** Anything you have to decide appears in chat,
complete enough to decide from, so you never need to open a file to make a
decision. Files hold the reasoning and the record. When there are many items
to decide, you get one table with a proposal for each, and you reply with
only the ones you'd change.

The skills use the `SKILL.md` format that Claude Code, Codex, and other
agent tools read. To use one in a plain chat window, paste in its
`SKILL.md` and any files it refers to. Fresh reviews need a separate
context; `skills/teg-review/harnesses.md` explains how in each tool,
including a manual mode for chat windows.

## Credit

Adapted from Dave Rensin's Elephant–Goldfish Model
([original essay](https://medium.com/@drensin/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874))
and Google's
[elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)
project (Apache-2.0). The workflow structure and the fix, contest, escalate,
and decline rules for review findings follow that project. The text here is
written for talks and lectures.

## License

Apache License 2.0. See [LICENSE](LICENSE).
