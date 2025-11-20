# =========================================
#   DECORATORS — BASICS & FUNDAMENTALS
# =========================================
# This file is a personal learning/teaching reference.
# It explains decorators step-by-step with clear examples.
#
# CONTENTS:
#     1. What is a decorator?
#     2. Minimal decorator (no arguments)
#     3. How @decorator syntax works
#     4. Step-by-step execution flow
#     5. Decorators that accept ANY arguments (*args, **kwargs)
#     6. Reusable decorator demo
#     7. Summary


# ============================================================
# 1. WHAT IS A DECORATOR?
# ============================================================

"""
Decorators in Python modify or enhance functions without changing their internal code.
They separate the "what" from the "how":
    - The function defines WHAT it does
    - The decorator defines HOW its behavior is modified

This separation keeps logic cleaner, reusable, and easier to maintain.
"""

"""
A decorator in Python is:

    → a function that takes another function
    → adds extra behavior to it
    → returns a modified function

The key idea:
    "Wrapping extra behavior around a function."

Benefits:
    ✓ Reusable behavior
    ✓ No changes inside the original function
    ✓ Clean, readable, maintainable code
"""


# ============================================================
# 2. SIMPLE DECORATOR (NO ARGUMENTS)
# ============================================================

def uppercase_simple(func):
    """
    A decorator that uppercases the return value of a function,
    but only works for functions that accept NO arguments.
    """
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase_simple
def greet_simple():
    return "hello world"


# ============================================================
# 3. "@decorator" SYNTAX EXPLAINED
# ============================================================

"""
This:

    @uppercase_simple
    def greet_simple():
        return "hello"

is the same as:

    def greet_simple():
        return "hello"
    greet_simple = uppercase_simple(greet_simple)

The decorated function name now points to the wrapper(), not the original.
"""


# ============================================================
# 4. STEP-BY-STEP EXECUTION FLOW
# ============================================================

def demo_step_by_step():
    """
    Demonstrates how decorator replacement works.

    1. Define original function.
    2. Pass it to decorator.
    3. Decorator returns wrapper.
    4. Original name now refers to wrapper.
    """
    print("\n=== Step-by-step demonstration ===")

    def original():
        return "hello"

    print("1. Original return:", original())

    decorated = uppercase_simple(original)
    print("2. Decorated return:", decorated())  # HELLO


# ============================================================
# 5. UNIVERSAL DECORATOR USING *args & **kwargs
# ============================================================

"""
Why do we need *args and **kwargs?

Because the simple decorator fails if the function has parameters.

Example:

    @uppercase_simple
    def greet(name):
        return f"hello {name}"

→ ERROR, because wrapper() expects 0 arguments.

Solution:
    Use a wrapper that accepts *any* arguments.
"""


def uppercase(func):
    """
    A universal decorator that:
        - accepts ANY function (with any number of arguments)
        - uppercases its return value, if it's a string
    """
    def wrapper(*args, **kwargs):
        # Forward ALL arguments to the original function
        result = func(*args, **kwargs)

        # Only uppercase strings
        if isinstance(result, str):
            return result.upper()
        return result

    return wrapper


@uppercase
def greet(name):
    """Now works thanks to *args and **kwargs."""
    return f"hello {name}"


@uppercase
def combine(a, b, c=0):
    """This function returns a number — decorator leaves it unchanged."""
    return a + b + c


# ============================================================
# 6. REUSING THE DECORATOR
# ============================================================

@uppercase
def warn():
    return "be careful!"

@uppercase
def bye():
    return "bye friend!"


def demo_reuse():
    print("\n=== Reuse demonstration ===")
    print("greet('Alex'):", greet("Alex"))
    print("bye():", bye())
    print("warn():", warn())
    print("combine(1,2,3):", combine(1, 2, 3), "(not a string → unchanged)")


# ============================================================
# 7. SUMMARY (FOR QUICK REVIEW)
# ============================================================

SUMMARY = """
===========================
      DECORATORS SUMMARY
===========================

• Decorators separate the WHAT from the HOW.
• A decorator is a function that takes a function and returns a new one.
• The @decorator syntax is just syntactic sugar for:
      func = decorator(func)

• wrapper(*args, **kwargs) makes a decorator universal.

• The original function is NOT modified — only wrapped.
• To call the original, you'd need to save a reference BEFORE decorating.

Next steps (in next files):
    → functools.wraps
    → decorators with parameters
    → stacked decorators
    → real-world examples (logging/timing/auth)
"""


def print_summary():
    print("\n" + SUMMARY)


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("greet_simple():", greet_simple())
    demo_step_by_step()
    demo_reuse()
    print_summary()