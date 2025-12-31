# ============================================================
#            LESSON — CONDITIONS (INTRO)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Fundamental conditional patterns for beginners:
#   simple decisions, comparison and logical operators,
#   multi-branch flows, nesting basics, truthy/falsy checks,
#   and a lightweight input validation loop.
#
# Contents:
#   1. Simple if statements
#   2. Comparison & logical operators
#   3. Boolean expressions in conditions
#   4. Multi-branch decisions
#   5. Nested decisions
#   6. Truthy vs falsy
#   7. Basic input validation
#
# ============================================================


print("\n# -----------------------------")
print("# 1. SIMPLE IF STATEMENTS")
print("# -----------------------------\n")

temperature_c = 18

if temperature_c > 20:
    print("Open the windows, it's warm!")

if temperature_c <= 20:
    print("Maybe grab a light jacket.")


print("\n# -----------------------------")
print("# 2. COMPARISON & LOGICAL OPERATORS")
print("# -----------------------------\n")

age = 19
has_id = True

if age >= 18 and has_id:
    print("Entry granted.")
else:
    print("Entry denied. Bring your ID next time.")

day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend vibes.")

print("\n# -----------------------------")
print("# 2.1 BOOLEAN TRUTH TABLES")
print("# -----------------------------\n")

# Truth tables show every possible outcome for logical operators.
rows = [
    (True, True),
    (True, False),
    (False, True),
    (False, False),
]

print("A     B     | A and B | A or B  | A xor B | not A")
print("-" * 50)
for a, b in rows:
    and_result = a and b
    or_result = a or b
    xor_result = (a and not b) or (not a and b)
    not_a = not a
    print(f"{a!s:<5} {b!s:<5} | {and_result!s:<7} | {or_result!s:<6} | {xor_result!s:<7} | {not_a!s}")

print("\n# -----------------------------")
print("# 2.2 OPERATOR PRECEDENCE (not, and, or)")
print("# -----------------------------\n")

# Precedence order is: not > and > or
# Use parentheses when in doubt.
a = True
b = False
c = True

print("a or b and c ->", a or b and c)       # and runs before or
print("(a or b) and c ->", (a or b) and c)  # parentheses change grouping


print("\n# -----------------------------")
print("# 3. BOOLEAN EXPRESSIONS IN CONDITIONS")
print("# -----------------------------\n")

# A boolean expression is any calculation that resolves to True or False.
# You can store them in variables or combine multiple expressions.

# Example 1: Direct boolean variable
balance = 150
account_on_hold = False
has_funds = balance > 0
can_withdraw = has_funds and not account_on_hold
print("Can withdraw?", can_withdraw)

# Example 2: Combined expressions
day_type = "weekday"
has_vacation = True

if day_type == "weekend" or has_vacation:
    print("Plan a longer hike.")
else:
    print("Keep it to a short walk.")

# Example 3: Using 'not' operator
is_cold = True
has_jacket = False

# Note: You can use 'not' to invert any boolean expression.
if is_cold and not has_jacket:
    print("Buy a jacket before going out.")


print("\n# -----------------------------")
print("# 4. MULTI-BRANCH DECISIONS")
print("# -----------------------------\n")

traffic_light = "yellow"

if traffic_light == "green":
    print("Go")
elif traffic_light == "yellow":
    print("Slow down")
else:
    print("Stop")


print("\n# -----------------------------")
print("# 5. NESTED DECISIONS")
print("# -----------------------------\n")

user_role = "editor"
can_publish = False

if user_role == "admin":
    print("Full access granted.")
elif user_role == "editor":
    if can_publish:
        print("Editor publishing mode enabled.")
    else:
        print("Editor access limited to drafts.")
else:
    print("Viewer mode only.")


print("\n# -----------------------------")
print("# 6. TRUTHY VS FALSY")
print("# -----------------------------\n")

shopping_cart = []
if not shopping_cart:
    print("Cart is empty.")

username = "alex"
if username:
    print("Welcome back,", username)


print("\n# -----------------------------")
print("# 7. BASIC INPUT VALIDATION")
print("# -----------------------------\n")

while True:
    guess = input("Guess a number between 1 and 5: ")
    if not guess.isdigit():
        print("Digits only, please.")
        continue

    number = int(guess)
    if 1 <= number <= 5:
        print("Nice choice!")
        break
    else:
        print("Keep guesses between 1 and 5.")
