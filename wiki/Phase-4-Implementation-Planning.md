# Phase 4 — Plan changes and tests

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

Turn approved decisions into bounded, testable implementation units.

**Lead:** Amelia / Developer  
**Recommended model : Claude Sonnet 5**

## Inputs

Approved requirements, readiness review, discovery map, 03-design-decision.md (or approved waiver), and approval records. Supply exact paths/revisions.

## Output

`<STORY-DIR>/04-implementation-plan.md`. Replace the story directory and any unit/review identifier before pasting. Preserve existing approved records; substantive revisions require renewed approval.

## Copy the authorization and phase prompt

Fill every placeholder. This block grants only its listed actions under the master. Keep the explanatory page outside the copied prompt.

```text
Apply the previously supplied BMAD master contract. Perform only this phase.
If the master or a required value is missing, stop before substantive work.

STORY / WORKSPACE: <RALLY-ID> / <repository or worktree>
PHASE / UNIT: 4
PHASE AUTHORIZED: YES
PRIMARY ROLE: Amelia / Developer
Recommended model : Claude Sonnet 5
SELECTED MODEL / BASIS: <actual selection; host-confirmed, user-reported, or unverified>
EXECUTION METHOD: Enterprise procedure EP-4 below; not an automatic native workflow invocation.
APPROVED INPUTS / REVISIONS: <resolve the inputs listed on this page>
ALLOWED READS: Named inputs and approvals; relevant source/tests/configuration and repository validation instructions; BMAD configuration/skill metadata.
ARTIFACT MODE: WORKSPACE
EXPECTED OUTPUT / ALLOWED ARTIFACT WRITES: <STORY-DIR>/04-implementation-plan.md only
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
1. Verify the relevant source still supports the approved design. Report changes affecting assumptions or ownership before planning dependent work.
2. Split work into coherent testable units with stable unit IDs, order/dependencies, AC coverage, and completion criteria. Identify any intermediate state that cannot yet satisfy full-story acceptance.
3. For each unit list exact existing/proposed production, test, and configuration paths, the intended change, reuse/extension decision, and explicitly excluded areas. No vague permission to edit whatever is needed.
4. Pair behavior changes with associated tests. Specify relevant unit/integration/regression checks, expected results, executable commands, environment, and generated runtime-output paths.
5. Include tests for relevant wiring, newer implementation behavior, legacy behavior that must remain, and required error cases. Do not prescribe tests that merely mirror implementation.
6. Define the pre-edit verification, stop conditions, evidence handoff, and review scope for each unit. If a needed file or permission is unknown, resolve it or mark the unit not ready.
7. Write only the plan. Do not begin implementation or run a native Build route that could cross the planning gate.

HANDOFF
Return artifact path/revision, baseline, key findings, actual validation or NOT RUN,
open decisions, and approval status. Keep full evidence in the artifact; avoid
duplicating it in chat. NEXT AUTHORIZED ACTION: USER REVIEW. STOPPED: YES.
```

## Human review checklist

- [ ] Every AC maps to units and verification.
- [ ] Production, test, and configuration paths are enumerated.
- [ ] Newer-code ownership survives into the actual edit plan.
- [ ] Commands and runtime effects are bounded and units have explicit readiness.
- [ ] Output path, revision, and approval conditions are correct.

## Copy approval only after reviewing

```text
APPROVED BY USER
STORY / PHASE: <RALLY-ID> / 4
ARTIFACT PATH / CONTENT REVISION: <STORY-DIR>/04-implementation-plan.md / <exact SHA-256 or immutable revision>
INPUT BASELINE: <requirements revision and relevant code baseline; NOT ASSESSED for code in requirements-only phases>
CONDITIONS: NONE
APPROVAL RECORD WRITE: <STORY-DIR>/approvals.md; append this decision only
NEXT-PHASE AUTHORIZATION: NONE
Do not change the approved artifact, source, or external systems.
Record this human decision, acknowledge, and stop.
```

If changes are needed, use [the revision pattern](Approvals-and-Handoffs.md). Approval does not execute the next phase.

**Navigation:** [Previous](Phase-3-Design.md) · [Workflow index](Developer-Workflow.md) · [Next page](Phase-5-Implementation.md)
