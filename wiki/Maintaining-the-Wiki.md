# Maintaining this wiki

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Ownership and status

Assign a team maintainer before enterprise rollout. Keep the master and phase cards under review together. The wiki is the proposed daily-use source; earlier Word and Markdown drafts are historical inputs and should not be mixed into current prompts.

This edition converts the research and developer template into a navigable handbook and newly aligned phase cards. The documentation is stored in this repository. Importing it does not install BMAD, run any phase, or modify application code. The source Word document remains unchanged.

## Structure decisions

- Home introduces BMAD and links the contents.
- Installation is separate from everyday story execution.
- Agents explains specialist roles and their best uses; it is reference material, not another runtime prompt.
- Master contains the stable session contract.
- Developer Workflow is an index; each phase is its own page with one bounded prompt.
- Shared approval, budget, and troubleshooting guidance is kept out of copied prompts.
- Role Guides provides seven job-specific learning pages with agent selection and bounded trial prompts. These are separate starters; complete production workflows for those roles can be developed without changing developer permissions.

## Pilot before rollout

Use a disposable repository and synthetic Rally snapshot to verify:

1. Master alone performs no tools or writes.
2. Unresolved card placeholders and mismatched approvals stop before substantive work.
3. Artifact-only phases write only their named outputs.
4. Discovery finds both a legacy path and a partially implemented newer path.
5. The design and plan preserve intended implementation ownership.
6. An unlisted test file stops implementation until scope is amended.
7. Native workflow behavior cannot bypass the gate, stage/commit, or mutate tracking unexpectedly.
8. Review produces findings without fixes; failed/unrun checks are not reported as passed.
9. New sessions restore progress without repeating completed work.
10. Model changes preserve inputs and gates, and Astra is excluded.

Record host, version, profiles, outputs, and observed deviations. Structural checks on the wiki are not execution tests of these scenarios.

Pilot each role starter separately: confirm agent activation uses the approved setup, then verify the trial produces only a chat draft, distinguishes fixture facts from proposals, and makes no tool calls or file/external changes after the trial prompt is supplied. Check that unknowns remain unknown and that human product, team, and release decisions are not invented.

## Changes requiring review

Review the installation page and execution profiles after a BMAD version change. Review model choices and budget guidance when pricing, available models, or measured quality changes. Review the entire approval chain when a shared field or artifact name changes.

For a lightweight change log, record date, changed pages, reason, and validation result. Do not place changing release notes inside the runtime master.

## Publishing to GitHub Wiki

Create the initial Home page in the target repository's Wiki if it has none. Clone its separate wiki Git repository, review existing content, and copy these Markdown pages into it. Review the diff before committing and pushing to the wiki's default branch. The source repository is Paul-Dominguez/bmad-wiki. Its separate Wiki must be available and initialized before publishing there. [GitHub wiki editing](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages)

Keep `_Sidebar.md` and `_Footer.md` alongside the pages. GitHub uses these for shared navigation. Repository pages use `.md` links. The export script removes that extension from internal links for the separate GitHub Wiki. [GitHub navigation files](https://docs.github.com/en/communities/documenting-your-project-with-wikis/creating-a-footer-or-sidebar-for-your-wiki)

For team review requiring pull requests, maintain the proposed wiki content in an ordinary repository and publish an accepted snapshot to the wiki repository using the team's process. Do not assume a local draft is already live.
