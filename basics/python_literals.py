# ============================================================
#             LESSON — PYTHON LITERALS OVERVIEW
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Walks through every literal family in Python and clarifies how the
#   interpreter reads them: numeric forms, strings and bytes, booleans
#   and None, plus collection literals like lists and dictionaries.
#   Highlights readability helpers such as underscores and raw strings.
#
# Contents:
#   1. Literal fundamentals
#   2. Numeric literals (int, float, complex)
#   3. Text & bytes literals
#   4. Boolean and None literals
#   5. Collection literals
#   6. Literal expressions vs constructors
#
# ============================================================


print("\n# -----------------------------")
print("# 1. Literal fundamentals")
print("# -----------------------------\n")

# A literal is a direct value in source code; Python reads it as-is without executing functions.
answer = 42             # integer literal
pi = 3.1415            # float literal
name = "Ada"          # string literal
print("answer:", answer, type(answer))
print("pi:", pi, type(pi))
print("name:", name, type(name))

# Literals can appear inside larger expressions but they themselves are fixed values.
print("answer + 8:", answer + 8)


print("\n# -----------------------------")
print("# 2. Numeric literals")
print("# -----------------------------\n")

# Integers include decimal, binary, octal, hex, and underscore groupings for readability.
print("decimal 255:", 255)
print("binary 0b11111111:", 0b11111111)
print("octal 0o377:", 0o377)
print("hex 0xFF:", 0xFF)
print("underscores in 1_000_000:", 1_000_000)

# Floats support standard and scientific notation.
float_val = 0.5
sci_val = 6.02e23
print("float:", float_val)
print("scientific:", sci_val)

# Complex numbers use the suffix j.
print("complex literal (3+4j):", 3 + 4j)
print("imaginary-only literal 5j:", 5j)


print("\n# -----------------------------")
print("# 3. Text & bytes literals")
print("# -----------------------------\n")

# Strings can be single-, double-, or triple-quoted, and raw strings keep backslashes literal.
regular = "Line 1\nLine 2"
triple = """Multi-line\nliteral"""
raw_path = r"C:\\new_folder\\file.txt"
print("regular string shows newline:")
print(regular)
print("triple-quoted string:")
print(triple)
print("raw string path:", raw_path)

# Bytes literals prefix text with b and stay limited to byte values (0-255).
packet = b"HTTP/1.1\r\n"
print("bytes literal:", packet)
print("bytes contents:", list(packet))


print("\n# -----------------------------")
print("# 4. Boolean and None literals")
print("# -----------------------------\n")

# True, False, and None each have single canonical objects.
is_enabled = True
is_deleted = False
placeholder = None
print("is_enabled:", is_enabled, type(is_enabled))
print("is_deleted:", is_deleted, type(is_deleted))
print("placeholder is None?", placeholder is None)

# Boolean literals combine with logical operators to produce new booleans.
print("True and False:", True and False)    # False
print("True or False:", True or False)      # True
print("not True:", not True)                # False

# None is a singleton; use "is" for identity checks.
missing_value = None
print("missing_value is None:", missing_value is None)
print("None == None:", None == None)
print("None is None:", None is None)

# None participates in logical expressions (it behaves like False in boolean context).
print("None and True:", None and True)   # None
print("None or 'fallback':", None or "fallback")


print("\n# -----------------------------")
print("# 5. Collection literals")
print("# -----------------------------\n")

# Lists, tuples, sets, and dicts all support literal notation for inline data structures.
fruits = ["apple", "kiwi", "plum"]
coords = (10, 20)
flags = {"debug", "verbose"}
config = {"host": "localhost", "port": 5432}
print("list literal:", fruits)
print("tuple literal:", coords)
print("set literal:", flags)
print("dict literal:", config)

# Empty set must use set(); {} creates an empty dict literal by design.
empty_set = set()
empty_dict = {}
print("empty_set via constructor:", empty_set)
print("empty_dict literal:", empty_dict)


print("\n# -----------------------------")
print("# 6. Literal expressions vs constructors")
print("# -----------------------------\n")

# Literal syntax is evaluated at compile time, while constructors run at runtime and can include logic.
literal_list = [1, 2, 3]
constructed_list = list((1, 2, 3))
print("literal_list:", literal_list)
print("constructed_list:", constructed_list)

# Comprehensions are not literals even though they appear inline—they execute code to generate values.
comp = [n * n for n in range(3)]
print("comprehension result (runtime-built):", comp)

print("\nLesson complete: literals make source code concise and explicit.")
