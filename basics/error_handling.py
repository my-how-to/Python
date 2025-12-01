# ============================================================
#            LESSON 8.1 - PYTHON EXCEPTION HANDLING
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains how Python handles errors (exceptions),
#   how to use try/except, else, finally, how to catch specific
#   errors, raise your own exceptions, and how to safely validate
#   user input inside loops.
#
# Contents:
#   1. What is an Exception?
#   2. Basic try/except
#   3. Catching specific errors
#   4. else and finally blocks
#   5. Raising your own exceptions
#   6. Validating input in loops
#   7. Common built-in exceptions
#   8. Real-world examples
#
# ============================================================


# ------------------------------------------------------------
# 1. WHAT IS AN EXCEPTION?
# ------------------------------------------------------------
# Exceptions are runtime errors that stop the program unless
# you handle them. Examples:
#    - dividing by zero
#    - converting letters to int
#    - opening missing files
#    - using undefined variables
#
# Python stops the program unless you catch the problem with
# try/except.


# ------------------------------------------------------------
# 2. BASIC try / except
# ------------------------------------------------------------

def example_basic_try():
    print("\n# --- BASIC try/except ---")
    try:
        number = int(input("Enter a number: "))
        print(10 / number)
    except:
        print("Something went wrong.")

# Example output (if user enters 'abc'):
# Something went wrong.


# ------------------------------------------------------------
# 3. CATCHING SPECIFIC EXCEPTIONS
# ------------------------------------------------------------

def example_specific_errors():
    print("\n# --- CATCHING SPECIFIC ERRORS ---")

    try:
        number = int(input("Enter a number: "))
        print(10 / number)
    except ValueError:
        print("Please enter numbers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# Example:
# Input: abc → Please enter numbers only.
# Input: 0   → Cannot divide by zero.


# ------------------------------------------------------------
# 4. ELSE and FINALLY BLOCKS
# ------------------------------------------------------------

def example_else_finally():
    print("\n# --- ELSE and FINALLY ---")

    try:
        file = open("notes.txt", "r")
    except FileNotFoundError:
        print("File not found.")
    else:
        print("File opened successfully.")
        file.close()
    finally:
        print("This always runs — cleaning up.")

# Example output:
# File not found.
# This always runs — cleaning up.


# ------------------------------------------------------------
# 5. RAISING YOUR OWN EXCEPTIONS
# ------------------------------------------------------------

def example_raising():
    print("\n# --- RAISING CUSTOM EXCEPTIONS ---")

    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print(f"Your age is {age}")

# Example:
# Input: -5 → ValueError: Age cannot be negative.


# ------------------------------------------------------------
# 6. VALIDATING INPUT INSIDE LOOPS
# ------------------------------------------------------------

def example_validation_loop():
    print("\n# --- INPUT VALIDATION WITH LOOP ---")

    while True:
        try:
            number = int(input("Enter a positive number: "))

            if number <= 0:
                raise ValueError("Number must be positive.")

        except ValueError as e:
            print("Error:", e)
        else:
            print(f"Good! You entered {number}")
            break

# Example:
# Enter a positive number: -5  → Error: Number must be positive.
# Enter a positive number: abc → Error: invalid literal for int()
# Enter a positive number: 10  → Good! You entered 10


# ------------------------------------------------------------
# 7. COMMON BUILT-IN EXCEPTIONS
# ------------------------------------------------------------
# Some exceptions you'll see often:
#
#   ValueError            wrong type conversion
#   ZeroDivisionError     dividing by zero
#   TypeError             wrong data types for an operation
#   FileNotFoundError     missing file
#   KeyError              missing dictionary key
#   IndexError            list index out of range
#   AttributeError        trying to use a missing attribute
#   NameError             using undefined variables
#   PermissionError       cannot access a file
#
# You don’t need to memorize them all — they become familiar
# as you code.

# ------------------------------------------------------------
# EXTRA: GETTING THE EXCEPTION NAME
# ------------------------------------------------------------
# Every Python exception object has a class. Using type(e).__name__
# allows you to print the exact exception name at runtime.
#
# Useful for debugging, logging, or generic except blocks.

try:
    5 / "2"
except Exception as e:
    print(type(e).__name__)  # TypeError

# ------------------------------------------------------------
# 8. REAL-WORLD EXAMPLES
# ------------------------------------------------------------

# 8.1 — Safe dictionary access
def example_safe_dict():
    print("\n# --- SAFE DICTIONARY ACCESS ---")

    user = {"name": "Alex"}

    try:
        print(user["email"])
    except KeyError:
        print("Email not found.")

# 8.2 — Safely reading a file
def example_safe_file():
    print("\n# --- SAFE FILE READING ---")

    try:
        with open("config.json", "r") as f:
            data = f.read()
            print("File loaded successfully!")
    except FileNotFoundError:
        print("Config file missing — using defaults.")

# 8.3 — Safe type conversion
def example_safe_conversion():
    print("\n# --- SAFE TYPE CONVERSION ---")

    values = ["10", "25", "abc", "100"]

    for val in values:
        try:
            num = int(val)
            print(num * 2)
        except ValueError:
            print(f"Skipping invalid value: {val}")


# ------------------------------------------------------------
# END OF FILE
# ------------------------------------------------------------
