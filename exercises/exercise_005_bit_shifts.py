# ============================================================
#            EXERCISE 005 — BIT SHIFTS AND DOUBLING
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise:
#   Starting from 1, keep doubling the value until it reaches 8.
#   For each step, print "#" and visualize the bits.
#
#   Add the following:
#   - Rewrite without bitwise operators
#   - Visualize the bits
#   - Compare << 1 with * 2
# ============================================================

print("# ------------------------------------------------------------")
print("# Version 1: with bitwise shift")
print("# Each loop prints the value and its 4-bit binary form.")
print("# ------------------------------------------------------------")

val = 1

while val < 8:
    print(f"val: {val} bits: {val:04b}")
    val = val << 1 # Left shift by 1 (equivalent to multiplying by 2)   val= val * 2
   #val = val << 2 # Left shift by 2 (equivalent to multiplying by 4)   val= val * 4


print("# ------------------------------------------------------------")
print("# Version 2: without bitwise operators (use * 2)")
print("# Same output as shifting, but uses multiplication.")
print("# ------------------------------------------------------------")

val = 1

while val < 8:
    print(f"val: {val} bits: {val:04b}")
    val = val * 2


print("# ------------------------------------------------------------")
print("# Comparison: << 1 vs * 2")
print("# Both produce the same numeric result for positive integers.")
print("# ------------------------------------------------------------")

nums = [1, 2, 3, 4, 5, 6, 7]

for n in nums:
    shifted = n << 1
    doubled = n * 2
    print("n:", n, "n<<1:", shifted, "n*2:", doubled)
    # Bits view (8-bit) to visualize the shift
    print("bits:", bin(n)[2:].rjust(8, "0"), "->", bin(shifted)[2:].rjust(8, "0"))
