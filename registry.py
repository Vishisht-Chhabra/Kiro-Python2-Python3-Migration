"""Demo Registry module.

Provides a central registry that maps demo names to their modules,
maintaining insertion order for consistent index page rendering.
"""


class DemoRegistry:
    """Registry for demo modules.

    Stores demo entries as an ordered list of (name, title, module) tuples.
    Provides lookup by name and listing of all registered demos.
    """

    def __init__(self):
        self._demos = []

    def register(self, name, title, module):
        """Register a demo module with a URL-safe name and display title.

        Args:
            name: URL-safe identifier (e.g., "print_statement")
            title: Human-readable title (e.g., "Print Statement Demonstration")
            module: Reference to the Python module object
        """
        self._demos.append((name, title, module))

    def get_all(self):
        """Return list of (name, title) tuples for all registered demos.

        Returns:
            List of (name, title) tuples in registration order.
        """
        return [(name, title) for name, title, module in self._demos]

    def get_module(self, name):
        """Return the module for a given demo name, or None.

        Args:
            name: The URL-safe demo name to look up.

        Returns:
            The module reference if found, None otherwise.
        """
        for demo_name, title, module in self._demos:
            if demo_name == name:
                return module
        return None
