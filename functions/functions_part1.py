# ============================================================
#            LESSON - FUNCTIONS (PART 1: FOUNDATIONS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Foundations of Python functions: definitions, parameters,
#   returns, scope, *args/**kwargs, lambdas, and type hints.
#   Run functions_part2.py for advanced patterns and extras.
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
# 

print("\n# -----------------------------")
print("# 1. Basic function definition")
print("# -----------------------------\n")

def greet():
    """Prints a simple greeting"""
    print("Hello, world!")

greet()


print("\n# -----------------------------")
print("# 2. Parameters")
print("# -----------------------------\n")

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alex")

# Note: the function gets the argument's value, not the variable itself.
# Reassigning the parameter does not affect the caller's variable.
# This is clear with immutable scalars like ints and strings.
age = 20

def change_age(value):
    value = 99
    print("Inside function:", value)

change_age(age)
print("Outside function:", age)

# However, for mutable types (like lists/dicts), modifying the object inside
# the function affects the original object.
# List variables store references to list objects, not the raw values.
# The parameter receives that reference, so mutations affect the same list.

numbers = [1, 2, 3]
def append_number(lst):
    lst.append(4) # mutating the list object
    print("Inside function:", lst)
    
append_number(numbers) 
print("Outside function:", numbers) # the original list is changed

# But if you mutate the list object the parameter points to
# (the object, not the name), the change is visible outside.

def reassign_list(lst):
    lst = [9, 8, 7]  # reassigning the parameter to a new list
    print("Inside function:", lst)
reassign_list(numbers)
print("Outside function:", numbers) # the original list remains unchanged


print("\n# -----------------------------")
print("# 3. Return values")
print("# -----------------------------\n")

def add(a, b):
    return a + b

print(add(3, 5))

# A bare return (or no return at all) means the function returns None.
def log_message(msg):
    print("LOG:", msg)
    return

def do_nothing():
    pass

print(log_message("Saved"))     # prints message, then prints None
log_message("Error occurred")   # prints message, return value ignored
print(do_nothing())             # prints None

# You can ignore a return value if you only need the side effect.
def notify(user):
    return f"Email sent to {user}"

notify("Alex")  # return value ignored on purpose
status = notify("Mara")
print(status)


print("\n# -----------------------------")
print("# 4. Default parameters")
print("# -----------------------------\n")

def greet_default(name="friend"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Michael")

# Beware: default arguments are evaluated once at function definition time.
def bad_accumulator(values=[]):
    values.append(1)
    return values
# list keeps growing with each call
print(bad_accumulator(), bad_accumulator())  # [1] [1, 1]

# Fix by using None as default and creating a new list inside.
def good_accumulator(values=None):
    if values is None:
        values = []
    values.append(1)
    return values
# new list each time
print(good_accumulator(), good_accumulator())  # [1] [1]


print("\n# -----------------------------")
print("# 5. Multiple returns")
print("# -----------------------------\n")

def stats(numbers):
    total = sum(numbers)
    biggest = max(numbers)
    smallest = min(numbers)
    return total, biggest, smallest

print(stats([2, 5, 7, 1]))


print("\n# -----------------------------")
print("# 6. Scope (local/global)")
print("# -----------------------------\n")

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


print("\n# -----------------------------")
print("# 7. *args (multiple positional arguments)")
print("# -----------------------------\n")

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


print("\n# -----------------------------")
print("# 8. **kwargs (multiple named arguments)")
print("# -----------------------------\n")

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

# Keyword arguments override positional order because names win; their order is irrelevant.
def announce(event, place, time):
    print(f"{event} at {place} starting {time}")

announce("Meetup", place="Community Hall", time="19:00")
announce("Workshop", time="18:30", place="Studio B")


print("\n# -----------------------------")
print("# 9. Combining *args and **kwargs")
print("# -----------------------------\n")

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


print("\n# -----------------------------")
print("# 10. lambda functions")
print("# -----------------------------\n")

# Lambdas are tiny anonymous functions.
# Used for:
#   - sorting
#   - inline transformations
#   - callbacks
#   - one-liners

double = lambda x: x * 2
print(double(5))


print("\n# -----------------------------")
print("# 11. Type hints")
print("# -----------------------------\n")

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
