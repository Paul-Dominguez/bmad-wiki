# Phase 5 — Implement one approved unit

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

Implement one authorized plan unit with its associated tests and evidence.

**Lead:** Amelia / Developer  
**Recommended model : Claude Sonnet 5**

## Inputs

Approved 04-implementation-plan.md and named unit; referenced approved requirements/design/discovery and approval records; prior unit evidence where required. Supply exact paths/revisions.

## Output

`<STORY-DIR>/05-unit-<UNIT>-implementation-log.md`. Replace the story directory and any unit/review identifier before pasting. Preserve existing approved records; substantive revisions require renewed approval.

## Copy the authorization and phase prompt

Fill every placeholder. This block grants only its listed actions under the master. Keep the explanatory page outside the copied prompt.

```text
Apply the previously supplied BMAD master contract. Perform only this phase.
If the master or a required value is missing, stop before substantive work.

STORY / WORKSPACE: <RALLY-ID> / <repository or worktree>
PHASE / UNIT: 5
AUTHORIZED UNIT: <UNIT from approved plan>

PHASE AUTHORIZED: YES
PRIMARY ROLE: Amelia / Developer
Recommended model : Claude Sonnet 5
SELECTED MODEL / BASIS: <actual selection; host-confirmed, user-reported, or unverified>
EXECUTION METHOD: Enterprise procedure EP-5 below; not an automatic native workflow invocation.
APPROVED INPUTS / REVISIONS: <resolve the inputs listed on this page>
ALLOWED READS: Named inputs and approvals; relevant source/tests/configuration, project instructions, existing diff/baseline, and BMAD configuration/skill metadata.
ARTIFACT MODE: WORKSPACE
EXPECTED OUTPUT / ALLOWED ARTIFACT WRITES: <STORY-DIR>/05-unit-<UNIT>-implementation-log.md only
ALLOWED SOURCE / TEST / CONFIG WRITES: <enumerate exact production, test, and configuration paths for this unit>
ALLOWED COMMANDS / ENVIRONMENT: Read-only file/search/Git status/diff/hash inspection within allowed reads; plus <exact test/build/lint commands from plan and named local/test environment; NONE if not authorized>
ALLOWED RUNTIME OUTPUTS: <exact permitted test/build/cache output paths; NONE if not authorized>
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
1. Verify the named unit, approved inputs, current repository baseline, existing user changes, and exact allowlist before editing. Preserve unrelated work.
2. Recheck the relevant current/newer implementation and wiring against the plan. Stop if new evidence invalidates ownership, design, or authorization; do not treat already planned missing functionality as a blocker.
3. Implement only this unit in the authorized locations, with the associated tests. Establish a reproduction or failing test when appropriate, then verify the behavior. Do not weaken tests to force a pass.
4. If any required production/test/configuration file is missing from the allowlist, stop and request a bounded plan/authorization amendment before touching it.
5. Run only named validation commands in the named environment, allowing only declared runtime outputs. Distinguish observed PASS/FAIL from NOT RUN/BLOCKED and explain impact.
6. Inspect the actual diff for unintended changes, duplication, wrong placement, missing integration, and AC coverage.
7. Write the unit log with baseline, changed paths, decisions, commands/results, remaining failures, and handoff. Do not stage, commit, update tracking/Rally, start another unit, or begin Phase 6.

HANDOFF
Return artifact path/revision, baseline, key findings, actual validation or NOT RUN,
open decisions, and approval status. Keep full evidence in the artifact; avoid
duplicating it in chat. NEXT AUTHORIZED ACTION: USER REVIEW. STOPPED: YES.
```

## Human review checklist

- [ ] Actual diff stays within the approved unit and paths.
- [ ] Associated tests were implemented and results accurately reported.
- [ ] Implementation uses the approved locations and integration points.
- [ ] Log approval is not mistaken for code acceptance.
- [ ] Output path, revision, and approval conditions are correct.

## Copy approval only after reviewing

```text
APPROVED BY USER
STORY / PHASE: <RALLY-ID> / 5
ARTIFACT PATH / CONTENT REVISION: <STORY-DIR>/05-unit-<UNIT>-implementation-log.md / <exact SHA-256 or immutable revision>
INPUT BASELINE: <requirements revision and relevant code baseline; NOT ASSESSED for code in requirements-only phases>
CONDITIONS: NONE
APPROVAL RECORD WRITE: <STORY-DIR>/approvals.md; append this decision only
NEXT-PHASE AUTHORIZATION: NONE
Do not change the approved artifact, source, or external systems.
Record this human decision, acknowledge, and stop.
```

If changes are needed, use [the revision pattern](Approvals-and-Handoffs.md). Approval does not execute the next phase.

**Navigation:** [Previous](Phase-4-Implementation-Planning.md) · [Workflow index](Developer-Workflow.md) · [Next page](Phase-6-Independent-Review.md)
