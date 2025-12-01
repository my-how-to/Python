# ============================================================
#            LESSON 2 — OPERATORS & EXPRESSIONS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson introduces operators and expressions in Python:
#   what expressions are, arithmetic operators, comparison
#   operators, logical operators, assignment operators, operator
#   precedence, and practical mini-examples.    
#
# Contents:
#   1. What is an expression?
#   2. Arithmetic operators
#   3. Comparison operators
#   4. Logical operators
#   5. Assignment operators
#   6. Operator precedence
#   7. Practical mini-examples
#
# ============================================================


print("\n# -----------------------------")
print("# 1. WHAT IS AN EXPRESSION?")
print("# -----------------------------\n")

# An expression is a combination of values and operators.
# Python evaluates it and produces a result.

result = 5 + 3 * 2
print("Result of 5 + 3 * 2 =", result)

# Output:
# 11


print("\n# -----------------------------")
print("# 2. ARITHMETIC OPERATORS")
print("# -----------------------------\n")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)            # float division
print("Floor Division:", a // b)     # removes decimal
print("Modulus:", a % b)             # remainder
print("Exponent:", a ** b)           # a^b

# Example Output:
# Addition: 13
# Subtraction: 7
# Multiplication: 30
# Division: 3.3333333333333335
# Floor Division: 3
# Modulus: 1
# Exponent: 1000


print("\n# -----------------------------")
print("# 3. COMPARISON OPERATORS")
print("# -----------------------------\n")

x = 5
y = 7

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# Example Output:
# x == y: False
# x != y: True
# x > y: False
# x < y: True
# x >= y: False
# x <= y: True


print("\n# -----------------------------")
print("# 4. LOGICAL OPERATORS")
print("# -----------------------------\n")

is_admin = True
is_active = False

print("AND:", is_admin and is_active)
print("OR:", is_admin or is_active)
print("NOT:", not is_admin)

# Example Output:
# AND: False
# OR: True
# NOT: False


print("\n# -----------------------------")
print("# 5. ASSIGNMENT OPERATORS")
print("# -----------------------------\n")

value = 10
print("Start:", value)

value += 5  # value = value + 5
print("After += 5:", value)

value -= 3
print("After -= 3:", value)

value *= 2
print("After *= 2:", value)

value //= 4
print("After //= 4:", value)

# Example Output:
# Start: 10
# After += 5: 15
# After -= 3: 12
# After *= 2: 24
# After //= 4: 6


print("\n# -----------------------------")
print("# 6. OPERATOR PRECEDENCE")
print("# -----------------------------\n")

# Python evaluates according to rules (PEMDAS):
# Parentheses, Exponent, Multiplication/Division, Addition/Subtraction

expr1 = 2 + 3 * 4
expr2 = (2 + 3) * 4

print("Without parentheses:", expr1)
print("With parentheses:", expr2)

# Output:
# Without parentheses: 14
# With parentheses: 20


print("\n# -----------------------------")
print("# 7. PRACTICAL MINI-EXAMPLES")
print("# -----------------------------\n")

print("# Example 1 — Checking age range")
age = 17
print("Is teenager?", age >= 13 and age <= 19)

print("\n# Example 2 — Password check")
password = "secret123"
print("Password too short?", len(password) < 8)

print("\n# Example 3 — Calculating discount")
price = 100
discount_rate = 0.2
final_price = price - price * discount_rate
print("Final price:", final_price)

# Example Output:
# Is teenager? True
# Password too short? False
# Final price: 80.0
