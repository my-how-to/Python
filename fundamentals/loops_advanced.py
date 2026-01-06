# ============================================================
#            LESSON — LOOPS (ADVANCED)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson builds on loops_intro.py with more detailed
#   control-flow techniques and best practices.
#
# Contents:
#   1. For loops
#   2. While loops
#   3. break
#   4. continue
#   5. break + continue combined
#   6. Nested loops
#   7. Loop else clause
#   8. enumerate()
#   9. Looping through dictionaries
#  10. Best practices
# 
# ============================================================

print("\n# -----------------------------")
print("# 1. FOR LOOPS (known repetitions)")
print("# -----------------------------\n")

for i in range(5):
    print("Iteration:", i)

# Output:
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4


# Loop through a string
for letter in "Python":
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

print("\n# -----------------------------")
print("# 2. WHILE LOOPS (unknown count) - printing OUTSIDE the loop")
print("# -----------------------------\n")

count = 0

while count < 3:
    print("Count is:", count)
    count += 1

# Output:
# Count is: 0
# Count is: 1
# Count is: 2

# WARNING:
# while True → infinite loop unless break is used.

print("\n# -----------------------------")
print("# 2.1 Example — printing OUTSIDE the loop (final value printed after the loop finishes)")
print("# -----------------------------\n")

count = 0

while count < 3:
    count += 1
print("Final count:", count)

# Output:
# Final count: 3

print("\n# -----------------------------")
print("# 3. BREAK STATEMENT")
print("# -----------------------------\n")

for i in range(10):
    if i == 5:
        break  # stops loop completely
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4



print("\n# -----------------------------")
print("# 4. CONTINUE STATEMENT")
print("# -----------------------------\n")

for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9



print("\n# -----------------------------")
print("# 5. BREAK + CONTINUE (combined example)")
print("# -----------------------------\n")

commands = ["run", "skip", "jump", "invalid", "exit", "run"]

for cmd in commands:
    if cmd == "invalid":
        continue  # skip invalid commands
    if cmd == "exit":
        break      # stop processing
    print("Processing:", cmd)

# Output:
# Processing: run
# Processing: skip
# Processing: jump



print("\n# -----------------------------")
print("# 6. NESTED LOOPS")
print("# -----------------------------\n")

# Multiplication table
for a in range(1, 4):
    for b in range(1, 4):
        print(f"{a} x {b} = {a*b}")
    print("---")

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ---
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ---
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ---



print("\n# -----------------------------")
print("# 7. LOOP ELSE CLAUSE")
print("# -----------------------------\n")

numbers = [3, 5, 7, 9]
target = 7

for n in numbers:
    if n == target:
        print("Found:", n)
        break
else:
    print("Item not found")

# Output:
# Found: 7



print("\n# -----------------------------")
print("# 8. ENUMERATE (index looping)")
print("# -----------------------------\n")

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry



print("\n# -----------------------------")
print("# 9. LOOPING THROUGH DICTIONARIES")
print("# -----------------------------\n")

person = {"name": "Alex", "age": 30, "city": "Chisinau"}

# Loop keys
for key in person:
    print("Key:", key)

# Loop values
for value in person.values():
    print("Value:", value)

# Loop key + value
for key, value in person.items():
    print(key, "→", value)



# ================================
# 10. BEST PRACTICES & MISTAKES
# ================================

# - Do NOT modify a list while iterating over it.
# - Use enumerate() instead of range(len()).
# - Avoid infinite loops unless intended.
# - Use break to prevent unnecessary iterations.
# - continue is useful but avoid overuse.
# - for is preferred over while unless you need unknown repetitions.
