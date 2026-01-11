# ============================================================
#        LESSON — SETS (EXTRA METHODS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson continues from sets.py and covers additional
#   set methods not shown in the main lesson.
#
# Contents:
#   1. discard()
#   2. intersection_update()
#   3. difference_update()
#   4. symmetric_difference_update()
#
print("\n# -----------------------------")
print("# 1. discard()")
print("# -----------------------------\n")

# discard() removes an item if present; no error if missing.
colors = {"red", "green", "blue"}
colors.discard("green")
colors.discard("missing")  # no error
print(colors)

print("\n# -----------------------------")
print("# 2. intersection_update()")
print("# -----------------------------\n")

a = {1, 2, 3, 4}
b = {3, 4, 5}
a.intersection_update(b)
print(a)  # {3, 4}

print("\n# -----------------------------")
print("# 3. difference_update()")
print("# -----------------------------\n")

a = {1, 2, 3, 4}
b = {3, 4, 5}
a.difference_update(b)
print(a)  # {1, 2}

print("\n# -----------------------------")
print("# 4. symmetric_difference_update()")
print("# -----------------------------\n")

a = {1, 2, 3}
b = {3, 4, 5}
a.symmetric_difference_update(b)
print(a)  # {1, 2, 4, 5}
