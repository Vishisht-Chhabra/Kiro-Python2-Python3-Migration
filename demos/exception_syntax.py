"""Exception Syntax Demonstration - Python 2 exception handling syntax."""

import sys
import traceback


def run():
    """Demonstrate Python 2 exception handling syntax."""

    print "=== Python 2 Exception Syntax Demo ==="
    print ""

    # except Exception, e: (comma syntax)
    print "--- except Exception, e: (comma syntax) ---"
    try:
        result = 1 / 0
    except ZeroDivisionError, e:
        print "Caught with comma syntax: except ZeroDivisionError, e:"
        print "  Exception type:", type(e).__name__
        print "  Exception message:", str(e)
    print ""

    # Another example with comma syntax
    print "--- Another comma syntax example ---"
    try:
        int("not_a_number")
    except ValueError, e:
        print "Caught: except ValueError, e:"
        print "  Error:", e
    print ""

    # raise Exception, "message" syntax
    print "--- raise Exception, 'message' syntax ---"
    try:
        raise ValueError, "this is the old raise syntax"
    except ValueError, e:
        print "Raised with: raise ValueError, 'this is the old raise syntax'"
        print "  Caught:", e
    print ""

    # raise with tuple arguments
    print "--- raise with type and value ---"
    try:
        raise TypeError, "expected int, got str"
    except TypeError, e:
        print "Raised with: raise TypeError, 'expected int, got str'"
        print "  Caught:", e
    print ""

    # Three-argument raise form with traceback
    print "--- Three-argument raise form (with traceback) ---"
    try:
        try:
            raise RuntimeError("original error")
        except:
            exc_type, exc_value, exc_tb = sys.exc_info()
            # Re-raise with the original traceback
            raise RuntimeError, "re-raised with original traceback", exc_tb
    except RuntimeError, e:
        print "Caught re-raised exception:", e
        print "  Traceback preserved (3-arg raise form used)"
    print ""

    # StandardError base class
    print "--- StandardError base class ---"
    print "StandardError exists:", StandardError is not None
    print "StandardError is parent of ValueError:", issubclass(ValueError, StandardError)
    print "StandardError is parent of TypeError:", issubclass(TypeError, StandardError)
    print "StandardError is parent of IOError:", issubclass(IOError, StandardError)
    print "StandardError is subclass of Exception:", issubclass(StandardError, Exception)
    print ""

    # Catching StandardError
    try:
        raise KeyError("test key")
    except StandardError, e:
        print "Caught KeyError via 'except StandardError, e:':", e
