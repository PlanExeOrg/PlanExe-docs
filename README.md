# PlanExe Documentation

This repository contains the built documentation for [PlanExe](https://planexe.org), hosted on GitHub Pages at [docs.planexe.org](https://docs.planexe.org).

## Overview

The documentation source files are maintained in the [PlanExe2 repository](https://github.com/PlanExeOrg/PlanExe2) in the `docs/website/` directory. Only that directory is published; the rest of `PlanExe2/docs/` is internal. This repository contains the build configuration; MkDocs Material output is deployed to GitHub Pages.

The PlanExe v1 documentation is no longer published here; it remains readable in [PlanExe/docs](https://github.com/PlanExeOrg/PlanExe/tree/main/docs).

## Architecture

- **Source**: [PlanExeOrg/PlanExe2/docs/website](https://github.com/PlanExeOrg/PlanExe2/tree/main/docs/website)
- **Build Tool**: MkDocs Material
- **Output**: This repository (deployed to GitHub Pages)
- **Domain**: docs.planexe.org

## Local Development

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Clone both repositories:
   ```bash
   # Clone this repo
   git clone https://github.com/PlanExeOrg/PlanExe-docs.git
   cd PlanExe-docs
   
   # Clone the PlanExe2 repo (adjust path as needed)
   git clone https://github.com/PlanExeOrg/PlanExe2.git ../PlanExe2
   ```

4. Build the documentation:
   ```bash
   python build.py
   ```

   Or manually:
   ```bash
   # Copy docs from PlanExe2 repo
   cp -r ../PlanExe2/docs/website/* docs/
   
   # Build
   mkdocs build
   ```

5. Preview locally:
   ```bash
   python serve.py
   ```
   Then open http://127.0.0.1:18525 in your browser.

### Custom Build Paths

If your PlanExe2 repo is in a different location:

```bash
PLANEXE_REPO=/path/to/PlanExe2 DOCS_SOURCE_DIR=docs/website python build.py
```

## Deployment

### Manual Deployment

1. Build the documentation:
   ```bash
   python build.py
   ```

2. Copy the `site/` directory contents to the repository root:
   ```bash
   cp -r site/* .
   ```

3. Commit and push:
   ```bash
   git add .
   git commit -m "Update documentation"
   git push
   ```

### Automated Deployment

See `.github/workflows/deploy.yml` for GitHub Actions automation.

**Why doesn’t the site rebuild when I push docs changes in PlanExe2?**

The docs site is built and deployed from **this** repo (PlanExe-docs). Pushing to **PlanExe2** does not run workflows here. Rebuilds happen when:

1. **Someone pushes to `main` on PlanExe-docs** (this repo), or
2. **Someone manually runs** the “Deploy Documentation” workflow in PlanExe-docs (Actions → Deploy Documentation → Run workflow), or
3. **A `repository_dispatch` of type `docs-updated`** is sent to this repo.

PlanExe2 has no workflow that sends (3) yet, so after merging docs changes in PlanExe2, use (2). To automate it, add a workflow to PlanExe2 that sends the dispatch when `docs/website/**` changes on `main`, with a secret named **`PLANEXE_DOCS_DISPATCH_TOKEN`** (PlanExe2 → Settings → Secrets and variables → Actions). The PlanExe v1 repo has such a workflow (`.github/workflows/docs-update.yml`) that can be used as a template; while it is active, v1 docs changes also trigger a (harmless) rebuild of this site.

**Token value:** use a GitHub Personal Access Token that can trigger workflows in this repo. A **fine-grained** token is recommended (narrower permissions). Fine-grained tokens have a **maximum expiration of 1 year**, so the secret must be renewed annually.

**Create or renew the fine-grained token:**

1. Go to [GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens](https://github.com/settings/tokens?type=beta).
2. **Generate new token** (or open an existing one to regenerate/check expiry).
3. **Token name:** e.g. `PlanExe docs dispatch`.
4. **Expiration:** set the maximum (1 year); add a calendar reminder to renew before it expires.
5. **Resource owner:** your user or the org that owns PlanExe2.
6. **Repository access:** Only select repositories → choose **PlanExeOrg/PlanExe-docs**.
7. **Permissions → Repository permissions:** set **Contents** to **Read and write** (required for the `repository_dispatch` API; Actions alone is not enough).
8. Generate the token, copy it (it is shown only once), then in the source repo update the **`PLANEXE_DOCS_DISPATCH_TOKEN`** secret with this value.

**Alternative:** a [classic PAT](https://github.com/settings/tokens) with **`repo`** scope also works and can have a longer or no expiration.

If the secret is missing or expired, the “Notify docs deploy” job in the source repo will fail and the site will not rebuild. Until then, use option (2).

**Troubleshooting deployment**

The main place to check is the **PlanExe-docs Actions** page: **[github.com/PlanExeOrg/PlanExe-docs/actions](https://github.com/PlanExeOrg/PlanExe-docs/actions)**. There you can see all workflow runs: “Deploy Documentation” (builds the site and deploys to GitHub Pages) and “pages build and deployment” (GitHub’s Pages publish). Runs triggered by a docs change in PlanExe show the event **docs-updated** and “Repository dispatch triggered by …”. Use this page to confirm a deploy ran, re-run a failed workflow, or manually start “Deploy Documentation” (Actions → Deploy Documentation → Run workflow).

- **Site didn’t update after pushing to PlanExe2/docs/website?** Open the [PlanExe-docs Actions](https://github.com/PlanExeOrg/PlanExe-docs/actions) page. If there is no “Deploy Documentation” run for your push, the trigger from PlanExe likely failed — check the [PlanExe Actions](https://github.com/PlanExeOrg/PlanExe/actions) tab: a failed “Notify docs deploy” job will show the API error (e.g. token missing **Contents: Read and write**). If “Deploy Documentation” ran but failed, open that run and fix the error shown in the logs. If it succeeded, wait a minute or two for GitHub Pages to update and try a hard refresh (Ctrl+Shift+R / Cmd+Shift+R) or a private window to avoid cache.
- **“Notify docs deploy” succeeded in PlanExe, but no “Deploy Documentation” run appears in PlanExe-docs?** The dispatch API may have rejected the request (e.g. 403). Fine-grained tokens need **Contents: Read and write** on PlanExe-docs; **Actions** alone is not enough. Update the token with that permission and update **`PLANEXE_DOCS_DISPATCH_TOKEN`** in the PlanExe repo. After the change, the PlanExe workflow fails the job and prints the API response when the dispatch is rejected, so the exact error will appear in [PlanExe Actions](https://github.com/PlanExeOrg/PlanExe/actions).

## Configuration

The MkDocs configuration is in `mkdocs.yml`. Key settings:

- **Site URL**: https://docs.planexe.org
- **Theme**: Material for MkDocs
- **Source**: Points to PlanExe2 repo's `docs/website` directory

## Contributing

To contribute to the documentation:

1. Edit files in the [PlanExe2 repository's `docs/website` directory](https://github.com/PlanExeOrg/PlanExe2/tree/main/docs/website)
2. Build and test locally using the instructions above
3. Submit a pull request to the PlanExe2 repository
4. After merging, rebuild and deploy to this repository

## License

MIT License - see [LICENSE](LICENSE) file.
