# ============================================================
#        LESSON — RESERVED KEYWORDS (PYTHON LANGUAGE)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson introduces Python reserved keywords like `in`,
#   explains what they are, and shows how they behave in code.
#
# Contents:
#   1. What are reserved keywords?
#   2. Popular keywords list
#   3. Membership and `in`
#   4. `in` with loops
#   5. Common keywords in action
#   6. Why keywords cannot be used as names
#
# ------------------------------------------------------------
# 1. What are reserved keywords?
# ------------------------------------------------------------

# Keywords are language-reserved words with special meaning.
# They cannot be used as variable, function, or class names.

# ------------------------------------------------------------
# 2. Popular keywords list
# ------------------------------------------------------------

# Common, beginner-friendly keywords you will see often:
# and, or, not, in, is, if, elif, else, for, while, break, continue,
# def, return, class, try, except, finally, with, as, import, from,
# True, False, None, pass

print("\n# -----------------------------")
print("# 3. Membership and `in`")
print("# -----------------------------\n")

# `in` checks membership in sequences and collections.
colors = ["red", "green", "blue"]
print("red" in colors)   # True
print("black" in colors) # False

text = "hello world"
print("world" in text)   # True

data = {"name": "Alex", "age": 32}
print("name" in data)    # True (checks keys)

print("\n# -----------------------------")
print("# 4. `in` with loops")
print("# -----------------------------\n")

# `for ... in ...` iterates over items in a sequence or iterable.
for ch in "abc":
    print(ch) # a b c

print("\n# -----------------------------")
print("# 5. Common keywords in action")
print("# -----------------------------\n")

# A few other keywords you will see often:
# if / elif / else
number = 7
if number % 2 == 0:
    print("even")
else:
    print("odd")

# for / break / continue
for n in range(5):
    if n == 2:
        continue
    if n == 4:
        break
    print("n:", n)

# def / return
def add(a, b):
    return a + b

print(add(2, 3))

# ------------------------------------------------------------
# 6. Why keywords cannot be used as names
# ------------------------------------------------------------

# This would be invalid syntax:
# in = 5
# print(in)
