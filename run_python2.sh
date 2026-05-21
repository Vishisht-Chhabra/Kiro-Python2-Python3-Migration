#!/bin/bash
# Helper script to run Python 2.7 code via Docker
# Usage: ./run_python2.sh <python_file_or_args>
# The Kiro-Python2 directory is mounted at /app in the container

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
docker run --rm -v "$SCRIPT_DIR:/app" -w /app python:2.7-slim python "$@"
