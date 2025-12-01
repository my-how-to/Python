# ===========================================
#            LESSON 9.2 - SETS (COLLECTIONS)
# ===========================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson covers sets in Python: what they are, how to
#   create them, adding/removing items, membership testing,
#   and powerful set operations (union, intersection,
#   difference, symmetric difference).
#
# Contents:
#   1. Sets — Unique, Unordered Collections
#   2. Set Operations (Powerful!)
#
# ============================================================
# 1) Sets — Unique, Unordered Collections
# ============================================================

colors = {"red", "green", "blue", "red"}
print(colors)  # {'red', 'green', 'blue'}

# ------------------------------------------------------------
# Adding & Removing Items
# ------------------------------------------------------------
colors.add("yellow")    # add to the set
colors.remove("green")  # remove an existing item
print(colors)

# ------------------------------------------------------------
# Membership Testing
# ------------------------------------------------------------
if "red" in colors:
    print("Yes, red is in the set.")

# ============================================================
# 2) Set Operations (Powerful!)
# ============================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# ------------------------------------------------------------
# Basic Operations
# ------------------------------------------------------------
print(a.union(b))         # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # {3, 4}
print(a.difference(b))    # {1, 2}

# ------------------------------------------------------------
# Additional Useful Operations
# ------------------------------------------------------------
print(a.symmetric_difference(b))  # {1, 2, 5, 6}
print(a.isdisjoint(b))            # False (share 3 and 4)
print(a.issubset(b))              # False
print(a.issuperset(b))            # False
