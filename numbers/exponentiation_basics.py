# ============================================================
#              EXPONENTIATION — PYTHON BASICS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains exponentiation from both:
#       - mathematical perspective
#       - Python implementation perspective using the ** operator
#
#   It covers:
#       - basic powers
#       - zero and negative exponents
#       - power rules
#       - fractional exponents (roots)
#       - operator precedence and associativity
#
# Contents:
#   1. What exponentiation means
#   2. Basic powers
#   3. Zero and power of one
#   4. Negative exponents
#   5. Power rules (multiply, divide, power of a power)
#   6. Fractional exponents (roots)
#   7. Operator precedence
#   8. Right-to-left associativity of **
# ============================================================


print("\n# -----------------------------")
print("# 1. Meaning of exponentiation")
print("# -----------------------------\n")

# a ** b means:
# a multiplied by itself b times
print("2 ** 3 =", 2 ** 3)   # 2 * 2 * 2 = 8
print("5 ** 2 =", 5 ** 2)   # 25


print("\n# -----------------------------")
print("# 2. Basic powers")
print("# -----------------------------\n")

print("10 ** 1 =", 10 ** 1)
print("7 ** 2  =", 7 ** 2)
print("4 ** 3  =", 4 ** 3)


print("\n# -----------------------------")
print("# 3. Zero and power of one")
print("# -----------------------------\n")

print("5 ** 0 =", 5 ** 0)   # always 1
print("9 ** 1 =", 9 ** 1)   # returns the base


print("\n# -----------------------------")
print("# 4. Negative exponents")
print("# -----------------------------\n")

print("2 ** -1 =", 2 ** -1)    # 1 / 2
print("10 ** -2 =", 10 ** -2)  # 1 / 100


print("\n# -----------------------------")
print("# 5. Power rules")
print("# -----------------------------\n")

# a^m * a^n = a^(m+n)
print("2**3 * 2**2 =", 2**3 * 2**2)

# a^m / a^n = a^(m-n)
print("2**5 / 2**2 =", 2**5 / 2**2)

# (a^m)^n = a^(m*n)
print("(2**3)**2 =", (2**3)**2)


print("\n# -----------------------------")
print("# 6. Fractional exponents (roots)")
print("# -----------------------------\n")

# Square root
print("9 ** 0.5  =", 9 ** 0.5)

# Cube root
print("8 ** (1/3) =", 8 ** (1/3))

# General fractional power
print("16 ** (3/2) =", 16 ** (3/2))


print("\n# -----------------------------")
print("# 7. Operator precedence")
print("# -----------------------------\n")

# Exponentiation is evaluated before addition
print("2 + 3 ** 2 =", 2 + 3 ** 2)
print("(2 + 3) ** 2 =", (2 + 3) ** 2)


print("\n# -----------------------------")
print("# 8. Right-to-left associativity of **")
print("# -----------------------------\n")

# ** is evaluated from RIGHT to LEFT
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)

# This is equivalent to:
print("2 ** (3 ** 2) =", 2 ** (3 ** 2))

# But NOT the same as:
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)
