# ============================================================
#            LESSON — CONDITIONS (ADVANCED)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Builds on conditions_intro.py with deeper coverage:
#   chaining comparisons, nested decisions, truthy/falsy,
#   shorthand expressions (ternary + walrus), match/case,
#   and more realistic validation flows.
#
# Contents:
#   1. Simple if statements (quick recap)
#   2. Comparison & logical operators
#   3. Multi-branch decisions (if / elif / else)
#   4. Nested conditions
#   5. Truthy / falsy values
#   6. Shorthand expressions (ternary & walrus)
#   7. Structural pattern matching (match/case)
#   8. Practical input validation
#
# ============================================================


print("\n# -----------------------------")
print("# 1. SIMPLE IF STATEMENTS")
print("# -----------------------------\n")

temperature_c = 30

if temperature_c > 25:
    print("It's a warm day, wear light clothes.")

# Note: if the condition is False nothing from this block runs.


print("\n# -----------------------------")
print("# 2. COMPARISON & LOGICAL OPERATORS")
print("# -----------------------------\n")

# Comparison operators: >, <, >=, <=, ==, !=
age = 18
print("Eligible voter?", age >= 18)

# Logical operators: and, or, not — they chain multiple comparisons.
has_ticket = True
is_vip = False

if (age >= 18 and has_ticket) or is_vip:
    print("Welcome to the concert!")
else:
    print("You need a ticket or to be added to the VIP list.")


print("\n# -----------------------------")
print("# 3. MULTI-BRANCH DECISIONS")
print("# -----------------------------\n")

x = 15

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")

# Use elif for mutually exclusive checks; only the first True block runs.


print("\n# -----------------------------")
print("# 4. NESTED CONDITIONS")
print("# -----------------------------\n")

user_role = "admin"
two_factor_enabled = True

if user_role == "admin":
    if two_factor_enabled:
        print("Admin login approved.")
    else:
        print("Admin access denied: please enable 2FA.")
else:
    print("Standard user login.")

# Prefer flattening deeply nested logic when possible to improve readability.


print("\n# -----------------------------")
print("# 5. TRUTHY VS FALSY")
print("# -----------------------------\n")

# Python treats several values as falsy: 0, 0.0, "", [], {}, None, False.
# Anything else is truthy.

items = []

if not items:
    print("Shopping cart is empty.")

name = "Alex"

if name:
    print("Hello", name)

# Double-negation trick: `not not value` reveals boolean truthiness.
samples = [5, 0, "", "hi", [], [1]]
for value in samples:
    print(f"not not {value!r} -> {not not value}")


print("\n# -----------------------------")
print("# 6. SHORTHAND EXPRESSIONS")
print("# -----------------------------\n")

# Ternary (conditional expression)
score = 92
result = "Pass" if score >= 70 else "Retake"
print("Exam result:", result)

# Walrus operator (Python 3.8+) lets you test & assign in one expression.
# Useful for compact loops or validation checks.

if (user_input := input("Enter your nickname: ")):
    print("Nickname saved:", user_input)
else:
    print("No nickname provided.")


print("\n# -----------------------------")
print("# 7. MATCH / CASE PATTERN MATCHING")
print("# -----------------------------\n")

import sys  # needed for version check in the pattern matching example

# Available from Python 3.10 onwards.
# Older interpreters will fall back to standard if/elif logic below.

http_status = 404

if sys.version_info >= (3, 10):
    pattern_demo = """
match http_status:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400 | 404:
        print("Client error")
    case _:
        print("Unhandled status")
"""
    exec(pattern_demo)
else:
    print("match/case requires Python 3.10+, using if/elif instead.")
    if http_status == 200:
        print("OK")
    elif http_status == 201:
        print("Created")
    elif http_status in (400, 404):
        print("Client error")
    else:
        print("Unhandled status")


print("\n# -----------------------------")
print("# 8. PRACTICAL INPUT VALIDATION")
print("# -----------------------------\n")

print("\nAccount creation — determine eligibility:")

while True:
    age_input = input("Enter your age: ").strip()

    if not age_input.isdigit():
        print("Please enter numbers only.")
        continue

    age_value = int(age_input)

    if age_value < 13:
        print("Sorry, a parent or guardian must create the account.")
    elif 13 <= age_value < 18:
        print("Parental consent required — check your email for instructions.")
    else:
        print("Account created successfully!")

    break  # validation complete; exit loop
