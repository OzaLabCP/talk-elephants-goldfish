**Talking with Elephants & Goldfish** is a model for preparing, reviewing, delivering, and improving professional talks and educational lectures. It can begin with a broad topic, scattered notes, an outline, or a finished slide deck.

Its organizing principle is: **develop with full context, review through fresh eyes, and improve using evidence from the people you address.**

The Elephant maintains the purpose, background, evidence, and reasoning behind the presentation. Goldfish reviewers examine deliberately limited materials without the preparation conversation. The presenter or instructor makes the judgments and remains responsible for the content.

The two animals also describe a real audience. **Elephants** have the context and are paying close attention: they remember what was said ten minutes ago and follow the thread. **Goldfish** know less, or stopped listening for a minute and are trying to catch up: they have only what is on the screen and what is being said now. A good talk works for both. The model uses an Elephant collaborator and Goldfish reviewers to test it for both.

This is an adaptation of Dave Rensin’s [Elephant–Goldfish Model](https://drensin.medium.com/elephants-goldfish-and-the-new-golden-age-of-software-engineering-c33641a48874). The original model uses a context-rich design process and fresh reviews to expose missing assumptions before implementation. [Google’s explanation](https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html) and the [project repository](https://github.com/google/elephant-goldfish-model) describe its software workflow. The talk and lecture workflows below extend that approach.

| Design question | Professional talks | Educational lectures |
| - | - | - |
| Intended result | An audience understands an argument, weighs its implications, or takes a relevant next step. | Students demonstrate specified knowledge or skills. |
| Main design unit | A claim connected to evidence and audience relevance. | A learning objective connected to practice and assessment. |
| Experience to prepare | Slides, narration, examples, demonstrations, discussion, and Q&A. | Explanations, examples, student work, feedback, and follow-up practice. |
| Evidence after delivery | What listeners understood, asked, decided, or did. | What students can explain, interpret, solve, or produce. |

The two versions can be combined for professional training, workshops, and research seminars. Specify both the communication outcome and the learning outcome when both matter.

# The shared preparation cycle

**Orient → define outcomes → design the experience → review → produce and rehearse → deliver → update.**

In practice, the cycle runs in four stages. Each step ends by naming the next one, and a short progress record keeps the place between sessions.

| Stage | Steps | Working artifacts |
| - | - | - |
| **A. Understand** | Take stock of existing material (when reusing); write the brief | Inventory, brief |
| **B. Design** | Adapt existing material (when reusing); plan the experience; review the plan | Inventory decisions, experience plan, review record |
| **C. Build** | Build the materials; check for drift; rehearse; review the materials | Delivery package, review record |
| **D. Deliver and learn** | Deliver; debrief against the brief and the reviews | Debrief, updated brief |

## Establish the roles

**The presenter or instructor** supplies judgment: which outcomes matter, what the evidence warrants, what to omit, and what trade-offs are acceptable.

**The Elephant** is the ongoing design collaborator. It asks consequential questions, proposes structures, challenges assumptions, and maintains a written brief. Its usable memory lives in that brief, source references, and decision record, so the work can continue in a new session.

**Goldfish reviewers** provide independent readings of a specified version. Freshness means they have not participated in the preparation conversation. Each receives the background necessary for its assigned role.

**Actual listeners and students** provide evidence about the experience. Their responses help distinguish problems predicted during preparation from problems that occur in practice.

## Define the result before polishing the materials

Write the desired outcome and how you will recognize it. Identify the audience’s starting knowledge and the constraints of the occasion. Label important unknowns and decide which require clarification.

Use outlines, rough diagrams, sample questions, and existing slides to develop the structure. Begin visual polish once the outcomes and sequence are stable enough to guide it.

## Describe the audience by role and distance

Two facts about the audience shape a talk more than any others.

**What they are there to do.** Audiences come to learn (students, trainees), to evaluate the presenter (competition judges, a thesis committee, a hiring or grant panel), to decide (a leadership briefing, a funding meeting), or to stay informed (a research talk without judges, a colloquium, a public lecture). The role sets the outcome and the evidence of success. When a session serves several roles, record which one defines success.

**How close they are to the field.** Specialists need little background and expect precise methods and limitations. Adjacent experts need to know why the problem matters, with key concepts translated. Informed non-experts need the question, the finding, how confident to be, and what it means, without unexplained terms. Novices need all of that built from familiar ideas. Do not infer distance from the venue: a competition panel may be mixed, and a “general audience” may mean educated non-experts or the public.

When an audience evaluates the presenter, its criteria are information that audience has. Give the rubric to reviewers who stand in for the judges. This is the reverse of a lecture, where students do not have the answer key and learner reviews should not have it either.

## Maintain four working artifacts

1. **Brief:** audience, purpose, outcomes, constraints, success criteria, and assumptions.

2. **Experience plan:** the sequence, what people see and hear, what they do, and the time allocated.

3. **Evidence and review record:** sources, qualifications, consequential findings, the response to each finding, drift checks, and which reviewers have seen which version.

4. **Delivery package:** slides or other materials, speaking or teaching notes, activities where needed, and follow-up resources.

These can be sections of one document. After delivery, add a short account of what happened and what should change.

## Review the big picture first

Before detailed reviews, ask a fresh reviewer whether this is the right talk or lesson for this audience, purpose, and occasion. The reviewer considers whether the outcome justifies the time, whether the scope fits the slot, whether the structure leads to the intended ending, and whether anything essential is missing or unnecessary.

When adapting existing material, the big-picture review asks whether the original answers the new audience’s question. A deck can be accurate and clear and still be built for someone else.

Repeat the big-picture review after a round of substantial revisions. Detailed corrections can each be reasonable while the whole drifts away from its purpose.

## Separate the review materials

| Review | Give the reviewer | Keep out of this review |
| - | - | - |
| Big-picture review | Brief, a short outline of the experience plan, and, when adapting, the inventory of the existing material. | Slide-level detail and the preparation conversation. |
| Design review | Brief, experience plan, constraints, and referenced evidence. | Preparation conversation and undocumented explanations. |
| Audience or learner comprehension | Expected prior knowledge and exactly what participants encounter. | Private rationale, additional answer cues, and background unavailable to participants. |
| Rejoining listener | The opening, then what participants encounter from a chosen point onward, with the stretch before it removed. | The missed stretch, private rationale, and background unavailable to participants. |
| Accuracy and evidence | Claims, examples, sources, data, and qualifications. | Unsupported explanations offered only in conversation. |
| Delivery review | Rendered materials and a timed rehearsal, recording, or observation. | Assumptions that the written outline proves readability or pacing. |
| Judge | What judges see and hear, the rubric and rules, and the panel’s background. | The brief, private rationale, and information about other entries. |

For comprehension, ask the reviewer to reconstruct the message before revealing the private statement of intent. Preserve any objectives or summaries that participants actually receive. For assessment review, obtain an independent attempt before revealing the answer key, then check the key and rubric.

A live talk is reviewed with its spoken explanation. A deck or recording distributed independently needs a separate review of that experience. For long or complex sequences, review sections in presentation order so later explanations do not conceal earlier confusion.

For a live talk or class longer than about ten minutes, add a rejoining review. A fresh reviewer hears the opening, misses a stretch, and rejoins partway through, as a listener does after looking at a phone. Choose rejoin points where losing the thread would cost the most, such as the start of the results. The review shows whether section titles, recaps, and restated questions let a listener back in.

Use a separate review context; asking the authoring conversation to forget its history does not create an independent review. When separation is unavailable, label the result an internal critique.

An AI reviewer can use knowledge that the audience lacks, even when asked to act as a novice. Treat its findings as possible problems to investigate. Human rehearsal and participant responses provide the evidence needed to judge the actual experience.

## Plan human reviewers

A fresh AI review can be repeated as often as needed. A person’s freshness is used up: someone who has read or heard one version cannot give a fresh comprehension reading of the next. Plan who sees what, and when.

- **Keep at least one representative person unexposed** until the full rehearsal, so the final version receives a genuine first hearing.

- **Use people who have already seen the material** for reviews that do not depend on freshness: accuracy, evidence, timing, and whether a revision resolved the problem they reported.

- **Choose reviewers who resemble the audience** in background and role. A colleague is a poor stand-in for students or non-specialists.

- **Record who has seen which version** in the review record.

# Starting from existing material and adapting it

| Starting material | First useful output |
| - | - |
| Topic or general scope | A brief that identifies the audience, purpose, outcome, and boundaries. |
| Notes and research | A map of ideas, evidence, uncertainties, and missing material. |
| Outline | A check of the sequence against the desired outcomes and prerequisites. |
| Existing deck | An inventory of each section’s purpose, claim or objective, evidence, and dependence on narration. |
| Previous recording or feedback | An account of observed strengths and difficulties, linked to specific moments. |

With an existing deck, inspect the visible slides as well as notes and embedded charts. Record inferred original intent as an inference. A missing explanation may have been spoken; establish that before deciding the material is defective.

For each section or slide, assign an action: **keep, reframe, replace, remove, or move to supporting material**. Give a reason connected to the current brief.

When the audience, purpose, course level, duration, or delivery format changes:

1. Record the changes in the brief.

2. Reconsider the outcome and the knowledge people can reasonably bring.

3. Check the implications for evidence, vocabulary, examples, sequence, activities, and the ending.

4. Decide what can carry forward and what needs rebuilding.

5. Repeat the reviews affected by those changes.

A shorter slot requires a smaller scope and revised timing. A different audience may need a different opening or explanation even when the central evidence stays the same. Moving a live presentation into an independent reading format requires making essential spoken context available.

Keep a shared collection of reliable sources and reusable material, with a distinct brief for each audience or class. Preserve the original version so later adaptations remain traceable.

## Check for drift

A deck that is reused and revised gradually separates from its brief. Slides added for one audience remain for the next, qualifications disappear during tightening, sources age, and the ending shifts purpose. Run a drift check before each reuse, after substantial revisions, and whenever the brief or the underlying evidence changes.

Use a fresh reviewer for the comparison when possible: whoever built the materials tends to see what was meant rather than what is there. Compare the current materials with the current brief:

- Does each section still serve an outcome in the brief?

- Has any claim become stronger than its evidence, or lost a qualification?

- Are sources, data, and examples still current?

- Do the opening and ending still match the stated purpose?

- Does material remain from an earlier audience or occasion?

- Does the timing still fit the slot?

Check in the other direction as well: decisions recorded in the brief that the materials never carried out. Report drift in the usual finding format and resolve it like any other finding.

# Professional talks

The professional workflow supports research talks, conference presentations, proposals, briefings, pitches, and internal updates. Its central question is: **What should this audience understand, and what should that understanding enable?**

## Prepare the talk brief

Record:

- **Occasion and audience:** who will attend, what they are there to do (learn, evaluate, decide, or stay informed), how close they are to the field, what they already know, and whether important subgroups have different needs.

- **Evaluation (judged talks):** the rubric, the rules and how strictly time is enforced, the panel’s composition and expertise, and the Q&A format.

- **Purpose and outcome:** inform, explain, persuade, seek a decision, invite collaboration, or establish shared understanding.

- **Message and relevance:** the central message and why this audience should care now.

- **Evidence and objections:** the strongest support, limitations, alternatives, and questions a thoughtful skeptic would raise.

- **Conditions:** speaking time, Q&A time, setting, format, accessibility needs, and whether the material must work afterward without you.

- **Success evidence:** what listeners should be able to restate, evaluate, or do; how you will observe that.

- **Boundaries:** material that must be included, what is outside scope, and what can move to an appendix.

A useful outcome statement is: “After this talk, [audience] should understand [message and implications] well enough to [relevant use or next step].” An informative talk can end in shared understanding without an action request. For a judged talk: “Against [criteria], [panel] should see that [claim about the work], and remember [one distinctive point] after hearing the other entries."

## Design the argument and experience

Connect each major claim to its evidence and its significance for the audience. Where the evidence admits several interpretations, make the uncertainty part of the explanation.

Develop the opening, progression, and ending together. Possible structures include a question followed by findings and implications; a problem followed by options and a recommendation; or an observation followed by an explanation and consequences. Select the structure that serves the occasion.

For every segment, record:

**Audience question → takeaway → support → visual or demonstration → spoken explanation → transition → time.**

Choose the detail that belongs on screen, the detail you will say, and the detail that belongs in supporting material. Include where a listener may need an orientation cue, definition, or concrete example.

## Review the talk

Begin with the big-picture review, then use the shared review materials with these questions:

- **Comprehension:** What is the main message? What supports it? Why does it matter? What conclusion or next step is being proposed?

- **Relevance:** Which parts depend on interests, authority, or background that this audience may not share?

- **Skepticism:** Which claim is least supported? What credible alternative or objection is left unanswered? Does the recommendation exceed the evidence?

- **Delivery:** Can listeners read and interpret the visuals at the intended size? Does the narration explain the necessary connections? Where does the pace become difficult?

Ask for the location and consequence of each finding. A reviewer who disagrees with a recommendation should identify the competing reasoning; disagreement alone does not establish that the talk is unclear.

## Produce and rehearse

Build the slides and notes from the reviewed plan. Then run a drift check against the brief: look for stronger claims, lost qualifications, missing evidence, or an ending that has changed purpose.

Rehearse aloud with the actual visuals and demonstrations. Include transitions, pauses, interaction, and the planned Q&A allowance. Prepare a shorter route through the talk that preserves its central argument if time is reduced.

Prepare answers to likely questions, the evidence you may need to show, and language for acknowledging what remains unknown. If the deck will circulate, prepare enough explanation for that separate use.

## Decide when the talk is ready

Proceed when:

- A fresh reviewer can recover the central message and its main support.

- The opening establishes relevance and the ending fulfills the stated purpose.

- Material claims are supported and significant uncertainty remains visible.

- Essential context is available when the audience needs it.

- A real rehearsal fits the slot and the visuals work in the delivery setting.

- Consequential review findings have been resolved or consciously accepted.

Afterward, record the questions, misunderstood points, timing, and relevant follow-up. Distinguish communication quality from outcomes affected by other factors: a clear proposal may still be declined.

# Educational lectures

The lecture workflow supports a single class session or a connected sequence of sessions. Its central question is: **What should students be able to do, and what work will show that they can do it?**

Align the learning objectives, the activities through which students practice, and the assessments that reveal their progress. This follows the instructional alignment described by [Carnegie Mellon’s Eberly Center](https://www.cmu.edu/teaching/assessment/basics/alignment.html).

## Prepare the lesson brief

Record:

- **Course position:** the unit, relevant previous lessons, and where the learning will be used next.

- **Learner starting point:** prerequisites, evidence of current understanding, likely misconceptions, and variation within the class. Distinguish material previously covered from learning actually demonstrated.

- **Objectives:** a manageable set of observable performances, such as interpreting a graph, comparing explanations, constructing an argument, or solving a problem.

- **Evidence of learning:** the tasks students will attempt and the features that count as a satisfactory response.

- **Instruction and support:** explanations, examples, practice, feedback, and resources students can use.

- **Conditions:** duration, class size, modality, preparation expected, materials, and access or participation needs.

- **Course connections:** follow-up practice, later retrieval, and how results will shape the next session.

Phrase each objective as: “Given [conditions or material], students can [observable action], with [criteria for adequate performance].”

## Connect objectives to student work

For each objective, specify:

**Prerequisite → explanation or example → practice → independent attempt → feedback → later use.**

An illustrative objective is: “Given an unfamiliar observational claim, students can explain why the observation alone does not establish causation and identify a plausible alternative explanation.”

| Design element | Application to this objective |
| - | - |
| Prior knowledge | Recognize a relationship between two observed variables. |
| Instruction | Model how to distinguish an observation from a causal explanation. |
| Guided practice | Compare possible explanations with a partner and justify a choice. |
| Independent evidence | Explain a different scenario individually, including an alternative explanation. |
| Response criteria | Acknowledge the limit of the evidence and give a relevant, coherent alternative. |
| Follow-up | Revisit the reasoning in a new context during a later session. |

For interpretive subjects, the criteria may emphasize evidence, reasoning, and engagement with alternatives. Make room for multiple defensible responses.

## Design the lecture as an experience

Plan a sequence of explanation and student work. At each significant step, specify what students see or hear, what they must think or do, what response you will inspect, and how you will respond.

An explanation may lead into a prediction, a worked example, a short written response, a discussion, a problem, or a critique. Include time to explain the activity and discuss what its results mean. Cornell’s teaching guidance describes these activities and emphasizes time for feedback and debriefing. [Active learning techniques](https://teaching.cornell.edu/teaching-resources/active-collaborative-learning/active-learning/getting-started-active-learning)

An illustrative 50-minute session could allocate:

| Minutes | Activity |
| - | - |
| 0–5 | Opening question and prerequisite check |
| 5–13 | Explanation of the central concept |
| 13–20 | Worked example with predictions |
| 20–30 | Guided practice and discussion |
| 30–38 | Feedback and examination of misconceptions |
| 38–45 | Individual application to a new case |
| 45–48 | Exit response and connection to the next lesson |
| 48–50 | Buffer and closure |

This is a planning example; the timing should follow the subject, students, and observed pace. Include instructions and movement between activities in the estimates.

## Review the lesson

Begin with the big-picture review: does this session, as planned, suit these students, this point in the course, and the time available? Then use fresh reviewers for the following tasks:

- **Prerequisites and sequence:** Identify each necessary concept or skill. Locate where students learn or retrieve it before it is required.

- **Misconceptions:** Identify a plausible incorrect interpretation, the wording or example that could support it, and a question that would reveal it.

- **Accuracy:** Check definitions, explanations, demonstrations, examples, and the boundaries of useful simplifications.

- **Assessment:** Attempt the student tasks without the answer key. Then examine whether the key, rubric, and tasks match the objectives and permit reasonable answers.

- **Participation and delivery:** Check instructions, workload, visibility, pacing, and whether students have a workable way to participate.

A review should identify the particular gap in an explanation or task. An AI’s ability to solve the task is not evidence that students have acquired the skill.

## Rehearse and prepare responses to student thinking

Work through every example and student task yourself. Check whether the materials support the reasoning students need and whether there is enough time for them to think.

For important checks, prepare a response rule. If a prerequisite is missing, supply a brief bridge. If a misconception appears, compare explanations or use a counterexample. If most students are ready, move to an extension. Decide which optional material can be deferred to preserve essential practice and feedback.

Prepare student materials separately from instructor notes, solutions, and teaching rationale.

## Decide when the lesson is ready

Proceed when:

- Each essential objective has practice and a task that can reveal progress.

- Necessary prerequisites are available or have a planned check and response.

- Examples, tasks, and response criteria are accurate and usable.

- Students have time to work and receive feedback.

- The instructor has a plan for likely misconceptions and timing changes.

- Essential materials are readable and participation is feasible.

After delivery, examine actual student work, including patterns among students whose understanding is least secure. Record which objectives need further attention. Use a later task to check whether learning persists and can be used in a different context.

Student satisfaction and confidence can inform the experience; demonstrated work provides evidence about the learning objectives.

# Review decisions and effort

Use a short finding format:

**Location — observed issue — likely consequence — supporting reason — proposed change — importance.**

Classify importance by consequence:

- **Essential correction:** factual error, unsupported central claim, missing prerequisite, unusable task, or timing problem that prevents the core outcome.

- **Meaningful improvement:** change likely to improve clarity, participation, reasoning, or usefulness.

- **Optional refinement:** preference or polish with little effect on the outcome.

## Respond to each finding

The Elephant proposes one response to each finding. The presenter or instructor decides and records the reason.

- **Fix:** The finding is valid. Change the brief, plan, or materials.

- **Contest:** The reviewer misread the materials. Cite the slide, note, source, or recorded decision that the reviewer could have checked.

- **Escalate:** The finding depends on something only the presenter or instructor can confirm, such as what will be said aloud, an organizer’s requirement, or what students demonstrated in an earlier session; or it is a comprehension finding in doubt that a recheck could settle. The presenter or instructor decides.

- **Decline:** The finding is an optional refinement. Record it without changing the materials.

Apply these rules:

- **A contest needs evidence the reviewer could have read.** “That was intentional” is not evidence.

- **Investigate a comprehension gap before dismissing it.** A reported gap is a signal, not proof: an AI reviewer can misread, or lack knowledge the audience has. Do not contest it on the author’s reading alone. Settle a doubtful finding with an independent recheck by a new fresh reviewer, or with feedback from a person who resembles the audience, and contest it only with that evidence. If the review lacked something participants will have, such as the narration, supply it and repeat the review.

- **Add context for the audience, not for the reviewer.** If only a reviewer without the audience’s background needs an explanation, escalate the finding instead of adding the explanation.

- **Do not change a finding’s importance.** To disagree with its importance, contest it and give the reason.

- **The wish to defend the material is not evidence.** Whoever wrote the material should expect to want to contest findings about it.

Put every decision in front of the presenter in the conversation, complete enough to decide from: a one-line summary, one table with a proposed response for each finding, the questions only the presenter can answer, and an invitation to name only the exceptions. Files hold the reasoning and the record, not the decision. Do not assume the presenter has opened them.

Update the actual brief, materials, or activity; a conversational explanation does not repair the artifact. Recheck the parts affected by substantial changes.

Stop reviewing when essential corrections are resolved, important trade-offs are explicit, and the relevant rehearsal has passed. Reviewers do not need to agree on every stylistic choice.

Scale effort to the work:

| Situation | Appropriate preparation |
| - | - |
| Small revision for a familiar audience | Update the brief, run a drift check, inspect the changed sections, obtain one focused fresh review, and rehearse the changes. |
| New talk or lecture | Use the full cycle, including a big-picture review and separate comprehension and accuracy checks. |
| Major change of audience, purpose, or course level | Start with a big-picture review and reconsider outcomes and sequence before deciding what to reuse. |
| Consequential professional decision or difficult core course concept | Add a subject expert or representative human reviewer and scrutinize the evidence or student tasks. |

Keep two improvement loops visible: revisions before delivery, and changes based on actual audience or student responses afterward. After delivery, compare the problems the reviewers predicted with those that actually occurred. Problems nobody predicted show what the next round of reviews should look for.

# The same subject in the two versions

Consider a subject such as evaluating a promising new research method.

**Professional talk:** A research team needs to decide whether the method merits a pilot. The Elephant organizes the findings, limits, comparison with current practice, and a proportionate next step. Goldfish reviewers reconstruct the recommendation, challenge the evidence, and identify unanswered questions. The delivered talk explains what a pilot could establish and what remains unknown. Follow-up records whether listeners understood the trade-offs and what information they still needed.

**Educational lecture:** Students need to judge what an evaluation study can and cannot establish. The Elephant identifies the necessary concepts, selects contrasting examples, and designs practice in evaluating evidence. Goldfish reviewers locate prerequisite gaps, misleading simplifications, and problems with the questions or response criteria. Students then analyze a new example individually. Their reasoning determines what the instructor revisits.

The evidence may overlap, while the sequence, depth, activities, and measures of success follow the distinct purposes.

# Reusable starting prompts

## Professional talk

> Help me prepare or adapt a professional talk using Talking with Elephants & Goldfish. My starting material may be a topic, notes, an outline, or an existing deck.
>
> First read what I have supplied and tell me briefly what you know, what you are inferring, and what is missing. Then, before designing anything, interview me one question at a time about my starting material, end goal, audience and what they are there to do (for example, judges scoring me against criteria versus colleagues staying informed), how close they are to my field (specialists, adjacent experts, informed non-experts, or novices), my role and what I want from the talk for myself, the occasion and constraints, and how I'll know it worked. If I will be judged or evaluated, ask for the rules, criteria, and panel composition. If I am adapting existing material, also ask what has changed and what must carry over. Ask the most consequential question first, skip what my materials already answer, follow up once on vague answers, and point out contradictions. When you can state the outcome, audience, constraints, and success evidence, read them back with your key assumptions for my confirmation, then write the brief. Label each item in the brief as confirmed, inferred, assumed, or open.
>
> Develop the argument and a timed experience plan before polishing slides. When more than one structure is defensible, show me the options with their trade-offs. If I ask you to choose, recommend one, say why, and proceed when I say go. Offer to draft the whole plan for me to mark up, or to build it with me step by step. If material already exists, recommend what to keep, reframe, replace, remove, or move to supporting material, with reasons.
>
> Start reviews with a fresh big-picture review of whether this talk fits the audience, purpose, and occasion. Then prepare distinct materials for fresh comprehension, evidence, and delivery reviews. Keep the private intended message out of the initial comprehension test while retaining everything the audience actually receives. For each finding, propose whether to fix, contest, escalate, or decline it; a contest must cite something the reviewer could have read, and anything only I can confirm comes to me. I decide, and accepted changes go into the materials. If I am reusing a deck, check it for drift from the current brief. Help me plan human reviewers so that at least one representative person stays fresh for the full rehearsal. For a live talk, include a rejoining review from partway through. Put every decision I need to make in the chat as one table, with your proposal for each, and let me name only the exceptions.
>
> Finish with a delivery package, a rehearsal plan, likely questions, and a short plan for learning from audience responses.
>
> Starting material and occasion: [insert what you have, or leave blank and let the interview gather it].

## Educational lecture

> Help me prepare or adapt a college lecture using Talking with Elephants & Goldfish. My starting material may be a topic, syllabus, notes, activities, or an existing deck.
>
> First read what I have supplied and tell me briefly what you know, what you are inferring, and what is missing. Then, before designing anything, interview me one question at a time about my starting material, where the session sits in the course, what students have actually demonstrated, likely misconceptions, what students should be able to do afterward, the class conditions, my role, and the student work that will show progress. If I am adapting existing material, also ask what has changed and what must carry over. Ask the most consequential question first, skip what my materials already answer, follow up once on vague answers, and point out contradictions. When you can state the learning objectives, students, conditions, and evidence of learning, read them back with your key assumptions for my confirmation, then write the brief. Label each item in the brief as confirmed, inferred, assumed, or open.
>
> Connect each objective to prerequisites, explanation, practice, an independent student response, and feedback. Develop a timed lesson plan that includes student thinking and transitions. When more than one sequence is defensible, show me the options with their trade-offs. If I ask you to choose, recommend one, say why, and proceed when I say go. Offer to draft the whole plan for me to mark up, or to build it with me step by step. Explain how existing material should be retained or changed.
>
> Start reviews with a fresh big-picture review of whether this session fits these students, this point in the course, and the time available. Then prepare distinct materials for fresh prerequisite, misconception, accuracy, assessment, and delivery reviews. Keep instructor rationale and answer keys out of the initial learner or task review. Then review the response criteria and solutions explicitly. For each finding, propose whether to fix, contest, escalate, or decline it; a contest must cite something the reviewer could have read, and anything only I can confirm comes to me. If I am reusing a deck, check it for drift from the current brief. Help me plan human reviewers so that at least one representative person stays fresh for the final version. Include a rejoining review from partway through the session. Put every decision I need to make in the chat as one table, with your proposal for each, and let me name only the exceptions.
>
> Finish with teaching materials, separate student materials and instructor notes, a plan for responding to student difficulties, and a way to use student work to improve the next lesson.
>
> Starting material and course context: [insert what you have, or leave blank and let the interview gather it].

## Fresh review

> Review the supplied version independently. Use only the material authorized for this review. Your role is [big-picture, design, comprehension, rejoining (starting partway through), evidence, assessment, delivery, drift (comparing materials with the brief, plan, and decisions), or judge scoring against the supplied criteria]. Expected participant background is [insert, including how close they are to the field: specialists, adjacent experts, informed non-experts, or novices].
>
> If the role, participant background, or review materials are missing, ask me for them before you begin. Do not ask what I intended or request background the participants would not have; work from the materials as supplied.
>
> For a big-picture review, judge whether the planned talk or lesson suits the stated audience, purpose, and occasion before examining details. For other roles, first state what the materials communicate or ask participants to do. Identify where your interpretation depends on information that participants do not receive. Distinguish what is supported from what you are inferring.
>
> Report consequential findings with their location, likely effect, supporting reason, proposed correction, and importance. Do not manufacture criticism or treat personal style preferences as errors. For an assessment attempt, work without the answer key before reviewing it.
>
> Review materials: [insert the appropriate materials].
