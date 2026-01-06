# ============================================================
#            LESSON — SHORT-CIRCUIT EVALUATION
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains short-circuit evaluation in Python.
#   It covers:
#       - how `and` and `or` short-circuit
#       - practical safety use-cases
#       - truthy and falsy evaluation
#       - performance impact
#       - common mistakes
#
#   Each section includes clean, runnable examples.
# ============================================================


# ============================================================
# 1. WHAT IS SHORT-CIRCUIT EVALUATION
# ============================================================

# Short-circuit evaluation means Python stops evaluating a logical
# expression as soon as the final result is determined. This applies
# to the logical operators `and` and `or`.


print("\n# -----------------------------")
print("# 2. SHORT-CIRCUIT WITH AND")
print("# -----------------------------\n")

def check_and():
    print("Second condition executed!")
    return True

result = False and check_and()
print("Result:", result)

# Explanation:
# - `and` needs both sides to be True.
# - Because the first value is False, Python never evaluates the second.


print("\n# -----------------------------")
print("# 3. SHORT-CIRCUIT WITH OR")
print("# -----------------------------\n")

def check_or():
    print("Second condition executed!")
    return False

result = True or check_or()
print("Result:", result)

# Explanation:
# - `or` stops as soon as it finds a True value.
# - The second function is skipped entirely.


print("\n# -----------------------------")
print("# 4. TRUTHY AND FALSY VALUES")
print("# -----------------------------\n")

print(bool(0))        # False
print(bool(""))       # False
print(bool(None))     # False
print(bool([]))       # False

print(bool(1))        # True
print(bool("text"))  # True
print(bool([1, 2]))  # True


print("\n# -----------------------------")
print("# 5. SAFE PROPERTY & FUNCTION ACCESS")
print("# -----------------------------\n")

user = None

if user and user.upper():
    print("User exists")
else:
    print("Safe: No crash occurred")

# Without short-circuiting, calling user.upper() would raise AttributeError.


print("\n# -----------------------------")
print("# 6. SHORT-CIRCUIT WITH FUNCTIONS")
print("# -----------------------------\n")

def dangerous():
    print("This should NOT run")
    return 10 / 0

safe = False and dangerous()
print("Still safe")

safe2 = True or dangerous()
print("Still safe")


print("\n# -----------------------------")
print("# 7. OPERATORS RETURN VALUES")
print("# -----------------------------\n")

result = "" or "default"
print(result)

result = 0 and 100
print(result)

# Important rule:
# - `or` returns the first truthy value.
# - `and` returns the first falsy value.


print("\n# -----------------------------")
print("# 8. REAL-WORLD PATTERNS")
print("# -----------------------------\n")

# Default value pattern
name = ""
display_name = name or "Guest"
print(display_name)

# Permission + action pattern
is_admin = False
is_logged_in = True

if is_logged_in and is_admin:
    print("Admin access granted")
else:
    print("Access denied")


print("\n# -----------------------------")
print("# 9. PERFORMANCE BENEFIT")
print("# -----------------------------\n")

def slow_operation():
    print("Performing slow operation...")
    return True

fast = False and slow_operation()
print("Fast path finished")

# Short-circuiting helps avoid extra function calls and heavy computations.


# ============================================================
# 10. COMMON MISTAKES
# ============================================================

x = 0

# Mistake: expecting function to always execute
def f():
    print("Executed")
    return True

x and f()   # Will NOT execute

# Common error: assuming the second expression always runs.
# It does NOT when short-circuit logic is involved.


# ============================================================
# CERTIFICATION TIPS (PCEP / PCAP)
# ============================================================

# Remember:
# - `and` stops on False.
# - `or` stops on True.
# - Expressions return actual values, not only booleans.
# - Used frequently for safe access, default values, permission checks,
#   and performance optimization.
