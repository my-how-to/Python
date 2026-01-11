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
# Why use tuples?
# * Faster and lighter than lists.
# * Ideal for fixed datasets (coordinates, weekdays, etc.).
# * Can serve as dictionary keys or set members.
# * Enable multiple return values from functions.
# * Support unpacking for easy variable assignment.
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
# Tuples without parentheses
# ------------------------------------------------------------
# Parentheses are optional when commas are present.
colors = "red", "green", "blue"
print(colors)

singleton = "only_one",
print(type(singleton))

# ------------------------------------------------------------
# Looping
# ------------------------------------------------------------
# The for-loop is designed for iterating sequences and other iterables.
for fruit in fruits:
    print(fruit)

# ------------------------------------------------------------
# Immutability
# ------------------------------------------------------------
# fruits[1] = "orange"  # Error! Tuples are immutable

print("\n# -----------------------------")
print("# 2. Tuple Tricks")
print("# -----------------------------\n")

# ------------------------------------------------------------
# Single-element tuple
# ------------------------------------------------------------
t = ("apple",)
print(type(t))

# ------------------------------------------------------------
# tuple() constructor
# ------------------------------------------------------------
# tuple() converts other iterables into tuples.
letters = tuple("ABC")
print(letters)  # ('A', 'B', 'C')

nums = tuple([1, 2, 3])
print(nums)  # (1, 2, 3)

# ------------------------------------------------------------
# Tuple unpacking
# ------------------------------------------------------------
person = ("Alex", 32, "Moldova")
name, age, country = person
print(name, age, country) # Alex 32 Moldova
print("See /assignments/multiple_assignment.py for advanced packing/unpacking patterns.")

# ------------------------------------------------------------
# Swapping tuple values (unpacking)
# ------------------------------------------------------------
# Tuple unpacking lets you swap values without a temporary variable.
left = (1,)
middle = (2,)
right = (3,)

left, middle, right = middle, right, left
print(left, middle, right) # (2,) (3,) (1,)

# ------------------------------------------------------------
# Variables inside tuples
# ------------------------------------------------------------
# Tuples can store variables as elements.
level = 42
badge = (3, level)
print(badge) # (3, 42)

# ------------------------------------------------------------
# count() method
# ------------------------------------------------------------
# count() returns how many times a value appears in the tuple.
marks = ("A", "B", "A", "C", "A")
print(marks.count("A"))  # 3

# ------------------------------------------------------------
# index() method
# ------------------------------------------------------------
# index() searches for a value and returns its position.
animals = ("cat", "dog", "cat")
print(animals.index("cat"))  # 0

print("\n# -----------------------------")
print("# 3. Tuple Concatenation")
print("# -----------------------------\n")

# Tuples can be joined using +
a = (1, 2, 3)
b = (4, 5)
print(a + b)  # (1, 2, 3, 4, 5)
