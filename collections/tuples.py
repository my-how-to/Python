# ============================================================
#            LESSON - TUPLES (COLLECTIONS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson covers tuples in Python: what they are, how to
#   create them, indexing and slicing, immutability, tuple
#   unpacking, single-element tuples, and tuple concatenation.
#
# Contents:
#   1. Tuples — Immutable Sequences
#   2. Tuple Tricks
#   3. Tuple Concatenation  
#  
print("\n# -----------------------------")
print("# 1. Tuples — Immutable Sequences")
print("# -----------------------------\n")

fruits = ("apple", "banana", "cherry")
print(fruits[0])  # apple

# ------------------------------------------------------------
# Looping
# ------------------------------------------------------------
for fruit in fruits:
    print(fruit)

# ------------------------------------------------------------
# Immutability
# ------------------------------------------------------------
# fruits[1] = "orange"  # Error! Tuples are immutable

# ------------------------------------------------------------
# Why use tuples?
# ------------------------------------------------------------
# * Faster and lighter than lists.
# * Ideal for fixed datasets (coordinates, weekdays, etc.).
# * Can serve as dictionary keys or set members.

print("\n# -----------------------------")
print("# 2. Tuple Tricks")
print("# -----------------------------\n")

# ------------------------------------------------------------
# Single-element tuple
# ------------------------------------------------------------
t = ("apple",)
print(type(t))

# ------------------------------------------------------------
# Tuple unpacking
# ------------------------------------------------------------
person = ("Alex", 32, "Moldova")
name, age, country = person
print(name, age, country) # Alex 32 Moldova
print("See /assignment/multiple_assignment.py for advanced packing/unpacking patterns.")

print("\n# -----------------------------")
print("# 3. Tuple Concatenation")
print("# -----------------------------\n")

# Tuples can be joined using +
a = (1, 2, 3)
b = (4, 5)
print(a + b)  # (1, 2, 3, 4, 5)
