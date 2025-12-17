# ============================================================
#        LESSON — OCTAL & HEXADECIMAL INTEGERS IN PYTHON
# ============================================================
# Author: Alexandru Petrenco (with AI assistance)
# 
# Description:
#   This lesson explains how octal (base-8) and hexadecimal
#   (base-16) integers work in Python, why they exist, and
#   when to use them in real-world scenarios.
#
# Topics covered:
#   1. Integer bases and prefixes
#   2. Octal integers (0o)
#   3. Hexadecimal integers (0x)
#   4. Real-world use cases
#   5. Conversions between bases
#   6. Common mistakes and exam tips
#
# ============================================================


print("\n# -----------------------------")
print("# 1. Integer bases overview")
print("# -----------------------------\n")

# Python supports multiple ways to write integers

decimal = 42      # base 10 (default)
binary  = 0b101010
_octal  = 0o52
hexadec = 0x2A

print(decimal, binary, _octal, hexadec)  # all are equal


print("\n# -----------------------------")
print("# 2. Octal integers")
print("# -----------------------------\n")

# Octal numbers use digits 0–7 and must start with 0o

octal_value = 0o12
print(octal_value)        # 10 in decimal

# Common real-world use: file permissions (Unix / Linux)

# 0o7 (7 decimal) = read + write + execute
# 0o5 (5 decimal) = read + execute
# 0o4 (4 decimal) = read only

file_permissions = 0o755
print(file_permissions)


print("\n# -----------------------------")
print("# 3. Hexadecimal integers")
print("# -----------------------------\n")

# Hex digits: 0–9 and A–F (case-insensitive)

hex_value = 0x1A
print(hex_value)          # 26 in decimal

# Hex is compact and aligns with binary (4 bits per hex digit)


print("\n# -----------------------------")
print("# 4. Hex use cases")
print("# -----------------------------\n")

# 1) Color values (RGB)
white = 0xFFFFFF
red   = 0xFF0000
print(white, red)

# 2) Bit masks and flags
READ  = 0x04
WRITE = 0x02
EXEC  = 0x01

permissions = READ | WRITE
print(permissions)


print("\n# -----------------------------")
print("# 5. Base conversions")
print("# -----------------------------\n")

# From string to integer
print(int("101", 2))     # binary -> decimal
print(int("17", 8))      # octal  -> decimal
print(int("1A", 16))     # hex    -> decimal

# From integer to string representation
print(bin(10))            # '0b1010'
print(oct(10))            # '0o12'
print(hex(10))            # '0xa'


print("\n# -----------------------------")
print("# 6. Rules and pitfalls")
print("# -----------------------------\n")

# Case-insensitive hex
print(0xFF == 0xff)       # True

# Arithmetic ignores base notation
print(0x10 + 0o10)        # 16 + 8 = 24

# Invalid digits raise SyntaxError (examples below are commented)
# 0o8     # invalid octal digit
# 0xG     # invalid hex digit
# 0b102   # invalid binary digit
# Leading zeros are not allowed in decimal literals

print("\n# -----------------------------")
print("# EXERCISE: Octal & Hexadecimal")
print("# -----------------------------\n")


# Display octal values from 0 to 20
print("Octal values from 0 to 20:")
for i in range(21):
    print(i, oct(i))

# Display hexadecimal values from 0 to 20
print("hexadecimal values from 0 to 20:")
for i in range(21):
    print(i, hex(i))
    