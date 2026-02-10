#!/usr/bin/env python3
"""
Build script for PlanExe documentation.
This script builds the docs from the PlanExe repo and outputs to this repo.
"""

import os
import sys
import shutil
import subprocess
import tempfile
from pathlib import Path
import yaml

# ANSI color codes
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
NC = '\033[0m'  # No Color


def print_colored(message: str, color: str = NC):
    """Print a colored message."""
    print(f"{color}{message}{NC}")


def main():
    """Main build function."""
    # Configuration
    planexe_repo = Path(os.environ.get("PLANEXE_REPO", "../PlanExe"))
    docs_source_dir = os.environ.get("DOCS_SOURCE_DIR", "docs")
    output_dir = "site"
    
    print_colored("Building PlanExe documentation...", GREEN)
    
    # Check if PlanExe repo exists
    if not planexe_repo.exists() or not planexe_repo.is_dir():
        print_colored(
            f"Error: PlanExe repo not found at {planexe_repo}",
            RED
        )
        print("Set PLANEXE_REPO environment variable to point to the PlanExe repository")
        sys.exit(1)
    
    # Check if docs source directory exists
    docs_source_path = planexe_repo / docs_source_dir
    if not docs_source_path.exists() or not docs_source_path.is_dir():
        print_colored(
            f"Error: Documentation source directory not found at {docs_source_path}",
            RED
        )
        print("Set DOCS_SOURCE_DIR environment variable if your docs are in a different directory")
        sys.exit(1)
    
    # Get the original directory
    original_dir = Path.cwd()
    mkdocs_yml = original_dir / "mkdocs.yml"
    
    if not mkdocs_yml.exists():
        print_colored(
            f"Error: mkdocs.yml not found in {original_dir}",
            RED
        )
        sys.exit(1)
    
    # Create temporary directory for docs
    with tempfile.TemporaryDirectory() as temp_docs:
        temp_docs_path = Path(temp_docs)
        
        # Create docs subdirectory (mkdocs expects docs_dir by default)
        docs_dir = temp_docs_path / "docs"
        docs_dir.mkdir()
        
        # Copy docs from PlanExe repo into the docs subdirectory
        print_colored(
            f"Copying documentation from {docs_source_path}...",
            YELLOW
        )
        shutil.copytree(docs_source_path, docs_dir, dirs_exist_ok=True)

        # Ensure custom CSS for nav status icons exists (PlanExe-docs override).
        nav_css_path = docs_dir / "assets" / "stylesheets" / "nav-status.css"
        nav_css_path.parent.mkdir(parents=True, exist_ok=True)
        nav_css_path.write_text(
            ".md-nav__link .md-status--proposal { display: none; }\n",
            encoding="utf-8",
        )
        
        # Copy component READMEs into docs/developer/ so they are part of the built docs
        developer_dir = docs_dir / "developer"
        developer_dir.mkdir(exist_ok=True)
        component_readmes = [
            ("open_dir_server", "README.md"),
            ("worker_plan", "README.md"),
            ("frontend_single_user", "README.md"),
            ("database_postgres", "README.md"),
            ("worker_plan_database", "README.md"),
            ("frontend_multi_user", "README.md"),
            ("mcp_local", "README.md"),
            ("mcp_cloud", "README.md"),
        ]
        for component, readme_name in component_readmes:
            src = planexe_repo / component / readme_name
            dst = developer_dir / f"{component}.md"
            if src.exists():
                shutil.copy2(src, dst)
            else:
                print_colored(
                    f"Warning: {src} not found, skipping for docs",
                    YELLOW
                )
        
        # Copy mkdocs.yml to temp directory
        shutil.copy2(mkdocs_yml, temp_docs_path / "mkdocs.yml")

        # Inject proposals into nav (alphabetical) if proposals dir exists.
        proposals_dir = docs_dir / "proposals"
        if proposals_dir.exists():
            class _IgnoreUnknownTagLoader(yaml.SafeLoader):
                pass

            def _construct_undefined(loader, node):
                return node.value

            _IgnoreUnknownTagLoader.add_constructor(None, _construct_undefined)

            mkdocs_temp_path = temp_docs_path / "mkdocs.yml"
            with open(mkdocs_temp_path, "r") as f:
                mkdocs_config = yaml.load(f, Loader=_IgnoreUnknownTagLoader)

            proposals = sorted(
                [
                    p for p in proposals_dir.glob("*.md")
                    if p.name.lower() != "agents.md"
                ],
                key=lambda p: p.name.lower(),
            )
            proposals_nav = []
            for proposal_path in proposals:
                title = proposal_path.stem.replace("_", " ").replace("-", " ").strip()
                proposals_nav.append({title: f"proposals/{proposal_path.name}"})

            nav = mkdocs_config.get("nav", [])
            for entry in nav:
                if isinstance(entry, dict) and "Development" in entry:
                    dev_items = entry["Development"]
                    if isinstance(dev_items, list):
                        dev_items = [
                            item for item in dev_items
                            if not (isinstance(item, dict) and "Proposals" in item)
                        ]
                        dev_items.append({"Proposals": proposals_nav})
                        entry["Development"] = dev_items
                    break

            with open(mkdocs_temp_path, "w") as f:
                yaml.safe_dump(mkdocs_config, f, sort_keys=False)
        
        # Build the documentation
        print_colored("Building with mkdocs...", YELLOW)
        
        try:
            subprocess.run(
                ["mkdocs", "build", "--site-dir", output_dir],
                cwd=temp_docs_path,
                check=True
            )
        except subprocess.CalledProcessError as e:
            print_colored(f"Error: mkdocs build failed: {e}", RED)
            sys.exit(1)
        except FileNotFoundError:
            print_colored(
                "Error: mkdocs command not found. Please install mkdocs-material.",
                RED
            )
            sys.exit(1)
        
        # Move output to current directory
        built_site = temp_docs_path / output_dir
        output_path = original_dir / output_dir
        
        if output_path.exists():
            shutil.rmtree(output_path)
        
        shutil.move(str(built_site), str(output_path))
    
    print_colored("✓ Documentation built successfully!", GREEN)
    print_colored(f"Output is in the '{output_dir}' directory", GREEN)


if __name__ == "__main__":
    main()
