# Approvals and handoffs

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Three different decisions

| Decision | What it means |
| --- | --- |
| Phase authorization | Permission to perform the specified work within the stated boundaries |
| Artifact approval | Human acceptance of exact content and its conditions; no next-phase execution |
| Delivery authorization | Separate permission for specified Git, PR, deployment, or external-system actions |

## Approve an artifact

Each phase page includes a ready-to-fill approval block. Obtain the content revision from the phase handoff, review that exact artifact, and replace every placeholder. Store approval in a separate append-only ledger so recording it does not change the approved artifact's hash.

```text
APPROVED BY USER
STORY / PHASE: <RALLY-ID> / <PHASE>
ARTIFACT PATH / CONTENT REVISION: <path> / <SHA-256 or immutable revision>
INPUT BASELINE: <Rally revision and relevant repository baseline>
CONDITIONS: NONE
APPROVAL RECORD WRITE: <STORY-DIR>/approvals.md; append this decision only
NEXT-PHASE AUTHORIZATION: NONE
Do not change the approved artifact or execute the next phase. Record the
human decision, acknowledge, and stop.
```

Use `APPROVAL RECORD WRITE: NONE` only when the approval already has a durable external record or no cross-session handoff depends on it. The agent records your decision; its text is not independent proof of approver identity. Follow the team's established review/audit system.

## Request changes instead

```text
CHANGES REQUIRED
STORY / PHASE: <RALLY-ID> / <PHASE>
ARTIFACT / REVIEWED REVISION: <path> / <revision>
REQUIRED REVISIONS: <specific changes>
ALLOWED READS / COMMANDS: <bounded evidence inspection>
ALLOWED WRITES: <artifact path only>
All other permissions remain unchanged. Return a new draft revision and
explain the delta. Do not label it approved or begin another phase.
```

A request to revise an artifact does not authorize source changes. If findings invalidate an earlier requirement or design, revise and reapprove affected inputs before dependent implementation.

## Continue in a new chat

1. Paste the master with `SESSION: CONTINUE` and the prior handoff reference.
2. Wait for initialization acknowledgment.
3. Paste the current phase/unit authorization with approved artifact and ledger references.
4. During authorized preparation, the agent verifies the revisions, workspace, conditions, and relevant source changes, then continues only the named work.

Do not reapprove unchanged artifacts solely because the model or chat changed. Do reassess approvals when their content or relevant inputs change. Do not overwrite accepted records while pretending their old approvals still apply.

## Handoff contents

Include story and phase/unit, result status, artifact paths/revisions, requirement and code baseline, key decisions, implementation ownership, verification results, unresolved questions, approval status, and next step. Keep it concise and reference evidence rather than repeating it.

If a durable handoff file is needed, add its exact path to the current card's allowed artifact writes before execution. Otherwise handoff remains in chat and must be provided as a versioned snapshot on resume.

## Acceptance after implementation

Approval of an implementation log acknowledges that record. It is not code acceptance. Phase 6 checks the actual implementation, and human acceptance follows resolution or explicit acceptance of relevant findings. No approval here grants commit, push, PR, deployment, or Rally-update rights.
