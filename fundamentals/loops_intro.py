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

print("\nWhile loop with break example:")
number = 1
while True:
    print("Inside loop:", number)
    if number == 3:
        break  # exit once condition is met
    number += 1
print(number, "Loop exited via break.") # prints 3 Loop exited via break.


print("\n# -----------------------------")
print("# 4. BREAK AND CONTINUE")
print("# -----------------------------\n")

print("BREAK example:")
for i in range(10):
    if i == 5:
        break  # exit the loop entirely
    print(i) # prints 0 to 4
print(i, "exited the loop at 5") # prints 5 exited the loop at 5

print("\nCONTINUE example:")
for i in range(10):
    if i % 2 == 0: # even number
        continue  # skip to the next iteration
    print(i)  # prints only odd numbers

print("\nPASS example:")
for fruit in fruits:
    if fruit == "banana":
        pass  # placeholder when no action is needed (required syntactically)
    else:
        print(f"Processing {fruit}")
print("PASS lets you leave a block empty without causing an error.")

# The else block runs only if the loop finishes WITHOUT a break.
for i in range(3):
    if i == 1:
        break
else:
    print("OK") # This will NOT print because of the break above.

print("\n# -----------------------------")
print("# 5. LOOP ELSE CLAUSE")
print("# -----------------------------\n")

# The else block on a loop only runs when the loop finishes naturally
# (WITHOUT hitting break). It's perfect for search-style tasks.

print("Example 1 — searching inventory for a target product:")
inventory = ["laptop", "mouse", "keyboard", "monitor"]
target_item = "keyboard"

for item in inventory:
    if item == target_item:
        print(f"{target_item} is in stock.")
        break
else:
    print(f"{target_item} is missing.")

print("\nExample 2 — validating a password list for forbidden words:")
passwords = ["cat123", "welcome", "abc!@#", "safePass90"]
forbidden = {"password", "welcome", "admin"}

for pwd in passwords:
    if pwd in forbidden:
        print(f"Rejected insecure password: {pwd}")
        break
else:
    print("All passwords look acceptable.")

print("\nExample 3 — checking if a number is prime:")
number_to_check = 29
for divisor in range(2, int(number_to_check ** 0.5) + 1):
    if number_to_check % divisor == 0:
        print(number_to_check, "is not prime (divisible by", divisor, ")")
        break
else:
    print(number_to_check, "is prime")

# The else block runs only if the loop was not interrupted by break.
# When you DO break out early, the else block is skipped entirely.

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

# enumerate() is a built-in function that returns 
# an iterator of (index, value) pairs.
print("Enumerate a list to get index + value:")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# zip() is a built-in function that returns 
# an iterator of tuples, pairing items in lockstep.
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
