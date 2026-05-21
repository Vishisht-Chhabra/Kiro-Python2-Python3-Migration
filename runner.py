"""Demo Runner module.

Executes a demo module's run() function and captures its stdout output.
Provides the source code and output (or error) as a DemoResult.
"""

import sys
import io
import inspect
import traceback


class DemoResult:
    """Result of executing a demo module.

    Attributes:
        source_code: The Python source code of the demo module.
        output: Captured stdout from executing the demo.
        error: Error message if execution failed, None on success.
    """

    def __init__(self, source_code, output, error):
        self.source_code = source_code
        self.output = output
        self.error = error


class DemoRunner:
    """Executes demo modules and captures their output.

    Redirects sys.stdout to a StringIO buffer during execution,
    restoring it afterwards even if an error occurs.
    """

    def execute(self, module):
        """Execute module.run(), capturing stdout.

        Args:
            module: A Python module with a run() function.

        Returns:
            DemoResult with source_code, output, and error fields.
        """
        # Read the module's source code
        source_code = self._get_source(module)

        # Capture stdout during execution
        captured = io.StringIO()
        old_stdout = sys.stdout
        output = ""
        error = None

        try:
            sys.stdout = captured
            module.run()
        except Exception:
            error = traceback.format_exc()
        finally:
            sys.stdout = old_stdout
            output = captured.getvalue()
            captured.close()

        return DemoResult(source_code, output, error)

    def _get_source(self, module):
        """Read the source code of a module.

        Args:
            module: A Python module object.

        Returns:
            The source code as a string, or a placeholder if unavailable.
        """
        try:
            return inspect.getsource(module)
        except (TypeError, IOError):
            return "# Source unavailable"
