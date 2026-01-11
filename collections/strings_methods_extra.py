# ============================================================
#        LESSON — STRINGS (EXTRA METHODS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson continues from strings.py and covers additional
#   string methods not shown in the main lesson.
#
# Contents:
#   1. Validation methods
#   2. Case and normalization
#   3. Splitting and partitioning
#   4. Indexing and padding
#   5. Prefix/suffix edits
#   6. Encoding and translation
#   7. format_map() and expandtabs()
#
print("\n# -----------------------------")
print("# 1. Validation methods")
print("# -----------------------------\n")

text = "Python3"
print(text.isalpha())      # False (digits present)
print(text.isalnum())      # True
print(text.isidentifier()) # True
print("123".isdecimal())   # True
print("123".isnumeric())   # True
print("  ".isspace())      # True
print("ABC".isupper())     # True
print("abc".islower())     # True
print("Hello".istitle())   # True
print("Hi!".isprintable()) # True
print("A".isascii())       # True

print("\n# -----------------------------")
print("# 2. Case and normalization")
print("# -----------------------------\n")

print("MIXED".casefold())  # strong lowercasing

print("\n# -----------------------------")
print("# 3. Splitting and partitioning")
print("# -----------------------------\n")

line = "a,b,c,d"
print(line.rsplit(",", 1))   # split from the right

path = "root/home/user"
print(path.partition("/"))   # ('root', '/', 'home/user')
print(path.rpartition("/"))  # ('root/home', '/', 'user')

print("\n# -----------------------------")
print("# 4. Indexing and padding")
print("# -----------------------------\n")

word = "banana"
print(word.rindex("na"))  # last index, raises if missing
print(word.zfill(8))      # '00banana'
print(word.ljust(10, "."))  # 'banana....'
print(word.center(10, "-")) # '--banana-'

print("\n# -----------------------------")
print("# 5. Prefix/suffix edits")
print("# -----------------------------\n")

title = "unhappy.txt"
print(title.removeprefix("un"))  # 'happy.txt'
print(title.removesuffix(".txt")) # 'unhappy'

print("\n# -----------------------------")
print("# 6. Encoding and translation")
print("# -----------------------------\n")

message = "price: $5"
encoded = message.encode("utf-8")
print(encoded)

table = str.maketrans({"$": "USD "})
print(message.translate(table))  # 'price: USD 5'

print("\n# -----------------------------")
print("# 7. format_map() and expandtabs()")
print("# -----------------------------\n")

template = "{name} scored {score:.1f}"
data = {"name": "Alex", "score": 9.25}
print(template.format_map(data))

tabbed = "A\tB\tC"
print(tabbed.expandtabs(4))
