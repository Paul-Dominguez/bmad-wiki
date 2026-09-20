# Models and credit efficiency

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Recommended model by phase

| Phase | Field to use |
| --- | --- |
| 1, 1B, 2, 3, 4, 5 | Recommended model : Claude Sonnet 5 |
| 6 | Recommended model : GPT-5.6 Sol |

These are editable recommendations, not BMAD requirements or measured rankings on the team's codebase. Astra is excluded. Use Opus 5 only for a targeted difficult question when the default approach and available evidence leave a material uncertainty. Model escalation cannot supply missing access or make a product decision for a human.

Sonnet is the cost-conscious everyday choice; Sol is a separate reasoning-capable review choice. A model change alone does not make review independent. [Anthropic capabilities](https://www.anthropic.com/claude/sonnet), [OpenAI capabilities](https://developers.openai.com/api/docs/models/gpt-5.6-sol)

## Planning around 50,000 credits and 2–3 features

Suggested allocation: **40,000 working credits + 10,000 reserve**. If this allowance covers the stated workload:

| Features per month | Average working allowance per feature |
| --- | ---: |
| 2 | 20,000 credits |
| 3 | Approximately 13,333 credits |

A feature may contain multiple stories. These are planning allowances, not spending targets or predicted costs. Deduct other work using the same allowance. For a shared pool, include everyone's covered workload. Measure the first completed feature, including corrections and review, then adjust. The allowance's individual/shared scope is still to be confirmed.

## What reduces consumption

1. Paste the master once per session, then only the active phase prompt.
2. Keep research, tutorials, historical chat, and this budget page outside routine prompts.
3. Reuse approved artifacts and verified implementation maps; inspect relevant changes and source needed for the current decision.
4. Search paths and symbols before loading large files. Expand when callers, wiring, newer code, or risks remain unresolved.
5. Produce one complete artifact and a short chat summary. For revisions, show the delta without reproducing all earlier artifacts.
6. Avoid automatic multi-agent discussions, broad repeated investigations, and expensive retries that repeat the same failed approach.
7. Keep acceptance checks, integration evidence, and independent review. Rework caused by a missed implementation area can erase savings from a shorter prompt.

## Billing reference

Copilot prices token usage by model, with separate input, output, and cache categories. At the September 20, 2026 listed rates, Sonnet 5 costs 40% of Opus 5 for the same billed token mix. This is not a promised reduction in total feature cost. [GitHub pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)

Use GitHub's actual usage report rather than estimated response length. Compare credits per accepted feature/story and rework rates. [Per-model token reporting](https://github.blog/changelog/2026-08-11-per-model-token-breakdown-in-the-usage-report/)

Budget controls belong in the organization's Copilot settings. Prompt text cannot enforce the monthly cap, guarantee caching, or confirm an unreported model identity. Recheck model availability and pricing before adopting future defaults.
