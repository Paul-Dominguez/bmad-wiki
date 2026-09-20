# Phase 2 — Discover the codebase

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

Locate current behavior and relevant newer foundations before deciding where the change belongs.

**Lead:** Amelia / Developer  
**Recommended model : Claude Sonnet 5**

## Inputs

Approved 01-requirements-analysis.md and 01b-requirements-readiness-review.md, approval records, original Rally revision/snapshot, and repository baseline. Supply exact paths/revisions.

## Output

`<STORY-DIR>/02-current-state-analysis.md`. Replace the story directory and any unit/review identifier before pasting. Preserve existing approved records; substantive revisions require renewed approval.

## Copy the authorization and phase prompt

Fill every placeholder. This block grants only its listed actions under the master. Keep the explanatory page outside the copied prompt.

```text
Apply the previously supplied BMAD master contract. Perform only this phase.
If the master or a required value is missing, stop before substantive work.

STORY / WORKSPACE: <RALLY-ID> / <repository or worktree>
PHASE / UNIT: 2
PHASE AUTHORIZED: YES
PRIMARY ROLE: Amelia / Developer
Recommended model : Claude Sonnet 5
SELECTED MODEL / BASIS: <actual selection; host-confirmed, user-reported, or unverified>
EXECUTION METHOD: Enterprise procedure EP-2 below; not an automatic native workflow invocation.
APPROVED INPUTS / REVISIONS: <resolve the inputs listed on this page>
ALLOWED READS: Named inputs and approvals; relevant repository files, history/diff, project instructions, BMAD configuration/skill metadata; dependencies within the authorized workspace.
ARTIFACT MODE: WORKSPACE
EXPECTED OUTPUT / ALLOWED ARTIFACT WRITES: <STORY-DIR>/02-current-state-analysis.md only
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
1. Trace affected entry points, routes/actions, callers, registrations, services, data contracts, flags, and existing tests. Start with targeted search and expand for evidence gaps.
2. Search beyond the first legacy path. Identify relevant newer, partial, disabled, or disconnected implementations in the permitted codebase. Record the search scope and evidence; NOT FOUND is not proof of absence.
3. For each AC/capability, record current behavior; relevant existing/newer files and symbols; supported behavior; missing behavior; reusable foundations; and uncertainty.
4. Identify candidate implementation locations and any existing approved ownership decision. Describe technical constraints and risks, but leave unresolved design decisions for Phase 3.
5. Explain the integration path between legacy entry points and newer code when relevant. Do not assume a separate repository, a complete new app, or that every story is a redirect.
6. Write an evidence-backed implementation map and focused design questions. Do not modify source/tests/configuration, execute the app, run tests, or prescribe unapproved design.

HANDOFF
Return artifact path/revision, baseline, key findings, actual validation or NOT RUN,
open decisions, and approval status. Keep full evidence in the artifact; avoid
duplicating it in chat. NEXT AUTHORIZED ACTION: USER REVIEW. STOPPED: YES.
```

## Human review checklist

- [ ] Both legacy and relevant newer code were investigated.
- [ ] File/symbol references support behavior claims.
- [ ] Known capability, missing capability, and uncertainty are separate.
- [ ] The map is sufficient to decide ownership without silently choosing the old location.
- [ ] Output path, revision, and approval conditions are correct.

## Copy approval only after reviewing

```text
APPROVED BY USER
STORY / PHASE: <RALLY-ID> / 2
ARTIFACT PATH / CONTENT REVISION: <STORY-DIR>/02-current-state-analysis.md / <exact SHA-256 or immutable revision>
INPUT BASELINE: <requirements revision and relevant code baseline; NOT ASSESSED for code in requirements-only phases>
CONDITIONS: NONE
APPROVAL RECORD WRITE: <STORY-DIR>/approvals.md; append this decision only
NEXT-PHASE AUTHORIZATION: NONE
Do not change the approved artifact, source, or external systems.
Record this human decision, acknowledge, and stop.
```

If changes are needed, use [the revision pattern](Approvals-and-Handoffs.md). Approval does not execute the next phase.

**Navigation:** [Previous](Phase-1B-Requirements-Review.md) · [Workflow index](Developer-Workflow.md) · [Next page](Phase-3-Design.md)
