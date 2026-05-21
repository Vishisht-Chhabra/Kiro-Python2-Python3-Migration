"""Classes and Objects Demonstration - Python 2 vs Python 3.

Python 2 had two flavors of class:
    class C:           -> old-style (legacy)
    class C(object):   -> new-style (inherits from object)

Python 3 has only new-style classes; the `(object)` base is redundant
because every class in Python 3 already inherits from `object`.

Removed/changed in Python 3:
    __metaclass__ = M               -> class C(Base, metaclass=M):
    __cmp__(self, other)            -> __lt__, __eq__ (or @functools.total_ordering)
    cmp(a, b)                       -> (a > b) - (a < b)
    Class.method (unbound method)   -> plain function;
                                       call as Class.method(instance, ...)
"""

import functools


def run():
    """Demonstrate Python 3 class syntax features."""

    print("=== Python 3 Classes & Objects Demo ===")
    print("")

    # In Python 2, omitting `(object)` produced an old-style class.
    # In Python 3 the same syntax produces a new-style class because
    # every class implicitly inherits from object.
    print("--- 'Old-style' syntax in Py3 is just a normal new-style class ---")

    class OldStyleAnimal:
        """In Py2 this was old-style; in Py3 it's a normal new-style class."""
        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

        def speak(self):
            return "%s says %s" % (self.name, self.sound)

    cat = OldStyleAnimal("Cat", "Meow")
    print("class OldStyleAnimal: (no explicit base)")
    print("  cat.speak() =", cat.speak())
    print("  type(cat) =", type(cat))
    print("  type(OldStyleAnimal) =", type(OldStyleAnimal))
    print("  OldStyleAnimal.__bases__ =", OldStyleAnimal.__bases__)
    print("")

    # New-style class - in Py3 the (object) base is redundant.
    print("--- New-style class (no need to write `(object)`) ---")

    class NewStyleAnimal:
        """In Py3, omit `(object)`; every class is already new-style."""
        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

        def speak(self):
            return "%s says %s" % (self.name, self.sound)

    dog = NewStyleAnimal("Dog", "Woof")
    print("class NewStyleAnimal: (object base dropped)")
    print("  dog.speak() =", dog.speak())
    print("  type(dog) =", type(dog))
    print("  type(NewStyleAnimal) =", type(NewStyleAnimal))
    print("  NewStyleAnimal.__bases__ =", NewStyleAnimal.__bases__)
    print("")

    # In Python 2 you'd write `__metaclass__ = MyMeta` inside the class body.
    # In Python 3 the metaclass is specified as a class keyword argument.
    print("--- metaclass keyword syntax (replaces __metaclass__) ---")

    class MyMeta(type):
        def __new__(mcs, name, bases, attrs):
            attrs['meta_created'] = True
            return super().__new__(mcs, name, bases, attrs)

    class MyClass(metaclass=MyMeta):
        value = 42

    print("class MyClass(metaclass=MyMeta):")
    print("  MyClass.meta_created =", MyClass.meta_created)
    print("  MyClass.value =", MyClass.value)
    print("  type(MyClass) =", type(MyClass))
    print("")

    # Python 3 removed __cmp__ and the built-in cmp(). Use rich-comparison
    # methods instead - here we use functools.total_ordering so we only have
    # to define __eq__ and __lt__.
    print("--- Rich comparison methods (replace __cmp__) ---")

    @functools.total_ordering
    class Temperature:
        def __init__(self, degrees):
            self.degrees = degrees

        def __eq__(self, other):
            return self.degrees == other.degrees

        def __lt__(self, other):
            return self.degrees < other.degrees

        def __repr__(self):
            return "Temperature(%d)" % self.degrees

    hot = Temperature(100)
    warm = Temperature(75)
    cold = Temperature(32)

    # cmp(a, b) was removed in Python 3. The standard one-liner replacement
    # is (a > b) - (a < b), which produces -1, 0, or 1 just like cmp.
    def py3_cmp(a, b):
        return (a > b) - (a < b)

    print("Temperature objects with @functools.total_ordering + __eq__/__lt__:")
    print("  (hot > cold) - (hot < cold) =", py3_cmp(hot, cold))
    print("  (cold > hot) - (cold < hot) =", py3_cmp(cold, hot))
    print("  (warm > warm) - (warm < warm) =", py3_cmp(warm, warm))
    print("  hot < cold =", hot < cold)
    print("  hot > cold =", hot > cold)
    print("  warm == warm =", warm == warm)
    print("  sorted([hot, cold, warm]) =", sorted([hot, cold, warm]))
    print("")

    # In Python 2, accessing a method via the class produced an "unbound
    # method" object that enforced the type of `self`. In Python 3 the same
    # access just returns the underlying plain function.
    print("--- Class.method is a plain function in Python 3 ---")

    class Greeter:
        def hello(self, name):
            return "Hello, %s!" % name

    # Accessing method through the class gives a plain function in Py3.
    func = Greeter.hello
    print("Greeter.hello =", func)
    print("  type(Greeter.hello) =", type(Greeter.hello))

    # You can still call it by passing the instance explicitly.
    g = Greeter()
    result = Greeter.hello(g, "World")
    print("  Greeter.hello(g, 'World') =", result)
