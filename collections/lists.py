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
print("\n# -----------------------------")
print("# 1. Lists — the Most Common Collection")
print("# -----------------------------\n")

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
print(fruits[::-1])  # ['cherry', 'banana', 'apple'] (reverses the list)
# slicing with negative step skips every other from the end
print(list(range(5))[::-2])  # [4, 2, 0]

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

# Or delete by index with del:
del fruits[0]
# del fruits  # removes the entire list
print(fruits)

# Delete a slice (remove multiple items at once):
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
del fruits[1:3]
print(fruits)  # ['apple', 'date', 'elderberry']

# ------------------------------------------------------------
# del removes a reference, not necessarily the list object
# ------------------------------------------------------------
original = ["alpha", "beta", "gamma"]
alias = original  # both names point to the same list object
del original      # only deletes the name, not the shared list
print("alias still works after deleting original:", alias)

# If no references remain, the list becomes unreachable and is cleaned up.
temp = [1, 2, 3]
del temp
# temp is no longer defined here.

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
print("kiwi" not in fruits)  # True / False

# ------------------------------------------------------------
# Aliasing vs independent lists
# ------------------------------------------------------------
# Assigning one list variable to another does NOT copy; both names point to same object.
x = [1, 2, 3]
y = x
y.append(4)
print("x after y.append:", x)  # [1, 2, 3, 4] → x and y reference the same list
print("y after y.append:", y)  # [1, 2, 3, 4]   

# Rebinding creates a new list object, leaving aliases untouched.
x = [1, 2, 3]
y = x
x = x + [4]  # new list produced; x now points to a different object
print("y stays referencing the original list:", y)  # [1, 2, 3]
print("x now points to a new list:", x)             # [1, 2, 3, 4]

# In-place operators mutate the existing list, so aliases see the change.
x = [1, 2, 3]
y = x
x += [4]  # extends the original object instead of rebinding
print("y also sees the appended value due to shared reference:", y)     # [1, 2, 3, 4]
print("x references the same list object as y:", x is y)                # True

# NOTE: For numbers, x = x + 1 and x += 1 are equivalent because ints are immutable.
# With lists, x += [value] performs in-place modification (like list.extend),
# and x = x + [value] builds a brand-new list, which is why aliases behave differently.


print("\n# -----------------------------")
print("# 2. Useful List Functions")
print("# -----------------------------\n")

numbers = [4, 1, 8, 2, 9]
print(max(numbers))  # 9
print(min(numbers))  # 1
print(sum(numbers))  # 24

numbers.sort()
print("Sorted ascending:", numbers)      # [1, 2, 4, 8, 9]

# Sort in reverse order
numbers.sort(reverse=True)
print("Sorted descending:", numbers)      # [9, 8, 4, 2, 1]

# Reverse the list order without sorting (same goal as slicing with step -1).
numbers.reverse()   # [1, 2, 4, 8, 9]
print("Reversed:", numbers)

# ------------------------------------------------------------
# Copying Lists (same goal as slicing a[:])
# ------------------------------------------------------------
# Two common shallow-copy options:
a = [1, 2, 3]
b = a[:]  # slicing
b.append(4)
print("a stays the same, b gets the new item:", a, b)   # a: [1, 2, 3], b: [1, 2, 3, 4]

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

# Be cautious with nested mutable objects:
triplicated = [[]] * 3
print(triplicated, "len:", len(triplicated)) # [[], [], []] len: 3
# All three references point to the same inner list object.
# for example, modifying one modifies all:
triplicated[0].append("wow")
print(triplicated, "len:", len(triplicated)) # [['wow'], ['wow'], ['wow']]

# To create independent inner lists, use a list comprehension:
independent = [[] for _ in range(3)]
print(independent, "len:", len(independent)) # [[], [], []] len: 3
# Now modifying one does not affect the others:
independent[0].append("wow")
print(independent, "len:", len(independent)) # [['wow'], [], []]    

triplicated[0].append("wow")
print("Appending via one reference touches all:", triplicated)


print("\n# -----------------------------")
print("# 3. Nested Lists (Lists Inside Lists)")
print("# -----------------------------\n")

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
