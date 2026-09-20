# Phase 6 — Independently review the result

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

Verify the actual implementation against original intent and approved decisions without applying fixes.

**Lead:** Independent reviewer in a separate review session  
**Recommended model : GPT-5.6 Sol**

## Inputs

Original Rally revision/snapshot; approved requirements/design/plan and records; relevant unit logs; exact review baseline and actual diff. Supply exact paths/revisions. For whole-story review include all units.

## Output

`<STORY-DIR>/06-review-<REVIEW-ID>.md`. Replace the story directory and any unit/review identifier before pasting. Preserve existing approved records; substantive revisions require renewed approval.

## Copy the authorization and phase prompt

Fill every placeholder. This block grants only its listed actions under the master. Keep the explanatory page outside the copied prompt.

```text
Apply the previously supplied BMAD master contract. Perform only this phase.
If the master or a required value is missing, stop before substantive work.

STORY / WORKSPACE: <RALLY-ID> / <repository or worktree>
PHASE / UNIT: 6
REVIEW ID / SCOPE / BASELINE: <REVIEW-ID> / <UNIT or WHOLE STORY> / <exact diff baseline>

PHASE AUTHORIZED: YES
PRIMARY ROLE: Independent reviewer in a separate review session
Recommended model : GPT-5.6 Sol
SELECTED MODEL / BASIS: <actual selection; host-confirmed, user-reported, or unverified>
EXECUTION METHOD: Enterprise procedure EP-6 below; not an automatic native workflow invocation.
APPROVED INPUTS / REVISIONS: <resolve the inputs listed on this page>
ALLOWED READS: Named inputs and approvals; actual diff, relevant surrounding source/tests/configuration, registrations/callers, project instructions, and BMAD configuration/skill metadata.
ARTIFACT MODE: WORKSPACE
EXPECTED OUTPUT / ALLOWED ARTIFACT WRITES: <STORY-DIR>/06-review-<REVIEW-ID>.md only
ALLOWED SOURCE / TEST / CONFIG WRITES: NONE
ALLOWED COMMANDS / ENVIRONMENT: Read-only file/search/Git status/diff/hash inspection within allowed reads; plus <exact verification commands and environment; NONE for inspection-only review>
ALLOWED RUNTIME OUTPUTS: <exact permitted verification/cache output paths; NONE if no execution>
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
1. Use a separate review context, not the implementer claiming to become a new persona. Verify original intent, approved inputs, and the exact unit or whole-story baseline.
2. Inspect actual source and diff, including relevant surrounding behavior, rather than relying solely on implementation logs.
3. Trace each in-scope AC to implementation and verification evidence. Check code placement, reuse, wiring to newer implementation, preserved legacy behavior, failure cases, and test quality.
4. Inspect whether tests exercise requirements and integration risks. Run only explicitly authorized commands with declared runtime outputs; otherwise label independent execution NOT RUN and state its effect on confidence.
5. Report findings with severity, file/symbol evidence, affected AC, expected versus actual behavior, and the decision/correction needed. Resolve speculative findings with evidence; do not silently drop them.
6. State VERIFIED, CHANGES REQUIRED, or INCOMPLETE for the named review scope. Whole-story review must cover all ACs and cross-unit integration; a unit pass is not whole-story acceptance.
7. Write only the review report. Do not fix code, update story/tracking/Rally, or run a stock review that mutates unapproved artifacts. Human acceptance and any correction authorization are separate.

HANDOFF
Return artifact path/revision, baseline, key findings, actual validation or NOT RUN,
open decisions, and approval status. Keep full evidence in the artifact; avoid
duplicating it in chat. NEXT AUTHORIZED ACTION: USER REVIEW. STOPPED: YES.
```

## Human review checklist

- [ ] Review uses actual code and original requirements.
- [ ] Scope is explicit: unit or whole story.
- [ ] Findings and unrun checks are visible.
- [ ] No automatic fixes or status updates occurred.
- [ ] Output path, revision, and approval conditions are correct.

## Copy approval only after reviewing

```text
APPROVED BY USER
STORY / PHASE: <RALLY-ID> / 6
ARTIFACT PATH / CONTENT REVISION: <STORY-DIR>/06-review-<REVIEW-ID>.md / <exact SHA-256 or immutable revision>
INPUT BASELINE: <requirements revision and relevant code baseline; NOT ASSESSED for code in requirements-only phases>
CONDITIONS: NONE
APPROVAL RECORD WRITE: <STORY-DIR>/approvals.md; append this decision only
NEXT-PHASE AUTHORIZATION: NONE
Do not change the approved artifact, source, or external systems.
Record this human decision, acknowledge, and stop.
```

If changes are needed, use [the revision pattern](Approvals-and-Handoffs.md). Approval does not execute the next phase.

**Navigation:** [Previous](Phase-5-Implementation.md) · [Workflow index](Developer-Workflow.md) · [Next page](Approvals-and-Handoffs.md)
