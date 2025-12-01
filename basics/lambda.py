# ============================================================
#            LESSON 10.2 — LAMBDA FUNCTIONS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains lambda functions in Python: what they
#   are, basic syntax, differences from normal functions, and
#   practical uses with map(), filter(), and sorted().
#
# Contents:
#   1. What is a lambda function?
#   2. Basic syntax
#   3. Lambdas vs normal functions
#   4. Using lambdas with map()
#   5. Using lambdas with filter()
#   6. Using lambdas with sorted()
#   7. Practical mini-examples
#
# ============================================================


print("\n# -----------------------------")
print("# 1. WHAT IS A LAMBDA FUNCTION?")
print("# -----------------------------\n")

# A lambda function is a small anonymous function.
# It is used for short, throwaway operations.

# Regular function:
def square_normal(x):
    return x * x

# Lambda version:
square_lambda = lambda x: x * x

print("Normal:", square_normal(4))
print("Lambda:", square_lambda(4))

# Output:
# Normal: 16
# Lambda: 16


print("\n# -----------------------------")
print("# 2. BASIC SYNTAX")
print("# -----------------------------\n")

# lambda arguments: expression

add = lambda a, b: a + b
print("5 + 7 =", add(5, 7))

# Output:
# 5 + 7 = 12


print("\n# -----------------------------")
print("# 3. LAMBDA VS NORMAL FUNCTION")
print("# -----------------------------\n")

# Normal function (better for complex logic)
def multiply(a, b):
    result = a * b
    return result

# Lambda (best for SHORT, SIMPLE logic)
multiply_lambda = lambda a, b: a * b

print("Normal multiply:", multiply(3, 4))
print("Lambda multiply:", multiply_lambda(3, 4))

# Output:
# Normal multiply: 12
# Lambda multiply: 12


print("\n# -----------------------------")
print("# 4. LAMBDAS WITH map()")
print("# -----------------------------\n")

numbers = [1, 2, 3, 4]

# Doubles each number
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# Output:
# Doubled: [2, 4, 6, 8]


print("\n# -----------------------------")
print("# 5. LAMBDAS WITH filter()")
print("# -----------------------------\n")

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# Output:
# Evens: [2, 4]


print("\n# -----------------------------")
print("# 6. LAMBDAS WITH sorted()")
print("# -----------------------------\n")

students = [
    ("Alex", 3),
    ("Maria", 5),
    ("John", 2)
]

# Sort by score (2nd element)
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by score:", sorted_students)

# Output:
# Sorted by score: [('John', 2), ('Alex', 3), ('Maria', 5)]


print("\n# -----------------------------")
print("# 7. PRACTICAL MINI-EXAMPLES")
print("# -----------------------------\n")

print("# Example 1 — Getting last character")
last_char = lambda s: s[-1]
print("Last char of 'Python':", last_char("Python"))

print("\n# Example 2 — Calculating price with tax")
price_with_tax = lambda price, tax: price + price * tax
print("Price 100 + 20% tax =", price_with_tax(100, 0.20))

print("\n# Example 3 — Quick if/else in lambda")
check_age = lambda age: "Adult" if age >= 18 else "Minor"
print("Age 17:", check_age(17))

# Example Output:
# Last char of 'Python': n
# Price 100 + 20% tax = 120.0
# Age 17: Minor
