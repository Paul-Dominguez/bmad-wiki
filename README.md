# bmad-wiki

Personal sandbox for testing BMAD wiki documentation, role guides, and developer workflows.

## Start here

**[Open the BMAD handbook](wiki/Home.md)**

- [Installation](wiki/Installation.md)
- [Agents](wiki/Agents.md)
- [Agile role guides and trial prompts](wiki/Role-Guides.md)
- [Master template](wiki/Master-Template.md)
- [Developer workflow](wiki/Developer-Workflow.md)
- [Model and credit guidance](wiki/Models-and-Credit-Efficiency.md)

The handbook contains 25 content pages plus sidebar and footer files. It targets BMAD 6.12.0 and remains a draft for team trials.

## Repository documentation and GitHub Wiki

The Markdown pages are readable directly in this private repository. GitHub was not retaining the Wiki feature as enabled at import time; the separate Wiki has not been published.

Private Wikis require a supported paid GitHub plan. See [GitHub Wiki availability](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis). Repository visibility remains private.

## Edit and export

Edit the pages in `wiki/`. Internal links use `.md` so navigation works in the repository.

Run `python tools/export_wiki.py` to validate local page links and regenerate [BMAD-GitHub-Wiki.zip](BMAD-GitHub-Wiki.zip). The export converts internal links to GitHub Wiki routes and places all pages at the archive root.

Once the separate Wiki is available, create its initial Home page, clone its `.wiki.git` repository, reconcile the exported files with any existing pages, and publish through the normal Git workflow. Do not copy repository-formatted pages directly without converting their links.

No BMAD installation or application workflow is executed by these documentation files.
