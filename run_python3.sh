#!/bin/bash
# Helper script to run Python 3 code via Docker.
# Usage: ./run_python3.sh <python_file_or_args>
# The project directory is mounted at /app in the container.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
docker run --rm -v "$SCRIPT_DIR:/app" -w /app python:3.11-slim python "$@"
