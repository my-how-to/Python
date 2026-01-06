# ============================================================
#              MULTIPLE ASSIGNMENT & UNPACKING
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains Python's multiple assignment feature:
#       - assigning several variables at once
#       - unpacking tuples, lists, and other iterables
#       - swapping values without a temporary variable
#       - using unpacking in loops, functions, and return values
#
# Contents:
#   1. Basic multiple assignment
#   2. Tuple unpacking
#   3. List and iterable unpacking
#   4. Swapping variables
#   5. Unpacking return values
#   6. Extended unpacking (* operator)
# ============================================================


# ============================================================
# 1. BASIC MULTIPLE ASSIGNMENT
# ============================================================
print("\n--- SECTION 1: Basic multiple assignment ---")

a, b = 10, 20
print("a:", a)
print("b:", b)

# Python packs the right side into a tuple automatically:
# (10, 20) is assigned to (a, b).


# ============================================================
# 2. TUPLE UNPACKING
# ============================================================
print("\n--- SECTION 2: Tuple unpacking ---")

t = (1, 2, 3)
x, y, z = t
print("x:", x)
print("y:", y) 
print("z:", z)

# Important: the number of variables must match the number of elements.
# If they don't match, Python raises a ValueError.
## Example:
try:
    a, b = (1, 2, 3)  # Raises ValueError: too many values to unpack
except ValueError as e:
    print("Error:", e)
# If you want to ignore some values, you can use an underscore:
_, b, _ = (1, 2, 3)  # b will be
print("b (ignored others):", b) # Output: b (ignored others): 2

# ============================================================
# 3. LIST AND ITERABLE UNPACKING
# ============================================================
print("\n--- SECTION 3: List and iterable unpacking ---")

lst = [4, 5, 6]
a, b, c = lst
print("a:", a, "b:", b, "c:", c)

# Works with any iterable, not just tuples:
s = "OK"
p, q = s
print("p:", p, "q:", q)


# ============================================================
# 4. SWAPPING VARIABLES (PYTHONIC SWAP)
# ============================================================
print("\n--- SECTION 4: Swapping variables ---")

a = 2
b = 3
print("Before swap:", a, b) # Output: Before swap: 2 3

# Python creates a tuple (b, a) and unpacks it into (a, b)
a, b = b, a
print("After swap:", a, b) # Output: After swap: 3 2


# ============================================================
# 5. UNPACKING RETURN VALUES
# ============================================================
print("\n--- SECTION 5: Unpacking return values ---")

def min_and_max(values):
    return min(values), max(values)  # returns a tuple

mn, mx = min_and_max([3, 7, 1, 9])
print("min:", mn, "max:", mx)


# ============================================================
# 6. EXTENDED UNPACKING (* OPERATOR)
# ============================================================
print("\n--- SECTION 6: Extended unpacking ---")

a, *middle, b = [1, 2, 3, 4, 5]
print("a:", a)
print("middle:", middle)
print("b:", b)

# * collects all remaining items into a list.
