# Phase 1B — Review requirements

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

Challenge clarity and testability before investing in implementation discovery.

**Lead:** John / Product Manager  
**Recommended model : Claude Sonnet 5**

## Inputs

Original Rally revision/snapshot; approved 01-requirements-analysis.md and its approval record. Supply exact paths and revisions.

## Output

`<STORY-DIR>/01b-requirements-readiness-review.md`. Replace the story directory and any unit/review identifier before pasting. Preserve existing approved records; substantive revisions require renewed approval.

## Copy the authorization and phase prompt

Fill every placeholder. This block grants only its listed actions under the master. Keep the explanatory page outside the copied prompt.

```text
Apply the previously supplied BMAD master contract. Perform only this phase.
If the master or a required value is missing, stop before substantive work.

STORY / WORKSPACE: <RALLY-ID> / <repository or worktree>
PHASE / UNIT: 1B
PHASE AUTHORIZED: YES
PRIMARY ROLE: John / Product Manager
Recommended model : Claude Sonnet 5
SELECTED MODEL / BASIS: <actual selection; host-confirmed, user-reported, or unverified>
EXECUTION METHOD: Enterprise procedure EP-1B below; not an automatic native workflow invocation.
APPROVED INPUTS / REVISIONS: <resolve the inputs listed on this page>
ALLOWED READS: Named requirements inputs, approval record, project instructions, and BMAD configuration/skill metadata. No application-code investigation.
ARTIFACT MODE: WORKSPACE
EXPECTED OUTPUT / ALLOWED ARTIFACT WRITES: <STORY-DIR>/01b-requirements-readiness-review.md only
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
1. Compare the approved interpretation with original Rally intent, including scope and exclusions.
2. For each AC, assess clarity, observable success, error/edge conditions, dependencies, and conflicts. Label missing detail as a question rather than inventing behavior.
3. Classify unresolved questions by whether they block discovery, design, or implementation. Requirements readiness is not technical implementation readiness.
4. Return READY FOR DISCOVERY, READY WITH NONBLOCKING QUESTIONS, or NOT READY, with evidence and proposed clarifications.
5. Write only the review artifact. Do not rewrite Rally or the approved requirements. Requirement changes return to Phase 1 and human approval.

HANDOFF
Return artifact path/revision, baseline, key findings, actual validation or NOT RUN,
open decisions, and approval status. Keep full evidence in the artifact; avoid
duplicating it in chat. NEXT AUTHORIZED ACTION: USER REVIEW. STOPPED: YES.
```

## Human review checklist

- [ ] The review compares against the original source.
- [ ] Every blocking question has a clear owner/decision needed.
- [ ] The readiness label does not imply the codebase is understood.
- [ ] Output path, revision, and approval conditions are correct.

## Copy approval only after reviewing

```text
APPROVED BY USER
STORY / PHASE: <RALLY-ID> / 1B
ARTIFACT PATH / CONTENT REVISION: <STORY-DIR>/01b-requirements-readiness-review.md / <exact SHA-256 or immutable revision>
INPUT BASELINE: <requirements revision and relevant code baseline; NOT ASSESSED for code in requirements-only phases>
CONDITIONS: NONE
APPROVAL RECORD WRITE: <STORY-DIR>/approvals.md; append this decision only
NEXT-PHASE AUTHORIZATION: NONE
Do not change the approved artifact, source, or external systems.
Record this human decision, acknowledge, and stop.
```

If changes are needed, use [the revision pattern](Approvals-and-Handoffs.md). Approval does not execute the next phase.

**Navigation:** [Previous](Phase-1-Story-Understanding.md) · [Workflow index](Developer-Workflow.md) · [Next page](Phase-2-Codebase-Discovery.md)
