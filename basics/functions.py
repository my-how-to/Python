# ============================================================
#            LESSON 8 - FUNCTIONS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson covers functions in Python: basic definition,
#   parameters, return values, scope, *args/**kwargs,
#   lambda functions, type hints, function aliases, nested
#   functions, closures, recursion, and more.
#
# Contents:
#   1. Basic function definition
#   2. Functions with parameters
#   3. Return values
#   4. Default parameters
#   5. Multiple returns (tuple)
#   6. Scope (local vs global)
#   7. *args — multiple positional arguments
#   8. **kwargs — multiple named arguments
#   9. Combining *args and **kwargs
#   10. Lambda functions
#   11. Type hints
#   12. Function aliases
#   13. Functions as arguments
#   14. Nested functions
#   15. Closures
#   16. nonlocal
#   17. Recursion
#   18. Positional-only & keyword-only parameters
#   19. Function stubs (placeholders)
#   20. Docstring format (PEP-257)
#   21. Functions without return → implicit None
# 
# ==========================================
# 1. BASIC FUNCTION DEFINITION
# ==========================================

print("\n--- SECTION 1: Basic function definition ---")

def greet():
    """Prints a simple greeting"""
    print("Hello, world!")

greet()


# ==========================================
# 2. FUNCTIONS WITH PARAMETERS
# ==========================================

print("\n--- SECTION 2: Parameters ---")

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alex")


# ==========================================
# 3. RETURN VALUES
# ==========================================

print("\n--- SECTION 3: Return values ---")

def add(a, b):
    return a + b

print(add(3, 5))


# ==========================================
# 4. DEFAULT PARAMETERS
# ==========================================

print("\n--- SECTION 4: Default parameters ---")

def greet_default(name="friend"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Michael")


# ==========================================
# 5. MULTIPLE RETURNS (TUPLE)
# ==========================================

print("\n--- SECTION 5: Multiple returns ---")

def stats(numbers):
    total = sum(numbers)
    biggest = max(numbers)
    smallest = min(numbers)
    return total, biggest, smallest

print(stats([2, 5, 7, 1]))


# ==========================================
# 6. SCOPE (LOCAL VS GLOBAL)
# ==========================================

print("\n--- SECTION 6: Scope (local/global) ---")

a = 5  # global variable

def modify_global():
    # global allows modifying a variable outside the function
    global a
    a = a + 2

modify_global()
print(a)  # now 7

# Better alternative: return the value instead of modifying globals
counter = 0

def increase(value):
    return value + 1

counter = increase(counter)
print(counter)


# ==========================================
# 7. *args — MULTIPLE POSITIONAL ARGUMENTS
# ==========================================

print("\n--- SECTION 7: *args (multiple positional arguments) ---")

# *args collects all extra positional arguments into a TUPLE.
# Useful for:
#   - flexible math helpers
#   - functions that accept unlimited inputs
#   - decorators wrapping any function signature
#   - API helpers, logging, analytics

def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30, 40))


# ==========================================
# 8. **kwargs — MULTIPLE NAMED ARGUMENTS
# ==========================================

print("\n--- SECTION 8: **kwargs (multiple named arguments) ---")

# **kwargs collects all keyword arguments into a DICTIONARY.
# Useful for:
#   - configuration functions
#   - dynamic options
#   - logging/debug helpers
#   - decorators

def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print_info(name="Alex", age=30, country="Moldova")


# ==========================================
# 9. COMBINING *args AND **kwargs
# ==========================================

print("\n--- SECTION 9: Combining *args and **kwargs ---")

# Useful in:
#   - decorators
#   - wrapper functions
#   - API clients
#   - flexible function signatures
#
# Accepts ANY number of positional and named arguments.
# Perfect for writing generic reusable helpers.

def debug_example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

debug_example(1, 2, 3, mode="test", verbose=True)


# ==========================================
# 10. LAMBDA FUNCTIONS
# ==========================================

print("\n--- SECTION 10: lambda functions ---")

# Lambdas are tiny anonymous functions.
# Used for:
#   - sorting
#   - inline transformations
#   - callbacks
#   - one-liners

double = lambda x: x * 2
print(double(5))


# ==========================================
# 11. TYPE HINTS
# ==========================================

print("\n--- SECTION 11: Type hints ---")

# Type hints help explain expected argument types.
# They:
#   - improve code readability
#   - help IDE autocomplete
#   - assist static analyzers (mypy)
#
# They DO NOT change runtime behavior.

def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(3, 4))


# ==========================================
# 12. FUNCTION ALIASES
# ==========================================

print("\n--- SECTION 12: Function aliases ---")

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


# ==========================================
# 13. FUNCTIONS AS ARGUMENTS
# ==========================================

print("\n--- SECTION 13: Functions as arguments ---")

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


# ==========================================
# 14. NESTED FUNCTIONS
# ==========================================

print("\n--- SECTION 14: Nested functions ---")

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


# ==========================================
# 15. CLOSURES
# ==========================================

print("\n--- SECTION 15: Closures ---")

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


# ==========================================
# 16. NONLOCAL
# ==========================================

print("\n--- SECTION 16: nonlocal keyword ---")

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


# ==========================================
# 17. RECURSION
# ==========================================

print("\n--- SECTION 17: Recursion ---")

# A function that calls itself.
# Must always have a base case and move toward it.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# ==========================================
# 18. POSITIONAL-ONLY & KEYWORD-ONLY PARAMETERS
# ==========================================

print("\n--- SECTION 18: Positional-only & keyword-only parameters ---")

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


# ==========================================
# 19. FUNCTION STUBS (PLACEHOLDERS)
# ==========================================

print("\n--- SECTION 19: Function stubs ---")

# pass → empty function body (common during development)
def todo():
    pass

# ... → ellipsis placeholder (valid no-op)
def future_feature():
    ...

print("Stub functions executed (no output).")


# ==========================================
# 20. DOCSTRING FORMAT (PEP-257)
# ==========================================

print("\n--- SECTION 20: Docstrings (PEP-257) ---")

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

# ==========================================
# 21. FUNCTIONS WITHOUT RETURN → IMPLICIT NONE
# ==========================================

print("\n--- SECTION 21: Functions without return (implicit None) ---")

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