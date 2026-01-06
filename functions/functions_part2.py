# ============================================================
#            LESSON - FUNCTIONS (PART 2: ADVANCED)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Continuation of the functions lesson: aliases, higher-order
#   functions, nested/closure patterns, recursion, advanced
#   parameter controls, stubs, docstrings, and None returns.
#   Run functions_part1.py first for foundational topics.
#
# Contents:
#   12. Function aliases
#   13. Functions as arguments
#   14. Nested functions
#   15. Closures
#   16. nonlocal
#   17. Recursion
#   18. Keyword argument passing
#   19. Positional-only & keyword-only parameters
#   20. Function stubs (placeholders)
#   21. Docstring format (PEP-257)
#   22. Functions without return → implicit None
#
print("\n# -----------------------------")
print("# 12. Function aliases")
print("# -----------------------------\n")

# Functions in Python are FIRST-CLASS OBJECTS.
# They can be:
#   - assigned to variables
#   - passed into functions
#   - stored in lists/dicts
#   - returned from functions

def shout(text):
    return text.upper()

yell = shout  # alias
print(yell("hello"))


print("\n# -----------------------------")
print("# 13. Functions as arguments")
print("# -----------------------------\n")

# Very common in Python:
#   - sorted(), map(), filter()
#   - callbacks
#   - decorators
#   - strategy pattern

def apply(func, value):
    return func(value)

def square(x):
    return x * x

print(apply(square, 5))


print("\n# -----------------------------")
print("# 14. Nested functions")
print("# -----------------------------\n")

# A function defined inside another function.
# Used for:
#   - hiding helper logic
#   - decorators
#   - closures

def outer():
    print("Outer start")

    def inner():
        print("Inner called")

    inner()

outer()


print("\n# -----------------------------")
print("# 15. Closures")
print("# -----------------------------\n")

# A closure remembers variables from the outer scope.
# Used for:
#   - decorators
#   - factories
#   - making configurable functions

def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
print(double(10))


print("\n# -----------------------------")
print("# 16. nonlocal keyword")
print("# -----------------------------\n")

# nonlocal allows modifying a variable from an ENCLOSING (outer) function.
# Used when closures need to update state.

def counter_factory():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

inc = counter_factory()
print(inc())
print(inc())


print("\n# -----------------------------")
print("# 17. Recursion")
print("# -----------------------------\n")

# A function can call other functions or even itself.
# When a function calls itself, it is called a recursive function.
# It must include a base case (a stop condition), so the calls end.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1) # recursive call

print(factorial(5)) # 120
print(factorial(6)) # 720 


print("\n# -----------------------------")
print("# 18. Keyword argument passing")
print("# -----------------------------\n")

# Keyword arguments are passed by name, not by position.
# They make calls clearer and allow reordering.
# Rule: All required parameters must come first.
# Optional (default) parameters must come after.

def full_name(first, last, *, middle=""):
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

print(full_name("Ada", "Lovelace"))
print(full_name(first="Ada", last="Lovelace"))
print(full_name(last="Lovelace", first="Ada"))
print(full_name("Ada", "Lovelace", middle="Augusta")) # ordered by position first, then by keyword

def add_three(a, b, c):
    return a + b + c

print(add_three(1, c=3, b=2)) # mix positional and keyword

# You can also unpack keyword arguments from a dict.
person = {"first": "Alan", "last": "Turing", "middle": "Mathison"}
print(full_name(**person))


print("\n# -----------------------------")
print("# 19. Positional-only & keyword-only parameters")
print("# -----------------------------\n")

# Introduced in Python 3.8+
# BEFORE "/"  → positional-only
# AFTER "*"   → keyword-only

def pos_only(a, b, /):
    return a + b

print(pos_only(3, 4))

def kw_only(*, a, b):
    return a * b

print(kw_only(a=2, b=3))

def mixed(a, b, /, *, c, d):
    return a + b + c + d

print(mixed(1, 2, c=3, d=4))


print("\n# -----------------------------")
print("# 20. Function stubs")
print("# -----------------------------\n")

# pass → empty function body (common during development)
def todo():
    pass

# ... → ellipsis placeholder (valid no-op)
def future_feature():
    ...

print("Stub functions executed (no output).")


print("\n# -----------------------------")
print("# 21. Docstrings (PEP-257)")
print("# -----------------------------\n")

def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Parameters:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float: The result of a / b

    Raises:
        ZeroDivisionError: If b = 0
    """
    return a / b

print(divide(10, 2))


print("\n# -----------------------------")
print("# 22. Functions without return (implicit None)")
print("# -----------------------------\n")

# If a function has NO return statement,
# Python automatically returns:
#       None
#
# Useful for:
#   - placeholder logic
#   - functions that only print
#   - functions that only modify external state

def f():
    pass  # no return → Python returns None

print(f())  # prints: None
