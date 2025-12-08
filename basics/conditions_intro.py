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
#   3. Multi-branch decisions
#   4. Nested decisions
#   5. Truthy vs falsy
#   6. Basic input validation
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
print("# 3. MULTI-BRANCH DECISIONS")
print("# -----------------------------\n")

traffic_light = "yellow"

if traffic_light == "green":
    print("Go")
elif traffic_light == "yellow":
    print("Slow down")
else:
    print("Stop")


print("\n# -----------------------------")
print("# 4. NESTED DECISIONS")
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
print("# 5. TRUTHY VS FALSY")
print("# -----------------------------\n")

shopping_cart = []
if not shopping_cart:
    print("Cart is empty.")

username = "alex"
if username:
    print("Welcome back,", username)


print("\n# -----------------------------")
print("# 6. BASIC INPUT VALIDATION")
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

