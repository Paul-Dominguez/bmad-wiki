# Phase 1 — Understand the story

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

Establish what the Rally story requires before investigating implementation.

**Lead:** Mary / Analyst  
**Recommended model : Claude Sonnet 5**

## Inputs

Original Rally story and linked material explicitly in scope, with revision or approved snapshot; applicable enterprise/project instructions.

## Output

`<STORY-DIR>/01-requirements-analysis.md`. Replace the story directory and any unit/review identifier before pasting. Preserve existing approved records; substantive revisions require renewed approval.

## Copy the authorization and phase prompt

Fill every placeholder. This block grants only its listed actions under the master. Keep the explanatory page outside the copied prompt.

```text
Apply the previously supplied BMAD master contract. Perform only this phase.
If the master or a required value is missing, stop before substantive work.

STORY / WORKSPACE: <RALLY-ID> / <repository or worktree>
PHASE / UNIT: 1
PHASE AUTHORIZED: YES
PRIMARY ROLE: Mary / Analyst
Recommended model : Claude Sonnet 5
SELECTED MODEL / BASIS: <actual selection; host-confirmed, user-reported, or unverified>
EXECUTION METHOD: Enterprise procedure EP-1 below; not an automatic native workflow invocation.
APPROVED INPUTS / REVISIONS: <resolve the inputs listed on this page>
ALLOWED READS: The named Rally source/snapshot and linked materials; relevant project instructions and BMAD configuration/skill metadata. No application-code investigation.
ARTIFACT MODE: WORKSPACE
EXPECTED OUTPUT / ALLOWED ARTIFACT WRITES: <STORY-DIR>/01-requirements-analysis.md only
ALLOWED SOURCE / TEST / CONFIG WRITES: NONE
ALLOWED COMMANDS / ENVIRONMENT: Read-only file/search/Git status/diff/hash inspection within the allowed reads; no app/test execution.
ALLOWED RUNTIME OUTPUTS: NONE
BMAD ACTIVATION COMMANDS / RUNTIME: <tested compatible profile with commands/output paths, or NONE>
DELEGATION: DISABLED
GIT MUTATIONS: NONE
EXTERNAL MUTATIONS: NONE
STOP CONDITION: Draft artifact and concise handoff delivered, or a blocking issue identified.

PREPARATION
Verify story, workspace, inputs/revisions, permissions, and relevant BMAD version/profile.
Use only the allowed preparation actions. Report the role/procedure actually used.
If persona activation is not authorized, do not claim it occurred. Never substitute
an unbounded native workflow for this enterprise procedure. Any conflicting required
effect must be resolved before invocation. Resolve the exact output path before writing.

TASK
1. Capture the business objective, actors, trigger, expected outcomes, explicit rules, exclusions, dependencies, and stated nonfunctional requirements.
2. Preserve original acceptance-criterion IDs; otherwise assign stable local IDs with exact source wording. Map each to an observable outcome.
3. Distinguish facts from assumptions, candidate implications, contradictions, and unanswered product questions. Do not promote an inference into scope.
4. Record relevant glossary terms and focused questions for codebase discovery; any suggested code area is only a hypothesis at this phase.
5. Write the named requirements artifact with source revision and traceability. Do not design, inspect implementation code, update Rally, or automatically invoke the PM.

HANDOFF
Return artifact path/revision, baseline, key findings, actual validation or NOT RUN,
open decisions, and approval status. Keep full evidence in the artifact; avoid
duplicating it in chat. NEXT AUTHORIZED ACTION: USER REVIEW. STOPPED: YES.
```

## Human review checklist

- [ ] Every AC is traceable to the source.
- [ ] Unknown requirements are visible, not invented.
- [ ] The artifact describes desired behavior without claiming repository facts.
- [ ] Output path, revision, and approval conditions are correct.

## Copy approval only after reviewing

```text
APPROVED BY USER
STORY / PHASE: <RALLY-ID> / 1
ARTIFACT PATH / CONTENT REVISION: <STORY-DIR>/01-requirements-analysis.md / <exact SHA-256 or immutable revision>
INPUT BASELINE: <requirements revision and relevant code baseline; NOT ASSESSED for code in requirements-only phases>
CONDITIONS: NONE
APPROVAL RECORD WRITE: <STORY-DIR>/approvals.md; append this decision only
NEXT-PHASE AUTHORIZATION: NONE
Do not change the approved artifact, source, or external systems.
Record this human decision, acknowledge, and stop.
```

If changes are needed, use [the revision pattern](Approvals-and-Handoffs.md). Approval does not execute the next phase.

**Navigation:** [Previous](Developer-Workflow.md) · [Workflow index](Developer-Workflow.md) · [Next page](Phase-1B-Requirements-Review.md)
