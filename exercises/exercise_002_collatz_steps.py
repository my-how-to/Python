# ============================================================
#                EXERCISE 002 — COLLATZ STEPS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise (while-loop practice):
#   Read a non-zero positive integer from the user.
#   If the number is even, divide it by 2.
#   If the number is odd, multiply by 3 and add 1.
#   Repeat until the number becomes 1.
#   Print every step and the total number of steps.
#
# Solution:
#   Use a while loop that runs until the number hits 1.
#   Update the value using the even/odd rule and count steps.
# ============================================================


# ------------------------------------------------------------
# WHILE-LOOP SOLUTION
# ------------------------------------------------------------
# The loop continues until the value reaches 1, printing
# each step so the sequence is visible.

number = int(input("write a non zero positive number: "))

step = 0

while number != 1:
    if number % 2 == 0:
        number //= 2            # integer division for even numbers
    else:
        number = 3 * number + 1

    step += 1
    print(step, number)

print("Done in", step, "steps.")
