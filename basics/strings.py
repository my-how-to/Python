# ============================================================
#            LESSON — STRINGS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains Python strings: what they are, how to
#   create them, indexing and slicing, useful methods, searching,
#   replacing, splitting/joining, trimming, formatting with
#   f-strings, escaping characters, and multi-line strings.
#
# Contents:
#   1. Strings are immutable
#   2. Indexing and slicing
#   3. Useful string methods
#   4. Searching inside strings
#   5. Replacing text
#   6. Splitting and joining
#   7. Trimming whitespace
#   8. Checking prefixes/suffixes
#   9. F-strings and formatting
#   10. Escaping characters
#   11. Multi-line strings
#   12. String operators (+ and *)
#
# ============================================================


print("\n# -----------------------------")
print("# 1. STRINGS ARE IMMUTABLE")
print("# -----------------------------\n")

s = "Python"
print(s)

# You CANNOT change characters like this:
# s[0] = "J"   # <-- error!

# But you can create a new string:
s2 = "J" + s[1:]
print(s2)

# Output:
# Python
# Jython


print("\n# -----------------------------")
print("# 2. INDEXING AND SLICING")
print("# -----------------------------\n")

text = "Hello, world!"

print("First char:", text[0])   # First char: H
print("Last char:", text[-1])   # Last char: !

print("Slice (0:5):", text[0:5])    # Slice (0:5): Hello
print("Slice (:5):", text[:5])      # Slice (:5): Hello
print("Slice (7:):", text[7:])      # Slice (7:): world!

print("Every second char:", text[::2])  # Every second char: Hlo ol!


print("\n# -----------------------------")
print("# 3. USEFUL STRING METHODS")
print("# -----------------------------\n")

name = "alex"

print("Upper:", name.upper())               # Upper: ALEX
print("Lower:", name.lower())               # Lower: alex
print("Title:", name.title())               # Title: Alex
print("Swapcase:", name.swapcase())         # Swapcase: ALEX
print("Capitalized:", name.capitalize())    # Capitalized: Alex


print("\n# -----------------------------")
print("# 4. SEARCHING INSIDE STRINGS")
print("# -----------------------------\n")

text = "bananas are yellow"

print("Index of 'a':", text.find("a"))   # first occurrence
print("Last index of 'a':", text.rfind("a"))
print("Count of 'a':", text.count("a"))
print("Contains 'yellow'?", "yellow" in text)

# Output:
# Index of 'a': 1
# Last index of 'a': 13
# Count of 'a': 4
# Contains 'yellow'? True


print("\n# -----------------------------")
print("# 5. REPLACING TEXT")
print("# -----------------------------\n")

sentence = "I like apples"
print(sentence.replace("apples", "bananas"))

# Output:
# I like bananas


print("\n# -----------------------------")
print("# 6. SPLITTING AND JOINING")
print("# -----------------------------\n")

csv_line = "Alex,25,QA"

parts = csv_line.split(",")
print("Split:", parts)

joined = "-".join(parts)
print("Joined:", joined)

# Output:
# Split: ['Alex', '25', 'QA']
# Joined: Alex-25-QA


print("\n# -----------------------------")
print("# 7. TRIMMING WHITESPACE")
print("# -----------------------------\n")

messy = "   Python   "

print("Strip:", messy.strip())
print("Lstrip:", messy.lstrip())
print("Rstrip:", messy.rstrip())

# Output:
# Strip: Python
# Lstrip: Python   
# Rstrip:    Python


print("\n# -----------------------------")
print("# 8. CHECKING PREFIXES/SUFFIXES")
print("# -----------------------------\n")

file = "report.pdf"

print("Ends with .pdf?", file.endswith(".pdf"))
print("Starts with rep?", file.startswith("rep"))

# Output:
# Ends with .pdf? True
# Starts with rep? True


print("\n# -----------------------------")
print("# 9. F-STRINGS AND FORMATTING")
print("# -----------------------------\n")

name = "Alex"
age = 30

print(f"My name is {name} and I am {age} years old.")

# Formatting expressions:
print(f"5 + 7 = {5 + 7}")
print(f"Pi approx = {3.14159:.2f}")

# Output:
# My name is Alex and I am 30 years old.
# 5 + 7 = 12
# Pi approx = 3.14


print("\n# -----------------------------")
print("# 10. ESCAPING CHARACTERS")
print("# -----------------------------\n")

print("He said \"Hello\"")
print("Path: C:\\new_folder\\test")

# Output:
# He said "Hello"
# Path: C:\new_folder\test


print("\n# -----------------------------")
print("# 11. MULTI-LINE STRINGS")
print("# -----------------------------\n")

multi = """This is a
multi-line
string."""
print(multi)

# Output:
# This is a
# multi-line
# string.


print("\n# -----------------------------")
print("# 12. STRING OPERATORS (+ AND *)")
print("# -----------------------------\n")

greeting = "Hello, " + "world!"
print("Concatenation:", greeting)   # Hello, world!

echo = "ha" * 3
print("Repetition:", echo)          # hahaha

# A number less than or equal to zero produces an empty string.
print("Zero repeat:", "ha" * 0)       # Zero repeat:  (empty string)
print("Negative repeat:", "ha" * -2)  # Negative repeat:  (empty string)

# Drawing a simple rectangle using concatenation and repetition
top_bottom = "+" + "-" * 10 + "+"
side = "|" + " " * 10 + "|\n"

print(top_bottom)
print(side * 5, end="")
print(top_bottom)

# +----------+
# |          |
# |          |
# |          |
# |          |
# |          |
# +----------+

# Right-aligned triangle using repetition
height = 5
for row in range(1, height + 1):
    spaces = " " * (height - row)   # spaces
    stars = "*" * row               # stars
    print(spaces + stars)           # print the row

#     *
#    **
#   ***
#  ****
# *****
