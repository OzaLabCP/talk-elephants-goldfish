# Starting fresh reviewers

A fresh reviewer needs:

- A new context with none of the preparation conversation
- Only its packet, its reviewer file, and `reviewers/common.md`
- No project instruction file that contains the talk's private intent

Some tools load project instruction files (such as `CLAUDE.md` or
`AGENTS.md`) into every subagent. Keep the talk's purpose and rationale out
of those files, or the reviewer starts with the answer.

Reviewers with file access can usually see the whole working folder.
`common.md` tells them to read only their packet, but this cannot be fully
enforced. Keep `brief.md` and notes outside the packet folders, and ask each
reviewer to report anything it opened outside its packet.

## By tool

| Tool | How to start a fresh reviewer |
| - | - |
| Claude Code | Use the `Agent` tool with a general-purpose subagent. Send several `Agent` calls in one message to run reviewers in parallel. |
| Codex | Use the subagent tool (`spawn_agent`). Set `fork_context: false`, or `fork_turns: "none"` if that is the option offered, so the reviewer does not inherit the conversation. |
| Antigravity | Use `invoke_subagent`. |
| Other tools | Use any feature that starts an agent with an empty conversation. If you are not sure the context is empty, use manual mode. |

Pass the prompt from `SKILL.md` Step 6 exactly, with absolute paths. Do not
add a summary of the talk, the conversation, or your own views.

## Manual mode

Use this when your tool cannot start a fresh context, such as a plain chat
window.

1. For each reviewer, write `reviews/<version>/manual/<reviewer>_prompt.md`.
   It contains `common.md`, the reviewer file, and the packet manifest,
   followed by the packet's text content. List any files that must be
   attached instead, such as the slide PDF.
2. Tell the presenter to open a **new conversation** for each reviewer,
   outside any project or workspace that holds the talk's materials, with
   chat memory turned off if the app has it. Paste the prompt, attach the
   listed files, and paste the reviewer's reply back here.
3. Save each reply to `reviews/<version>/findings/<reviewer>.md` and
   continue from Step 7.

Manual mode is a genuine fresh review if the new conversation has no memory
of the work.

## When neither is possible

Run the review yourself and label every result **internal critique** in
the report and the review record. An internal critique can still find
problems, but it cannot show what a fresh reader would miss.
