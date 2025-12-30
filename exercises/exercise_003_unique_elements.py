# ============================================================
#            EXERCISE 003 — UNIQUE LIST ELEMENTS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise:
#   Given a list with repeated values, build a new list that
#   keeps each element only once, preserving the original order.
#
# Solution:
#   Loop through the original list and append a value only if
#   it is not already in the new list.
# ============================================================

# Example of using the "not in" operator.
numbers = [8, 1, 8, 6, 3, 9, 3, 2, 11, 6]

new_list = []

for value in numbers:
    if value not in new_list:
        new_list.append(value)

print("Unique elements (order preserved):", new_list) 
# [8, 1, 6, 3, 9, 2, 11]

# ------------------------------------------------------------
# Alternative solution using a set
# ------------------------------------------------------------
# Note: Sets do not preserve order.
unique_set = set(numbers)
print("Unique elements with set (order not guaranteed):", unique_set) 
# {1, 2, 3, 6, 8, 9, 11}

# ------------------------------------------------------------
# Alternative solution using dict.fromkeys (order preserved)
# ------------------------------------------------------------
unique_ordered = list(dict.fromkeys(numbers))
print("Unique elements with dict.fromkeys (order preserved):", unique_ordered) 
# [8, 1, 6, 3, 9, 2, 11]

# ------------------------------------------------------------
# Alternative solution using OrderedDict (order preserved)
# ------------------------------------------------------------
from collections import OrderedDict

unique_ordered_alt = list(OrderedDict.fromkeys(numbers))
print("Unique elements with OrderedDict (order preserved):", unique_ordered_alt) 
# [8, 1, 6, 3, 9, 2, 11]
