#!/usr/bin/env python3
"""
Serve script for PlanExe documentation.
Serves the built site directory using Python's built-in HTTP server.
"""

import errno
import os
import sys
import http.server
import socketserver
from pathlib import Path

DEFAULT_PORT = 18525
PORT_RANGE = range(DEFAULT_PORT, DEFAULT_PORT + 6)  # try 18525–18530
SITE_DIR = "site"


class ReuseAddressTCPServer(socketserver.TCPServer):
    """TCPServer that allows reusing the address (avoids 'Address already in use' after restart)."""
    allow_reuse_address = True


def main():
    """Main serve function."""
    site_path = Path(SITE_DIR)
    
    if not site_path.exists():
        print(f"Error: Site directory '{SITE_DIR}' not found.")
        print("Please run 'python build.py' first to build the documentation.")
        sys.exit(1)
    
    os.chdir(site_path)
    
    Handler = http.server.SimpleHTTPRequestHandler
    port = None

    for port in PORT_RANGE:
        try:
            httpd = ReuseAddressTCPServer(("", port), Handler)
            break
        except OSError as e:
            if e.errno != errno.EADDRINUSE:
                raise
            continue
    else:
        print(f"Error: All ports {DEFAULT_PORT}–{PORT_RANGE.stop - 1} are in use.")
        print("Stop another server (e.g. another 'python serve.py') or free a port.")
        sys.exit(1)

    with httpd:
        print(f"Serving documentation at http://127.0.0.1:{port}/")
        print(f"Or http://localhost:{port}/")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server and releasing port…")
            httpd.server_close()
            print("Server stopped.")
            sys.exit(0)


if __name__ == "__main__":
    main()
