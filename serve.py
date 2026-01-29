#!/usr/bin/env python3
"""
Serve script for PlanExe documentation.
Serves the built site directory using Python's built-in HTTP server.
"""

import os
import sys
import http.server
import socketserver
from pathlib import Path

PORT = 18525
SITE_DIR = "site"


def main():
    """Main serve function."""
    site_path = Path(SITE_DIR)
    
    if not site_path.exists():
        print(f"Error: Site directory '{SITE_DIR}' not found.")
        print("Please run 'python build.py' first to build the documentation.")
        sys.exit(1)
    
    os.chdir(site_path)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving documentation at http://127.0.0.1:{PORT}/")
        print(f"Or http://localhost:{PORT}/")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            sys.exit(0)


if __name__ == "__main__":
    main()
