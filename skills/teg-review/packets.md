# Review packets

Each reviewer receives what the people it stands in for would have, and
nothing that would let it skip the work those people must do.

Every reviewer also reads `reviewers/common.md` and its own reviewer file.
Those files are instructions, not packet materials.

## What each reviewer receives

| Reviewer | Receives | Kept out |
| - | - | - |
| **Big picture** | Brief; a short outline of the plan (segments, minutes, one-line purpose each); when adapting, the inventory of the existing material | Slide-level detail, the preparation conversation, earlier findings |
| **Design** | Brief, experience plan, constraints, referenced evidence; for lectures, objectives and the list of tasks | The preparation conversation and undocumented explanations |
| **Comprehension** | A description of the participants' background; exactly what participants encounter: rendered slides, narration (for a live talk), handouts, and any objectives or agenda they are shown | The brief, the outcome statement, private notes and rationale, answer keys, slides that will not be shown |
| **Comprehension, phase 2** | The comprehension packet, the phase 1 reconstruction, and the intended message | The rest of the brief and the preparation conversation |
| **Evidence** | Claims as presented (slides plus narration or script), sources, data, stated qualifications, the brief's evidence section | Explanations offered only in conversation |
| **Rejoining** | The comprehension packet with the missed stretch removed: the opening section, then everything from the rejoin point onward (slides and narration) | The missed stretch, the brief, private notes, and anything else kept out of comprehension |
| **Misconceptions** | The comprehension packet, plus the objectives | Instructor notes, answer keys, rationale |
| **Assessment, phase 1** | Student tasks exactly as students receive them, the students' background, the conditions (time, permitted resources), and the rubric only if students see it | Answer key, instructor notes, a rubric students do not see |
| **Assessment, phase 2** | Tasks, the phase 1 attempt, answer key, rubric, objectives | The preparation conversation |
| **Delivery** | Rendered slides at their real size, the timing plan, a rehearsal recording or timestamped transcript, the setting (room, screen, remote or hybrid); for lectures, activity instructions and class conditions | Claims that the outline proves readability or pacing |
| **Judge** | What judges see and hear (as for comprehension), the rubric and rules, the panel's background | The brief, rationale, and anything about other entries |

## Describing the participants' background

Comprehension, misconception, assessment, and judge packets need a short
description of who the participants are. Write it as what they know, not
what the presenter wants:

> The participants are [role and number]. They know [specific concepts,
> methods, vocabulary]. They do not know [specific concepts]. They are
> [specialists in the subfield / experts in an adjacent area / informed
> non-experts / novices]. They are there to [learn / judge / decide / stay
> informed].

Do not include phrases such as "the goal is," "they should come away
with," or "the key point is."

## Preparing a deck

- Give reviewers what is visible as a PDF or images, so they see layout,
  charts, and type size. A text export alone hides most visual problems.
- Put narration in a separate file, labeled with its source: rehearsal
  transcript, script, or speaker notes the presenter confirmed are spoken.
- Remove hidden slides, backup slides that will not be presented, comments,
  and revision history.
- If you can only extract text, say so in the manifest. Visual and delivery
  findings are then limited, and the delivery review should wait for a
  rendered version.

## Leak checklist

Check every comprehension, learner, assessment phase 1, and judge packet
for:

- Speaker notes that state the intent or rationale
- File or folder names that state the conclusion (rename them neutrally,
  for example `deck_v3.pdf`)
- Document titles, metadata, or slide comments
- Hidden slides or backup slides that will not be shown
- Instructor notes inside student handouts
- Answer keys stored in the same file as the tasks
- The brief, or any part of it, pasted into the manifest
- Earlier review findings

## Recheck packets

When a finding has been fixed, a recheck packet may include that finding
and the revised material, so the reviewer can confirm whether it is
resolved. Use a new reviewer for any recheck that depends on freshness, such
as comprehension.

## Manifest

Each packet folder has a `manifest.md`:

```markdown
# Packet: [reviewer], [version]

Files:
- [file]: [what it is]

Participants' background: [description as above, or "not applicable"]
Narration: [included (source) / not included: mark findings narration might resolve]
Format: [live talk / recorded / circulated without the presenter / class session]
Length: [speaking minutes] + [Q&A or activity minutes]
Review in sections: [yes, in this order: ... / no]
Rejoins at: [location, and roughly how many minutes were missed / not applicable]
Recheck of: [finding IDs, or "none"]
```
