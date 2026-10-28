---
name: education-learning
description: "Design objectives, lessons, curricula, assessments, study materials, tutoring, and accessible learning experiences."
license: CC-BY-SA-4.0 AND MIT
---

# GNCore Education and Learning

## Select the work from the user's intent

Identify the learner's starting point, learning objective, context, and available teaching material. Align explanation, practice, feedback, and assessment to the objective. Use retrieval, worked examples, scaffolding, and spaced review where they fit the task; preserve the intended cognitive demand.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check factual accuracy, alignment, answer keys, difficulty, accessibility, and whether the assessment actually demonstrates the target skill rather than familiarity with wording.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `education-learning-objectives` | Write measurable learning objectives aligned with learner needs, prerequisites, practice, and assessment. |
| `education-lesson` | Plan a lesson with sequenced explanation, active practice, feedback, and accessible timing. |
| `education-curriculum` | Organize a curriculum into coherent progression, prerequisite links, practice, and assessment. |
| `education-assessment` | Create an assessment aligned to learning outcomes with clear instructions and fair scoring. |
| `education-rubric` | Develop a behavior-anchored rubric that supports consistent feedback and grading. |
| `education-study-guide` | Create a focused study guide with key concepts, retrieval practice, examples, and self-check answers. |
| `education-tutor` | Tutor a learner by diagnosing understanding, guiding practice, and adapting explanations. |
| `education-content-accessibility` | Adapt learning content for accessible navigation, language, formats, and participation. |
| `education-feedback` | Synthesize learner feedback into evidence-based course improvements while protecting privacy. |
| `education-course-review` | Review a course for alignment among objectives, instruction, practice, assessment, workload, and accessibility. |

## Focused procedures

### Learning Objectives (`education-learning-objectives`)

Specify observable performance, context, success threshold, prior knowledge, and transfer. Ensure every assessment measures the intended objective rather than recall unrelated to the goal.

### Lesson Plan (`education-lesson`)

State audience, duration, prerequisites, materials, objective, activity sequence, checks for understanding, and adjustment options. Make timing realistic and include a closure that verifies learning.

### Curriculum Map (`education-curriculum`)

Map competencies, units, dependencies, expected depth, assessment evidence, and revision owners. Check workload and avoid gaps or accidental repetition across courses.

### Assessment Design (`education-assessment`)

Use a transparent rubric, representative tasks, accessible format, time expectations, and accommodations. Check construct coverage, ambiguity, and answer keys before release.

### Scoring Rubric (`education-rubric`)

Define criteria from objectives, use distinct observable performance levels, avoid double-counting, include exemplars where useful, and calibrate with sample responses.

### Study Guide (`education-study-guide`)

Prioritize material tied to outcomes, explain misconceptions, vary practice difficulty, include answer rationales, and avoid implying that the guide guarantees a particular score.

### Tutoring Session (`education-tutor`)

Ask what the learner has tried, use hints before answers, check understanding with a new example, correct misconceptions kindly, and respect the learner's requested level of help.

### Accessible Learning Material (`education-content-accessibility`)

Use semantic headings, readable language, captions/transcripts, alt text, keyboard-compatible activities, and multiple ways to engage. Preserve the learning objective while changing presentation where needed.

### Learner Feedback Synthesis (`education-feedback`)

Group feedback by course element and learner outcome, note response bias and sample size, include dissenting observations, and propose a small change with a measurable review point.

### Course Quality Review (`education-course-review`)

Trace outcomes through materials and evaluation, sample the learner journey, inspect prerequisites and workload, document barriers and evidence, and prioritize improvements by learning impact.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [samber/developer-relations-skills / developer-education-strategy](research/samber-developer-relations-skills-developer-education-strategy/GUIDE.md): MIT.
- [dylantarre/animation-principles / education-learning](research/dylantarre-animation-principles-education-learning/GUIDE.md): MIT.
- [garethmanning/education-agent-skills / learning-progression-builder](research/garethmanning-education-agent-skills-learning-progression-builder/GUIDE.md): CC-BY-SA-4.0.
- [garethmanning/education-agent-skills / learning-analytics-interpretation-guide](research/garethmanning-education-agent-skills-learning-analytics-interpretation-guide/GUIDE.md): CC-BY-SA-4.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
