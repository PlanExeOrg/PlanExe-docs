# PlanExe Documentation

This repository contains the built documentation for [PlanExe](https://planexe.org), hosted on GitHub Pages at [docs.planexe.org](https://docs.planexe.org).

## Overview

The documentation source files are maintained in the main [PlanExe repository](https://github.com/PlanExeOrg/PlanExe) in the `docs` directory. This repository contains the compiled output from MkDocs Material, which is automatically deployed to GitHub Pages.

## Architecture

- **Source**: [PlanExeOrg/PlanExe/docs](https://github.com/PlanExeOrg/PlanExe/tree/main/docs)
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
   
   # Clone the PlanExe repo (adjust path as needed)
   git clone https://github.com/PlanExeOrg/PlanExe.git ../PlanExe
   ```

4. Build the documentation:
   ```bash
   python build.py
   ```

   Or manually:
   ```bash
   # Copy docs from PlanExe repo
   cp -r ../PlanExe/docs/* docs/
   
   # Build
   mkdocs build
   ```

5. Preview locally:
   ```bash
   python serve.py
   ```
   Then open http://127.0.0.1:18525 in your browser.

### Custom Build Paths

If your PlanExe repo is in a different location:

```bash
PLANEXE_REPO=/path/to/PlanExe DOCS_SOURCE_DIR=docs python build.py
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

**Why doesn’t the site rebuild when I push docs changes in PlanExe?**

The docs site is built and deployed from **this** repo (PlanExe-docs). Pushing to the **PlanExe** repo does not run workflows here. Rebuilds happen when:

1. **Someone pushes to `main` on PlanExe-docs** (this repo), or  
2. **Someone manually runs** the “Deploy Documentation” workflow in PlanExe-docs (Actions → Deploy Documentation → Run workflow), or  
3. **The PlanExe repo triggers a rebuild** when `docs/` changes on `main`.

For (3), the [PlanExe repo](https://github.com/PlanExeOrg/PlanExe) has a workflow (`.github/workflows/docs-update.yml`) that sends a `repository_dispatch` to this repo when files under `docs/` change. For that to work you must configure a secret in the **PlanExe** repo named **`PLANEXE_DOCS_DISPATCH_TOKEN`** (PlanExe → Settings → Secrets and variables → Actions).

**Token value:** use a GitHub Personal Access Token that can trigger workflows in this repo. A **fine-grained** token is recommended (narrower permissions). Fine-grained tokens have a **maximum expiration of 1 year**, so the secret must be renewed annually.

**Create or renew the fine-grained token:**

1. Go to [GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens](https://github.com/settings/tokens?type=beta).
2. **Generate new token** (or open an existing one to regenerate/check expiry).
3. **Token name:** e.g. `PlanExe docs dispatch`.
4. **Expiration:** set the maximum (1 year); add a calendar reminder to renew before it expires.
5. **Resource owner:** your user or the org that owns PlanExe.
6. **Repository access:** Only select repositories → choose **PlanExeOrg/PlanExe-docs**.
7. **Permissions → Repository permissions:** set **Actions** to **Read and write** (needed to trigger the deploy workflow).
8. Generate the token, copy it (it is shown only once), then in the **PlanExe** repo update the **`PLANEXE_DOCS_DISPATCH_TOKEN`** secret with this value.

**Alternative:** a [classic PAT](https://github.com/settings/tokens) with **`repo`** scope also works and can have a longer or no expiration.

If the secret is missing or expired, the “Notify docs deploy” job in PlanExe will fail and the site will not rebuild. Check the [PlanExe Actions](https://github.com/PlanExeOrg/PlanExe/actions) tab after pushing docs changes. Until the token is set, use option (2) and manually run “Deploy Documentation” in PlanExe-docs after merging docs changes.

## Configuration

The MkDocs configuration is in `mkdocs.yml`. Key settings:

- **Site URL**: https://docs.planexe.org
- **Theme**: Material for MkDocs
- **Source**: Points to PlanExe repo's `docs` directory

## Contributing

To contribute to the documentation:

1. Edit files in the [PlanExe repository's `docs` directory](https://github.com/PlanExeOrg/PlanExe/tree/main/docs)
2. Build and test locally using the instructions above
3. Submit a pull request to the PlanExe repository
4. After merging, rebuild and deploy to this repository

## License

MIT License - see [LICENSE](LICENSE) file.
