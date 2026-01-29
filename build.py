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
        
        # Copy mkdocs.yml to temp directory
        shutil.copy2(mkdocs_yml, temp_docs_path / "mkdocs.yml")
        
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
