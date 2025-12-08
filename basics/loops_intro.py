# ============================================================
#            LESSON — LOOPS (INTRO)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Essential loop patterns every beginner should know:
#   for/while loops, iterating over sequences, using range(),
#   loop control keywords, nested loops, loop/else, enumerate,
#   zip, and real-world style input validation.
#
# Contents:
#   1. For loops with range()
#   2. Looping over sequences
#   3. While loops
#   4. break and continue
#   5. Loop else clause
#   6. Nested loops
#   7. enumerate() and zip()
#   8. Input validation loop
#   9. Common pitfalls & tips
#
# ============================================================


print("\n# -----------------------------")
print("# 1. FOR LOOPS WITH range()")
print("# -----------------------------\n")

print("FOR loop from 1 to 5 (range is exclusive of the stop value):")
for number in range(1, 6):
    print(number)

# range(start, stop, step) builds an arithmetic progression lazily.

print("\nEven numbers between 0 and 10:")
for even in range(0, 11, 2):
    print(even, end=" ")
print()


print("\n# -----------------------------")
print("# 2. LOOPING OVER SEQUENCES")
print("# -----------------------------\n")

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(f"I like {fruit}")

message = "loop"
for char in message:
    print(char.upper())


print("\n# -----------------------------")
print("# 3. WHILE LOOPS")
print("# -----------------------------\n")

print("While loop countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Lift off!")


print("\n# -----------------------------")
print("# 4. BREAK AND CONTINUE")
print("# -----------------------------\n")

print("BREAK example:")
for i in range(10):
    if i == 5:
        break  # exit the loop entirely
    print(i)

print("\nCONTINUE example:")
for i in range(10):
    if i % 2 == 0:
        continue  # skip to the next iteration
    print(i)  # prints only odd numbers


print("\n# -----------------------------")
print("# 5. LOOP ELSE CLAUSE")
print("# -----------------------------\n")

numbers = [3, 5, 7, 9]
target = 7

for n in numbers:
    if n == target:
        print("Found:", n)
        break
else:
    print("Item not found")

# The else block runs only if the loop was not interrupted by break.


print("\n# -----------------------------")
print("# 6. NESTED LOOPS")
print("# -----------------------------\n")

print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()


print("\n# -----------------------------")
print("# 7. ENUMERATE() AND ZIP()")
print("# -----------------------------\n")

print("Enumerate a list to get index + value:")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

print("\nZip multiple sequences together:")
colors = ["red", "green", "blue"]
hex_codes = ["#FF0000", "#00FF00", "#0000FF"]

for color, hex_code in zip(colors, hex_codes):
    print(color, "→", hex_code)


print("\n# -----------------------------")
print("# 8. INPUT VALIDATION LOOP")
print("# -----------------------------\n")

print("Ask user for a valid number:")

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        number = int(user_input)
        print(f"Thank you! You entered {number}")
        break
    else:
        print("Invalid input, try again.")


# ================================
# 9. COMMON PITFALLS & TIPS
# ================================

# - Avoid while True unless you have a clear break condition.
# - Never modify a list in place while iterating over it; create a copy.
# - Use enumerate() instead of range(len(iterable)) to keep code readable.
# - Prefer for loops when you know the number of iterations in advance.
# - Keep loop bodies small; refactor repeated work into functions.
