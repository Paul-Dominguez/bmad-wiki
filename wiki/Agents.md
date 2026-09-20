# BMAD agents

[Home](Home.md) · [Developer workflow](Developer-Workflow.md) · [Model recommendations](Models-and-Credit-Efficiency.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

For a hands-on example tailored to your job, see [Role guides](Role-Guides.md). Each guide names the agent to invoke and supplies a bounded fictional exercise.

Use this page to choose the specialist perspective that answers your current question. BMAD's BMM module supplies five named agents. Their shipped definitions and menus are summarized below; the phase assignments, examples, and review criteria are recommendations for our enterprise workflow.

An agent is a role with instructions and a menu. A workflow skill performs a task. An LLM runs that work. An artifact preserves its result. Agents do not arrive knowing your codebase, and changing a persona does not transfer verified project knowledge into a new session. [6.12.0 catalog](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/docs/reference/skills-and-agents.md)

## Contents

- [Choose an agent](Agents.md#choose-an-agent)
- [Mary — Business Analyst](Agents.md#mary)
- [John — Product Manager](Agents.md#john)
- [Winston — System Architect](Agents.md#winston)
- [Amelia — Developer](Agents.md#amelia)
- [Sally — UX Designer](Agents.md#sally)
- [Testing and additional roles](Agents.md#testing-and-additional-roles)
- [Worked example](Agents.md#worked-example)
- [Using agents effectively](Agents.md#using-agents-effectively)

## Choose an agent

| Your immediate question | Start with |
| --- | --- |
| What business behavior is being requested, and what is unclear? | Mary |
| Is the scope coherent, valuable, and testable? | John |
| What does the repository actually contain? | Amelia |
| Where should this behavior belong, and how should components connect? | Winston |
| What should the user experience during the interaction? | Sally |
| What exact code and test changes deliver the approved behavior? | Amelia |
| Does the actual implementation meet the original intent? | Separate reviewer using the review capability |

This is a routing aid, not a requirement to run every agent. A supporting question may be answered within an authorized phase without creating another artifact or spawning another agent.

## Mary

**Role:** Business Analyst  
**Agent skill:** `bmad-agent-analyst`

### What Mary does and is best for

Mary investigates a problem before the team commits to a solution. Her emphasis is evidence, precise requirements, and stakeholder perspectives. Use her for unclear business language, domain research, competing interpretations, and early product discovery.

### Native capabilities

Her menu includes brainstorming (`BP`); market, domain, and technical research (`MR`, `DR`, `TR`); technology selection (`TS`); competitive and user-voice research (`CR`, `UV`); product briefs (`CB`); PRFAQ work (`WB`); and project context (`PC`). Research routes use Deep Recon; context work uses `bmad-project-context`. [Shipped role and menu](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/src/bmm-skills/agents/bmad-agent-analyst/customize.toml)

### How we use Mary

Give Mary the Rally story, source revision, terminology, linked business material, and known constraints. In [Phase 1](Phase-1-Story-Understanding.md), expect an AC map, explicit scope, assumptions, and focused questions. A new product brief is unnecessary when approved Rally material already answers those questions.

**Example request:** “Explain the requested behavior and identify what the story leaves undecided. Separate confirmed requirements from assumptions.”

**Review for:** traceability and unanswered questions. A business interpretation does not establish what code exists; repository claims require discovery evidence.

## John

**Role:** Product Manager  
**Agent skill:** `bmad-agent-pm`

### What John does and is best for

John turns product intent into deliverable scope. Use him to challenge ambiguous outcomes, oversized stories, competing priorities, and changes that undermine the original objective. His focus is the value and completeness of the requested result.

### Native capabilities

`PRD` creates, updates, or validates requirements; `CE` breaks work into epics/stories; `IR` checks planning readiness through sprint planning; `CC` addresses significant changes through Correct Course. The readiness route can continue into tracking, so inspect its effects before using it under a bounded authorization. [Shipped role and menu](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/src/bmm-skills/agents/bmad-agent-pm/customize.toml)

### How we use John

In [Phase 1B](Phase-1B-Requirements-Review.md), supply the original Rally material and Mary's approved analysis. Expect a review of clarity, observable outcomes, conflicts, dependencies, and decisions needed. Do not recreate an entire PRD for every existing story.

**Example request:** “Review whether these acceptance criteria distinguish successful, failed, and unsupported outcomes. Propose clarifications without changing approved scope.”

**Review for:** testable outcomes and explicit decisions. John can recommend a scope change; the human product owner approves it. Requirements readiness does not establish technical readiness.

## Winston

**Role:** System Architect  
**Agent skill:** `bmad-agent-architect`

### What Winston does and is best for

Winston resolves technical decisions that affect how separately implemented parts fit together. Use him for ownership boundaries, interfaces, competing implementation locations, integration constraints, and consequential tradeoffs. His approach favors maintainable choices over unnecessary abstraction.

### Native capabilities

`CA` invokes `bmad-architecture` to record architectural rules and decisions. `IR` invokes sprint planning to assess readiness. Neither menu entry means that every story needs a large architecture document. [Shipped role and menu](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/src/bmm-skills/agents/bmad-agent-architect/customize.toml)

### How we use Winston

In [Phase 3](Phase-3-Design.md), give him approved requirements, the evidence-backed implementation map, project constraints, and unresolved ownership questions. Expect a bounded design decision describing where behavior belongs, what is reused or extended, what is new, and which legacy integration changes are necessary.

**Example request:** “Given these legacy and newer files, decide the implementation ownership for each required capability and explain the smallest compatible change.”

**Review for:** decisions tied to inspected code and approved requirements. An elegant design built on guessed repository facts is not ready for implementation. Keep established, low-risk patterns brief.

## Amelia

**Role:** Developer / Senior Software Engineer  
**Agent skill:** `bmad-agent-dev`

### What Amelia does and is best for

Amelia implements approved work with test discipline and precise code evidence. Use her for understanding actual execution paths, planning concrete changes, writing code and tests, and investigating defects.

### Native capabilities

Her menu provides Build (`BD`), API/E2E test generation (`QA`), code review (`CR`), sprint planning (`SP`), and epic retrospective (`ER`). Her shipped principles emphasize verified results, minimal code, and avoiding workflow metadata in source comments. [Shipped role and menu](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/src/bmm-skills/agents/bmad-agent-dev/customize.toml)

### How we use Amelia

Use her for evidence gathering in [Phase 2](Phase-2-Codebase-Discovery.md), bounded planning in [Phase 4](Phase-4-Implementation-Planning.md), and authorized implementation in [Phase 5](Phase-5-Implementation.md). Supply approved inputs, exact paths, current baseline, and permitted commands. Expect repository evidence first, then a plan, then an actual diff and observed validation results under separate authorizations.

**Example request:** “Implement only the approved unit in the newer implementation files and the named legacy integration point; verify the required behavior.”

**Review for:** correct location, existing behavior reused appropriately, working integration, and honest test results. Access to a review menu does not make the implementer its own independent reviewer.

## Sally

**Role:** UX Designer  
**Agent skill:** `bmad-agent-ux-designer`

### What Sally does and is best for

Sally translates user needs into interaction and experience decisions that inform architecture and implementation. Use her when a story changes navigation, task flow, user feedback, page states, or accessibility expectations.

### Native capabilities

`CU` invokes `bmad-ux`. Her shipped principles emphasize user needs, simple starting points, and refinement through feedback. [Shipped role and menu](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/src/bmm-skills/agents/bmad-agent-ux-designer/customize.toml)

### How we use Sally

Consult Sally within [Phase 3](Phase-3-Design.md) when there is an unresolved UX question. Give her the user goal, approved requirements, current screens or flow, design-system constraints, and relevant accessibility requirements. Record the resolved interaction in the design artifact; a separate full UX workflow is warranted only when its output is needed.

**Example request:** “Define the user's experience when this action moves to the newer page, including loading, failure, return navigation, and preserved context.”

**Review for:** a complete interaction rather than only a successful screenshot. A UX proposal does not prove that routes, permissions, or backend capabilities exist; technical discovery must establish them.

## Testing and additional roles

### Built-in QA versus Test Architect

Amelia's `QA` capability generates API/E2E tests for implemented features. The separate **TEA** module offers broader testing capabilities, including heavier automated coverage, test design, traceability, ATDD, and nonfunctional assessment. Use it when the required assurance justifies the additional setup and work; verify the installed TEA version separately from BMM. [6.12.0 testing guide](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/docs/build/test-completed-work.md)

Generated tests, implementation review, and human acceptance answer different questions. Test generation writes files and may run/fix tests; it cannot be invoked under an artifact-only review permission. Our Phase 5 still includes associated tests even when no additional QA workflow is selected.

### Names from older tutorials

The five agents above are the core BMM directory for this baseline. Paige, the technical writer, is described as on hiatus; project context remains available through Mary's `PC` capability. Older role lists may differ. Inspect the project's installed modules and effective overrides before relying on a tutorial's agent list. [Pinned catalog](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/docs/reference/skills-and-agents.md)

## Worked example

**Situation:** A Rally feature moves an existing action toward newer functionality. The repository contains legacy behavior and some newer implementation, but the newer capability is incomplete.

| Agent contribution | Question to answer | Evidence or decision handed forward |
| --- | --- | --- |
| Mary | What outcome does the story require? | Confirmed behavior, ACs, and unanswered business questions |
| John | Are scope and success conditions clear? | Reviewed requirements and explicit clarification decisions |
| Amelia, during discovery | Where does the action run today, and which newer pieces already exist? | Routes/callers, newer files, current capability, and missing behavior |
| Winston | Where should each required change belong? | Approved reuse/extension/new-code decisions and legacy integration boundary |
| Sally, if needed | What should the user experience during the transition? | Navigation, state, errors, and continuity decisions |
| Amelia, during planning and implementation | Which authorized edits and tests deliver that design? | Bounded plan, actual changes, and verification evidence |
| Separate reviewer | Does the actual behavior satisfy the original story? | Findings on placement, wiring, duplication, regressions, and AC coverage |

The same feature can legitimately need new code, extensions to newer files, and a small legacy integration edit. The handoffs preserve that distinction instead of letting the existing legacy location determine every change.

## Using agents effectively

1. Select the role for a specific question. Give it approved inputs and a bounded result, not “analyze everything.”
2. Start from the [master](Master-Template.md) and the [authorized phase card](Developer-Workflow.md). Examples on this page are illustrative; they are not standalone authorization prompts.
3. Verify the installed persona/skill and effective configuration before activation. Menu codes are agent-specific: Mary's `CR` concerns competitors; Amelia's `CR` concerns code. Use the host's supported invocation method rather than assuming a slash prefix.
4. Check the workflow's side effects before dispatch. Build and review may do more than the current phase permits; use the tested enterprise procedure when needed. [Compatibility guidance](Developer-Workflow.md#native-bmad-compatibility).
5. Pass the approved artifact references and necessary evidence to the next role. Verify changed inputs; avoid repeated full-repository investigations and copied chat history.
6. Keep one owner for each phase result. Optional perspectives do not automatically authorize delegation, extra documents, or the next phase.
7. Choose the LLM separately using [model and credit guidance](Models-and-Credit-Efficiency.md). Keep this explanatory page out of everyday phase prompts.

**Next:** [Developer workflow](Developer-Workflow.md) · [Approvals and handoffs](Approvals-and-Handoffs.md)
