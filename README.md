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
