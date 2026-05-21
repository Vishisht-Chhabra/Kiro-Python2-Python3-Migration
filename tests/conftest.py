# conftest.py - pytest configuration for Python 2 demo tests
import sys
import os

# Add the project root to the path so tests can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
