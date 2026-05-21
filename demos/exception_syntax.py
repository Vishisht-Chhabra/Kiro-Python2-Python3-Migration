"""Exception Syntax Demonstration - Python 2 vs Python 3.

Python 3 changed how exceptions are caught, raised, and chained, and removed
the ``StandardError`` base class. The Python 2 syntax forms below are now
``SyntaxError`` in Python 3 and are kept here for educational comparison:

    Python 2 syntax (now SyntaxError in Python 3):
      except ZeroDivisionError, e:           # comma form
      raise ValueError, "msg"                # two-arg raise
      raise RuntimeError, "msg", tb          # three-arg raise (traceback)
      except StandardError, e:               # StandardError catch-all

    Python 3 syntax:
      except ZeroDivisionError as e:
      raise ValueError("msg")
      raise RuntimeError("msg").with_traceback(tb)
      except Exception as e:                 # StandardError removed; use Exception
"""

import sys


def run():
    """Demonstrate Python 3 exception handling syntax."""

    print("=== Python 3 Exception Syntax Demo ===")
    print("")

    # except Exception as e: (Python 2 used the comma form)
    # Python 2 form (now SyntaxError):
    #     except ZeroDivisionError, e:
    print("--- except ZeroDivisionError as e: (was: except ZeroDivisionError, e:) ---")
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print("Caught with as-syntax: except ZeroDivisionError as e:")
        print("  Exception type:", type(e).__name__)
        print("  Exception message:", str(e))
    print("")

    # Another example with the as-syntax.
    # Python 2 form (now SyntaxError):
    #     except ValueError, e:
    print("--- Another as-syntax example ---")
    try:
        int("not_a_number")
    except ValueError as e:
        print("Caught: except ValueError as e:")
        print("  Error:", e)
    print("")

    # raise Exception("message") - Python 2 used `raise Exception, "msg"`.
    # Python 2 form (now SyntaxError):
    #     raise ValueError, "this is the old raise syntax"
    print("--- raise ValueError('message') (was: raise ValueError, 'message') ---")
    try:
        raise ValueError("this is the new raise syntax")
    except ValueError as e:
        print("Raised with: raise ValueError('this is the new raise syntax')")
        print("  Caught:", e)
    print("")

    # raise with type and value
    # Python 2 form (now SyntaxError):
    #     raise TypeError, "expected int, got str"
    print("--- raise with type and value ---")
    try:
        raise TypeError("expected int, got str")
    except TypeError as e:
        print("Raised with: raise TypeError('expected int, got str')")
        print("  Caught:", e)
    print("")

    # Three-argument raise form replaced by .with_traceback(tb).
    # Python 2 form (now SyntaxError):
    #     raise RuntimeError, "re-raised with original traceback", exc_tb
    print("--- raise E('msg').with_traceback(tb) (was: raise E, V, T) ---")
    try:
        try:
            raise RuntimeError("original error")
        except RuntimeError:
            exc_type, exc_value, exc_tb = sys.exc_info()
            # Re-raise with the original traceback using the Python 3 form.
            raise RuntimeError("re-raised with original traceback").with_traceback(exc_tb)
    except RuntimeError as e:
        print("Caught re-raised exception:", e)
        print("  Traceback preserved via .with_traceback(tb)")
    print("")

    # StandardError was removed in Python 3 - use Exception instead.
    # Python 2 had a StandardError base class for most built-in errors;
    # Python 3 removed it and folded those classes directly under Exception.
    print("--- StandardError was removed in Python 3 (use Exception) ---")
    print("Note: In Python 2, StandardError was the parent of most built-in")
    print("      errors (ValueError, TypeError, IOError, KeyError, ...).")
    print("      Python 3 removed StandardError; those classes now inherit")
    print("      directly from Exception.")
    print("Exception is parent of ValueError:", issubclass(ValueError, Exception))
    print("Exception is parent of TypeError:", issubclass(TypeError, Exception))
    print("Exception is parent of IOError:", issubclass(IOError, Exception))
    print("Exception is parent of KeyError:", issubclass(KeyError, Exception))
    print("")

    # Catching via Exception (Python 2 used `except StandardError, e:`).
    # Python 2 form (now NameError / SyntaxError):
    #     except StandardError, e:
    try:
        raise KeyError("test key")
    except Exception as e:
        print("Caught KeyError via 'except Exception as e:':", e)
