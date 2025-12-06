# ============================================================
#            LESSON — LISTS (COLLECTIONS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson covers lists in Python: what they are, how to
#   create them, accessing and modifying items, useful list
#   methods, looping through lists, list comprehensions, and
#   nested lists.
#   
#   Collections let you store multiple values in one variable,
#   such as a group of numbers, words, or even objects.
# 
# Contents:
#   1. Lists — the Most Common Collection
#   2. Useful List Functions
#   3. Nested Lists (Lists Inside Lists)
#
# ============================================================
# 1) Lists — the Most Common Collection
# ============================================================
print("\n--- SECTION 1: Lists — the Most Common Collection ---")

# A list is an ordered, changeable (mutable) collection.
fruits = ["apple", "banana", "cherry"]

# You can store any type of data inside:
mixed = [10, "hello", True, 3.14]

# ------------------------------------------------------------
# Accessing List Items (zero-indexed)
# ------------------------------------------------------------
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # cherry (last item). See more in negative_indices.py

# ------------------------------------------------------------
# Slicing Lists 
# ------------------------------------------------------------
# Slicing returns a portion of the list. 

# list[start : stop]
# start → index where the slice begins (inclusive)
# stop → index where the slice ends (exclusive)

print(fruits[0:2])   # ['apple', 'banana'] this makes slicing predictable -> 2 items
print(fruits[:2])    # ['apple', 'banana'] So the second number (2) is NOT included in the result.
print(fruits[1:])    # ['banana', 'cherry']
print(fruits[::-1])  # reversed list

# ------------------------------------------------------------
# Changing Items
# ------------------------------------------------------------
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']

# ------------------------------------------------------------
# Adding Items
# ------------------------------------------------------------
fruits.append("mango")     # adds to the end
fruits.insert(1, "pear")   # adds at position 1
print(fruits)  # ['apple', 'pear', 'orange', 'cherry', 'mango']

# ------------------------------------------------------------
# Removing Items
# ------------------------------------------------------------
fruits.remove("cherry")
print(fruits)

# Or remove by index:
fruits.pop(0)  # removes first item
print(fruits)

# Remove last item:
fruits.pop()
print(fruits)

# ------------------------------------------------------------
# Looping Through a List
# ------------------------------------------------------------
for fruit in fruits:
    print(f"I like {fruit}")

# Loop with index:
for index, fruit in enumerate(fruits):
    print(index, fruit)

# ------------------------------------------------------------
# Getting List Length
# ------------------------------------------------------------
print(len(fruits))  # number of elements

# ------------------------------------------------------------
# Checking Membership
# ------------------------------------------------------------
print("apple" in fruits)     # True / False

# ------------------------------------------------------------
# Aliasing vs independent lists
# ------------------------------------------------------------
# Assigning one list variable to another does NOT copy; both names point to same object.
x = [1, 2, 3]
y = x
y.append(4)
print("x after y.append:", x)  # [1, 2, 3, 4] → x and y reference the same list

# ============================================================
# 2) Useful List Functions
# ============================================================
print("\n--- SECTION 2: Useful List Functions ---")

numbers = [4, 1, 8, 2, 9]
print(max(numbers))  # 9
print(min(numbers))  # 1
print(sum(numbers))  # 24

numbers.sort()
print(numbers)      # [1, 2, 4, 8, 9]

numbers.sort(reverse=True)
print(numbers)      # [9, 8, 4, 2, 1]

# ------------------------------------------------------------
# Copying Lists
# ------------------------------------------------------------
nums_copy = numbers.copy()
print(nums_copy)    # [9, 8, 4, 2, 1]

# ------------------------------------------------------------
# List Comprehensions
# ------------------------------------------------------------
# Create a list of squares
squares = [n * n for n in numbers]
print(squares)      # [81, 64, 16, 4, 1]

# Filter even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers) # [8, 2]

# List repetition duplicates the list content N times.
print([1, 2] * 2)   # [1, 2, 1, 2]
print([1, 2] * 4)   # [1, 2, 1, 2, 1, 2, 1, 2]

# ============================================================
# 3) Nested Lists (Lists Inside Lists)
# ============================================================
print("\n--- SECTION 3: Nested Lists ---")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6

# Looping through nested lists
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
