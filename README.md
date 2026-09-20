# bmad-wiki

Personal sandbox for testing BMAD wiki documentation, role guides, and developer workflows.

## Start here

**[Open the BMAD Wiki](https://github.com/Paul-Dominguez/bmad-wiki/wiki)**

- [Installation](wiki/Installation.md)
- [Agents](wiki/Agents.md)
- [Agile role guides and trial prompts](wiki/Role-Guides.md)
- [Master template](wiki/Master-Template.md)
- [Developer workflow](wiki/Developer-Workflow.md)
- [Model and credit guidance](wiki/Models-and-Credit-Efficiency.md)

The handbook contains 25 content pages plus sidebar and footer files. It targets BMAD 6.12.0 and remains a draft for team trials.

## Repository documentation and GitHub Wiki

The handbook is published in the [GitHub Wiki](https://github.com/Paul-Dominguez/bmad-wiki/wiki). This repository is public and retains the Markdown source pages in `wiki/` for review and maintenance.

## Edit and export

Edit the pages in `wiki/`. Internal links use `.md` so navigation works in the repository.

Run `python tools/export_wiki.py` to validate local page links and regenerate [BMAD-GitHub-Wiki.zip](BMAD-GitHub-Wiki.zip). The export converts internal links to GitHub Wiki routes and places all pages at the archive root.

To update the live Wiki, clone `https://github.com/Paul-Dominguez/bmad-wiki.wiki.git`, reconcile the exported files with any existing pages, and commit and push to its `master` branch. Do not copy repository-formatted pages directly without converting their links.

No BMAD installation or application workflow is executed by these documentation files.
