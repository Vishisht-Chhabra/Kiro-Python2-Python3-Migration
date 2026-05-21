"""Main entry point for the Python 2 Feature Demos web application.

Registers all demo modules with the registry and starts the HTTP server
on a configurable port (default 8080).
"""

import sys
import socket
import BaseHTTPServer

from registry import DemoRegistry
from runner import DemoRunner
from renderer import HtmlRenderer
from server import DemoRequestHandler

from demos import print_statement
from demos import integer_division
from demos import unicode_handling
from demos import range_xrange
from demos import dict_methods
from demos import user_input
from demos import exec_statement
from demos import string_formatting
from demos import exception_syntax
from demos import numeric_types
from demos import iterators_functional
from demos import classes_objects
from demos import module_imports


def main(port=8080):
    """Start the HTTP server on the given port.

    Args:
        port: TCP port number to listen on (default 8080).
    """
    # Create shared instances
    registry = DemoRegistry()
    runner = DemoRunner()
    renderer = HtmlRenderer()

    # Register all demo modules
    registry.register("print_statement", "Print Statement", print_statement)
    registry.register("integer_division", "Integer Division", integer_division)
    registry.register("unicode_handling", "Unicode Handling", unicode_handling)
    registry.register("range_xrange", "Range and Xrange", range_xrange)
    registry.register("dict_methods", "Dictionary Methods", dict_methods)
    registry.register("user_input", "User Input", user_input)
    registry.register("exec_statement", "Exec Statement", exec_statement)
    registry.register("string_formatting", "String Formatting", string_formatting)
    registry.register("exception_syntax", "Exception Syntax", exception_syntax)
    registry.register("numeric_types", "Numeric Types", numeric_types)
    registry.register("iterators_functional", "Iterators and Functional Programming", iterators_functional)
    registry.register("classes_objects", "Classes and Objects", classes_objects)
    registry.register("module_imports", "Module Imports", module_imports)

    # Inject dependencies into the request handler
    DemoRequestHandler.registry = registry
    DemoRequestHandler.runner = runner
    DemoRequestHandler.renderer = renderer

    # Start the server
    try:
        server = BaseHTTPServer.HTTPServer(("", port), DemoRequestHandler)
    except socket.error as e:
        if e.errno == 98 or e.errno == 48:
            print >> sys.stderr, "Error: Port %d is already in use. Try a different port." % port
            sys.exit(1)
        raise

    print >> sys.stderr, "Python 2 Feature Demos server running at http://localhost:%d/" % port
    print >> sys.stderr, "Press Ctrl+C to stop."

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print >> sys.stderr, "\nShutting down server."
        server.shutdown()


if __name__ == "__main__":
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print >> sys.stderr, "Error: Invalid port number '%s'" % sys.argv[1]
            sys.exit(1)
    main(port)
