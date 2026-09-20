# Troubleshooting

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

| Symptom | Next action |
| --- | --- |
| Agent implements in the legacy area | Return to Phase 2 evidence and Phase 3 ownership. Confirm the plan names the newer files and the permitted legacy integration edits. |
| Newer implementation cannot be found | Record search scope, inspect routing/imports/registrations/tests, and ask for a pointer if access or evidence remains incomplete. Do not equate not found with nonexistent. |
| Newer code exists but is incomplete | Identify the missing capability and plan it in the approved location. Do not force reuse or assume all new code is duplication. |
| Rally cannot be accessed | Supply an approved versioned story snapshot or restore approved access. Do not invent requirements. |
| Skill is absent or activation fails | Check installation, runtime, and host integration. Report actual availability; do not simulate BMAD execution. |
| Native workflow wants to commit or update tracking | Stop before the conflict. Use a tested bounded enterprise procedure or explicitly change the relevant permissions. |
| Review wants to apply fixes | Keep the report-only boundary. Authorize a separate correction unit after deciding which findings to address. |
| A necessary test file is not in the allowlist | Revise and approve the plan/authorization before creating it. |
| Approved artifact hash no longer matches | Identify the changed content and reassess the affected approval. Do not silently retain APPROVED status. |
| New session repeats completed work | Supply the approved handoff and exact next unit; verify state during authorized preparation. |
| Model dropdown does not show the recommendation | Select another enterprise-approved model, excluding Astra, and record actual selection. Do not assert availability from the wiki. |
| Usage is higher than expected | Inspect context rereads, long outputs, repeated tool loops, and rework before removing useful discovery. Use actual usage reports. |

If blocked, report the evidence, affected artifact/AC, decision needed, and bounded next action. Do not broaden permissions to repair setup or implementation automatically.
