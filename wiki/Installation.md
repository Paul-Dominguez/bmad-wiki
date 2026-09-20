# Install BMAD

[Home](Home.md) · [Developer workflow](Developer-Workflow.md)

**Status:** Draft for team review | **BMAD baseline:** 6.12.0 | **Reviewed:** September 20, 2026

## Purpose

Use the normal BMAD installer. This wiki targets **6.12.0**; the unversioned command can install a newer release. Run setup from the application project directory, not the wiki repository.

## Prerequisites

- Node.js 20.12 or later and npm/npx.
- Your supported AI coding tool, such as the team's GitHub Copilot host.
- Git when installing external or custom Git-hosted modules.
- `uv` for skills that require its Python runtime, including Build. Missing `uv` may allow installation to finish while leaving those skills unusable.

## Installation steps

1. Open a terminal in the target project and inspect existing changes with `git status` if it is a Git repository.
2. Run the standard interactive installer:

```shell
npx bmad-method install
```

For this wiki's exact version baseline, use:

```shell
npx bmad-method@6.12.0 install
```

3. Select the BMad Method module (**BMM**), the target directory, and the supported Copilot integration offered by the installer. Configure language and artifact locations as prompted. Add other modules only when needed.
4. Review the success summary and warnings. Check the generated files and configured version; do not infer the version from this wiki.
5. Open the project in your AI tool and invoke `bmad-help` using its supported skill mechanism. This verification is setup work, not story-phase authorization.

The installer places shared configuration under `_bmad` and skills in the selected tool's integration location. [6.12.0 installation reference](https://github.com/bmad-code-org/BMAD-METHOD/blob/v6.12.0/docs/start/install-bmad.md)

## When the expected tool is not offered

Inspect the supported list and help for the same package version:

```shell
npx bmad-method@6.12.0 install --list-tools
npx bmad-method@6.12.0 install --help
```

Do not guess an integration ID. If required runtime or access is missing, resolve it through the team's normal setup process. Commands here are documentation; producing this wiki did not install anything.

## Updating later

Rerun the appropriate version of the installer from the project and inspect its update/reconfiguration choices. A deliberate version upgrade should trigger review of this wiki's execution profiles. [Current installation guide](https://docs.bmad-method.org/start/install-bmad/)

**Next:** [Master template](Master-Template.md).
