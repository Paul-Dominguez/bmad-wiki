# Phase 3 — Decide the design

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

Resolve implementation ownership and the smallest design that meets the approved requirement.

**Lead:** Winston / Architect; consult Sally for specific UX questions when relevant  
**Recommended model : Claude Sonnet 5**

## Inputs

Approved requirements, requirements review, 02-current-state-analysis.md, and approval records; relevant existing architecture constraints. Supply exact paths/revisions.

## Output

`<STORY-DIR>/03-design-decision.md`. Replace the story directory and any unit/review identifier before pasting. Preserve existing approved records; substantive revisions require renewed approval.

## Copy the authorization and phase prompt

Fill every placeholder. This block grants only its listed actions under the master. Keep the explanatory page outside the copied prompt.

```text
Apply the previously supplied BMAD master contract. Perform only this phase.
If the master or a required value is missing, stop before substantive work.

STORY / WORKSPACE: <RALLY-ID> / <repository or worktree>
PHASE / UNIT: 3
PHASE AUTHORIZED: YES
PRIMARY ROLE: Winston / Architect; consult Sally for specific UX questions when relevant
Recommended model : Claude Sonnet 5
SELECTED MODEL / BASIS: <actual selection; host-confirmed, user-reported, or unverified>
EXECUTION METHOD: Enterprise procedure EP-3 below; not an automatic native workflow invocation.
APPROVED INPUTS / REVISIONS: <resolve the inputs listed on this page>
ALLOWED READS: Named inputs, approvals, relevant source/interfaces/tests/configuration, project instructions, and BMAD configuration/skill metadata.
ARTIFACT MODE: WORKSPACE
EXPECTED OUTPUT / ALLOWED ARTIFACT WRITES: <STORY-DIR>/03-design-decision.md only
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
1. Verify discovery facts needed for the decision. If material evidence is missing, identify a bounded discovery update rather than guessing.
2. For each affected capability, select intended implementation ownership and REUSE, REWIRE, EXTEND, REPLACE, or NEW. Explain the requirement/gap and exact existing or proposed file/module locations.
3. Define only relevant interfaces, data changes, state/navigation, error behavior, compatibility, rollout/rollback considerations, and security/accessibility constraints. Consult the UX role only for an actual unresolved interaction question.
4. Identify necessary legacy integration edits separately from newer implementation work. Avoid both unjustified duplication and forced reuse.
5. Record consequential alternatives and the chosen rationale; keep minor established patterns brief. List assumptions and human decisions still required.
6. Write the design artifact. No source/test/configuration writes. If a separate design is unnecessary, produce a concise waiver proposal with evidence and retained constraints; only human approval makes it effective.

HANDOFF
Return artifact path/revision, baseline, key findings, actual validation or NOT RUN,
open decisions, and approval status. Keep full evidence in the artifact; avoid
duplicating it in chat. NEXT AUTHORIZED ACTION: USER REVIEW. STOPPED: YES.
```

## Human review checklist

- [ ] The intended change locations are explicit.
- [ ] New functionality is distinguished from behavior already available.
- [ ] Interfaces and risks are proportional to the story.
- [ ] A proposed waiver is not treated as automatic permission to skip a gate.
- [ ] Output path, revision, and approval conditions are correct.

## Copy approval only after reviewing

```text
APPROVED BY USER
STORY / PHASE: <RALLY-ID> / 3
ARTIFACT PATH / CONTENT REVISION: <STORY-DIR>/03-design-decision.md / <exact SHA-256 or immutable revision>
INPUT BASELINE: <requirements revision and relevant code baseline; NOT ASSESSED for code in requirements-only phases>
CONDITIONS: NONE
APPROVAL RECORD WRITE: <STORY-DIR>/approvals.md; append this decision only
NEXT-PHASE AUTHORIZATION: NONE
Do not change the approved artifact, source, or external systems.
Record this human decision, acknowledge, and stop.
```

If changes are needed, use [the revision pattern](Approvals-and-Handoffs.md). Approval does not execute the next phase.

**Navigation:** [Previous](Phase-2-Codebase-Discovery.md) · [Workflow index](Developer-Workflow.md) · [Next page](Phase-4-Implementation-Planning.md)
