# ============================================================
#            LESSON — VARIABLES & DATA TYPES
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson introduces variables and data types in Python:  
#   what variables are, naming rules, dynamic typing, main data
#   types (int, float, str, bool, list, tuple, set, dict), type
#   checking with type(), type conversions, and practical examples.
#
# Contents:
#   1. What is a variable?
#   2. Valid / invalid variable names
#   3. Dynamic typing
#   4. Primitive data types
#   5. Type checking
#   6. Converting between types
#   7. Practical mini-examples
#
# ============================================================


print("\n# -----------------------------")
print("# 1. WHAT IS A VARIABLE?")
print("# -----------------------------\n")

# A variable is a name that stores a value in memory.
x = 10
message = "Hello"
is_active = True

print("x =", x)
print("message =", message)
print("is_active =", is_active)

# Example Output:
# x = 10
# message = Hello
# is_active = True


print("\n# -----------------------------")
print("# 2. VARIABLE NAMING RULES")
print("# -----------------------------\n")

# Valid names:
user_age = 25
total_sum = 100
_name = "Alex"
HEIGHT = 180  # constants usually CAPITALIZED
_ = "Underscore variable"   # valid but not recommended
HEIGHT = 180                # constants usually CAPITALIZED
Import = "Reserved words can be used but not recommended" #started with capital letter

# Invalid names (uncomment to see SyntaxError):
# 2user = 5
# user-age = 30
# my variable = 10

print("Valid examples:", user_age, total_sum, _name, HEIGHT)


print("\n# -----------------------------")
print("# 3. PYTHON IS DYNAMICALLY TYPED")
print("# -----------------------------\n")

var = 10       # int
print("var =", var, "type:", type(var))

var = "text"   # str
print("var =", var, "type:", type(var))

var = 3.14     # float
print("var =", var, "type:", type(var))

# Example Output:
# var = 10 type: <class 'int'>
# var = text type: <class 'str'>
# var = 3.14 type: <class 'float'>


print("\n# -----------------------------")
print("# 4. MAIN DATA TYPES")
print("# -----------------------------\n")

integer_example = 42                 # int
float_example = 3.14                 # float
string_example = "Python"            # str
boolean_example = False              # bool
list_example = [1, 2, 3]             # list (mutable)
tuple_example = (1, 2, 3)            # tuple (immutable)
set_example = {1, 2, 3}              # set (unique items)
dict_example = {"name": "Alex"}      # dict (key-value pairs)

print(integer_example, type(integer_example))
print(float_example, type(float_example))
print(string_example, type(string_example))
print(boolean_example, type(boolean_example))
print(list_example, type(list_example))
print(tuple_example, type(tuple_example))
print(set_example, type(set_example))
print(dict_example, type(dict_example))


print("\n# -----------------------------")
print("# 5. CHECKING TYPES WITH type()")
print("# -----------------------------\n")

value = 123
print("Type of value:", type(value))
print("Type name:", type(value).__name__)

# Example Output:
# Type of value: <class 'int'>
# Type name: int


print("\n# -----------------------------")
print("# 6. TYPE CASTING (CONVERSIONS)")
print("\n# -----------------------------")

# print(int("3.5")) 
# int() cannot convert a decimal string. Must use float("3.5") first.
# Correct way:
print(int(float("3.5")))  # Output: 3

num_str = "100"
num_int = int(num_str)
num_float = float(num_str)

print(num_str, type(num_str))
print(num_int, type(num_int))
print(num_float, type(num_float))

# Possible conversions:
# int()  float()  str()  bool()

# ================================
# Printing Variables That Are Not Defined - NameError
# ================================

# If you try to use or print a variable before it exists,
# Python raises a NameError.

# Example — undefined variable
# print(x) # xr is not defined

# Error:
# NameError: name 'xr' is not defined

# Example — variable defined INSIDE a function cannot be used outside
# def test():
#    y = 10 # local variable
# print(y) # y is not defined here
# Error:
# NameError: name 'y' is not defined

# Key rule:
# A variable must exist *in the current scope* before you can print or use it.

print("\n# -----------------------------")
print("# 7. PRACTICAL MINI-EXAMPLES")
print("# -----------------------------\n")

print("# Example 1 — Adding numbers")
a = 5
b = 7
print("Result:", a + b)

print("\n# Example 2 — String concatenation")
first = "Alex"
last = "Frost"
print("Full name:", first + " " + last)

print("\n# Example 3 — Boolean expressions")
age = 18
print("Is adult?", age >= 18)

# Example Outputs:
# Result: 12
# Full name: Alex Frost
# Is adult? True

