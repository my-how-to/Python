# =========================================
#  DECORATORS — BEST PRACTICES & ADVANCED
# =========================================
#
# This file expands the basics and introduces:
#    - functools.wraps
#    - decorators that accept arguments
#    - stacked decorators
#    - preserving original functions
#    - practical guidelines
#
# All explanations are included inside triple-quoted blocks.
#


# ============================================================
# 1. WHY functools.wraps IS IMPORTANT
# ============================================================

"""
When you use a decorator, the wrapper replaces the original function.
This means:
    - __name__ becomes 'wrapper'
    - __doc__ becomes None
    - __module__ may change
    - debugging tools become less useful

Solution: use functools.wraps.
This copies metadata from the original function to the wrapper.
"""

import functools

def uppercase_wraps(func):
    """Decorator that uppercases the return value and preserves metadata."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_wraps
def hello(name):
    """Return a simple greeting."""
    return f"hello {name}"


def demo_wraps():
    print("hello('Alex') ->", hello("Alex"))
    print("Function name:", hello.__name__)
    print("Docstring:", hello.__doc__)


# ============================================================
# 2. DECORATORS THAT ACCEPT ARGUMENTS
# ============================================================

"""
Sometimes you want a decorator that accepts parameters, e.g.:
    @repeat(times=3)
    def greet(): ...

This requires three layers:
    1. the outer function receives decorator arguments
    2. the middle function receives the decorated function
    3. the inner wrapper receives the function call arguments
"""

def repeat(times):
    """Repeat the function output N times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def cheer():
    print("Go!")


def demo_repeat():
    cheer()  # prints 'Go!' three times


# ============================================================
# 3. STACKING DECORATORS
# ============================================================

"""
Decorators stack from bottom to top.

Example:
    @deco1
    @deco2
    def func():
        pass

Equivalent to:
    func = deco1(deco2(func))
"""

def deco1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("[deco1] before")
        result = func(*args, **kwargs)
        print("[deco1] after")
        return result
    return wrapper

def deco2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("[deco2] before")
        result = func(*args, **kwargs)
        print("[deco2] after")
        return result
    return wrapper

@deco1
@deco2
def process():
    print("processing...")


def demo_stack():
    process()


# ============================================================
# 4. PRESERVING ORIGINAL FUNCTION (OPTIONAL FEATURE)
# ============================================================

"""
Sometimes you want access to the undecorated function.
You can store it manually:

    wrapper.original = func

This allows:
    decorated()
    decorated.original()
"""

def uppercase_keep_original(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    wrapper.original = func
    return wrapper

@uppercase_keep_original
def speak():
    return "quiet voice"


def demo_original():
    print("Decorated:", speak())
    print("Original:", speak.original())


# ============================================================
# 5. GENERAL BEST PRACTICES SUMMARY
# ============================================================

BEST_PRACTICES = """
DECORATOR BEST PRACTICES:

1. Always use functools.wraps.
2. Use *args and **kwargs for universal compatibility.
3. Keep decorators simple; avoid hiding too much logic.
4. When needed, allow access to the original function.
5. Use decorator arguments for configurable behavior.
6. Remember stacking order (bottom applies first).
7. Keep decorators reusable and pure.
"""


def print_best_practices():
    print(BEST_PRACTICES)


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    demo_wraps()
    demo_repeat()
    demo_stack()
    demo_original()
    print_best_practices()
