# BMAD team wiki

## What is BMAD?

BMAD is the **Breakthrough Method of Agile AI-driven Development**. It adds reusable skills and specialist agent roles to an AI coding environment, helping a team clarify requirements, investigate an existing system, design changes, implement them, and review the result. It can support analysis without writing code, as well as software delivery.

Think of an **agent** as a specialist role, a **skill** as the capability you invoke, and an **artifact** as the reviewable result. The **LLM** is the model running the work. Choosing an agent and choosing a model are separate decisions.

This wiki explains our proposed use of BMAD with Rally and GitHub Copilot. Our developer phases and human approval gates are an enterprise procedure layered over BMAD, not BMAD's native phase numbering. Developers have a complete phase sequence; the wider agile team has role-specific guides and bounded trial prompts.

## Start here

**Delivering a story?** Follow this sequence:

1. [Install BMAD](Installation.md) in the project, or verify an existing setup.
2. Open [Master template](Master-Template.md), fill the configuration, and paste its prompt once in a new chat.
3. Go to [Developer workflow](Developer-Workflow.md), select the current phase, and paste only that phase's completed authorization prompt.
4. Review the artifact and use its separate approval block. Authorize the next phase only when ready.

## Table of contents

| Page | What you will find |
| --- | --- |
| [Installation](Installation.md) | Standard setup, a 6.12.0 pin, and installation verification |
| [Agents](Agents.md) | Detailed profiles, best uses, capabilities, and handoff examples |
| [Role guides](Role-Guides.md) | How BMAD supports each agile role, which agent to invoke, and fictional trial prompts |
| [Master template](Master-Template.md) | The reusable session contract before any phase begins |
| [Developer workflow](Developer-Workflow.md) | Phase navigation, agent responsibilities, inputs, and outputs |
| [Phase 1 — Understand the story](Phase-1-Story-Understanding.md) | Rally requirements and acceptance-criterion traceability |
| [Phase 1B — Review requirements](Phase-1B-Requirements-Review.md) | Clarity, testability, and unresolved product questions |
| [Phase 2 — Discover the code](Phase-2-Codebase-Discovery.md) | Current behavior, newer foundations, and implementation gaps |
| [Phase 3 — Decide the design](Phase-3-Design.md) | Implementation ownership, interfaces, and reuse decisions |
| [Phase 4 — Plan changes and tests](Phase-4-Implementation-Planning.md) | Bounded implementation units and exact permitted paths |
| [Phase 5 — Implement one unit](Phase-5-Implementation.md) | Approved changes, tests, and observed results |
| [Phase 6 — Independently review](Phase-6-Independent-Review.md) | Evidence-based verification and correction routing |
| [Approvals and handoffs](Approvals-and-Handoffs.md) | Revisions, approval records, corrections, and new sessions |
| [Models and credit efficiency](Models-and-Credit-Efficiency.md) | Model defaults, escalation, and feature-level budgets |
| [Troubleshooting](Troubleshooting.md) | Missing skills, stale evidence, wrong code placement, and workflow conflicts |
| [Maintaining this wiki](Maintaining-the-Wiki.md) | Ownership, pilot checks, and publication guidance |
| [References](References.md) | Official documentation and pinned behavior sources |

## The codebase problem this workflow addresses

An existing application may contain legacy behavior alongside a partial newer implementation. Agents must locate both, identify what remains to be built, and establish where each change belongs before implementation. New files may be appropriate; duplicating existing behavior or putting new behavior in the wrong area is not.

## Working agreement

**Authorize → produce evidence → human review → approve the exact revision → separately authorize the next phase.** Reading a wiki page does not authorize tool use. Paste only its marked prompt when you intend to begin that work.

These pages are a reviewable draft. They have not been execution-tested against the enterprise Copilot installation. [Pilot checklist](Maintaining-the-Wiki.md).
