# BMAD role guides

[Home](Home.md) · [Agents](Agents.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft role starters | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Choose your role

These pages explain how BMAD can support the wider agile team. Each includes an agent recommendation, useful inputs, a fictional trial prompt, expected output, and a human review checklist. They are role starters, not yet complete gated production workflows.

| Your role | Start with | Trial output |
| --- | --- | --- |
| [Business Analyst](Role-Business-Analyst.md) | Mary | A requirements table, prioritized questions, and proposed acceptance wording. |
| [Product Owner and Product Manager](Role-Product-Owner.md) | John | A small proposed backlog with outcomes, dependencies, and outstanding decisions. |
| [QA and Test Engineer](Role-QA-Test-Engineer.md) | Amelia | An AC-to-scenario matrix and a short list of coverage questions. |
| [UX and Product Designer](Role-UX-Designer.md) | Sally | A state/interaction table, proposed focus behavior, and prototype-review checks. |
| [Technical Lead and Architect](Role-Technical-Lead.md) | Winston | A proposed decision record with boundaries, alternatives, and verification needs. |
| [Scrum Master and Delivery Lead](Role-Scrum-Master.md) | John | A readiness/dependency table, meeting questions, and proposed improvement experiments. |
| [Release and DevOps Engineer](Role-Release-DevOps.md) | Winston | A proposed runbook outline, evidence gates, and unresolved operational questions. |
| [Developer](Developer-Workflow.md) | Amelia | Existing full phase workflow, implementation evidence, and independent review |

The [Agents page](Agents.md) describes native capabilities. These role pairings are our recommendations. Human roles do not map one-to-one to BMAD agent names: Product Owner and Product Manager share a starter, while Scrum Master and Release/DevOps use a relevant core persona rather than an invented dedicated agent.

## Trial setup

1. Use an installed, approved BMAD environment with the recommended model enabled. [Installation](Installation.md).
2. Run trials in a fresh learning chat and a disposable/configured project, rather than inside a developer session awaiting phase authorization. They have their own narrow analysis-only scope and do not require pasting the developer master.
3. Agent activation may load configuration and execute configured startup steps. Use the team's verified setup whose startup effects are permitted; inspect unknown overrides before activation. The later no-tool trial prompt does not retroactively restrict startup.
4. Invoke the exact agent skill listed on the role page through the host's supported mechanism. If it is missing or activation fails, resolve setup separately; do not treat a generic role-play response as verified BMAD execution.
5. Once activation succeeds, paste the role's trial prompt. Use its fictional fixture as supplied for the first run; it needs no Rally connection, repository scan, or file writes.
6. Assess the output using the checklist before moving to real work. A polished response is not evidence that a requirement, test, design, or release is approved.

The actual prompts are bounded enterprise exercises, not native menu workflow invocations. This keeps the first trial short and avoids unintended artifact generation, tracking updates, implementation, or deployment.

## Testing guidance

For the QA starter, use Amelia without launching her QA menu item. Native QA generates and executes tests; broader test design and traceability can use the separately installed TEA module when needed. Verify TEA's version and permissions before use. [Pinned testing guidance](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/docs/build/test-completed-work.md)

For completed-epic evidence, Amelia exposes a retrospective capability. That is distinct from the Scrum Master's facilitation trial and does not automatically represent the team's retrospective or acceptance decision. [Pinned developer menu](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/src/bmm-skills/agents/bmad-agent-dev/customize.toml)

## Shared principles for real work

Keep the same evidence and authorization principles across roles: source revisions, facts separate from assumptions, bounded permissions, reviewable outputs, and human decisions. Adapt the task and artifact to the role; do not make a BA or Scrum Master follow code-implementation phases merely to use BMAD.

Product priorities, acceptance, estimates, team commitments, and release authority remain human responsibilities. Handoffs should preserve the accepted decision and its source, not imply that an agent's draft changed Rally or any other system.

## Efficient use

Each trial is designed for one modest response. Use the role page as a handbook and paste only its prompt. Bring in a second perspective for a named unresolved question; do not run every agent on the same material. [Credit guidance](Models-and-Credit-Efficiency.md).
