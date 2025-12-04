# ============================================================
#            LESSON 9.2 - ERROR HANDLING — OOP VERSION
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This file demonstrates how to use exceptions inside classes,
#   how to define custom exceptions, enforce object rules, and
#   validate data safely in OOP-style Python programs.
#
# Contents:
#   1. Custom exception classes
#   2. Using exceptions inside methods
#   3. Constructor validation (__init__)
#   4. Real-world BankAccount example
#   5. Best practices for OOP error handling
#
# ============================================================


# ------------------------------------------------------------
# 1. CUSTOM EXCEPTION CLASSES
# ------------------------------------------------------------
# Creating your own exception helps you describe errors better.

class NegativeAmountError(Exception):
    """Raised when a negative amount is used."""
    pass

class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds account balance."""
    pass


# ------------------------------------------------------------
# 2. USING EXCEPTIONS INSIDE METHODS
# ------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Deposit must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Withdrawal must be positive.")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Not enough funds: tried {amount}, available {self.balance}"
            )

        self.balance -= amount
        return self.balance


# ------------------------------------------------------------
# 3. USING EXCEPTIONS IN __init__ CONSTRUCTOR
# ------------------------------------------------------------

class User:
    def __init__(self, username, age):
        if not username:
            raise ValueError("Username cannot be empty.")

        if age < 0:
            raise ValueError("Age cannot be negative.")

        self.username = username
        self.age = age


# ------------------------------------------------------------
# 4. REAL-WORLD USAGE EXAMPLES
# ------------------------------------------------------------

def example_bank_account_flow():
    print("\n# --- BANK ACCOUNT EXAMPLE ---")

    alex = BankAccount("Alex", 100)

    try:
        alex.deposit(50)
        alex.withdraw(200)
    except InsufficientFundsError as e:
        print("Error:", e)

    try:
        alex.withdraw(-10)
    except NegativeAmountError as e:
        print("Error:", e)


def example_user_creation():
    print("\n# --- USER CREATION EXAMPLE ---")

    try:
        user = User("", 25)
    except ValueError as e:
        print("Error:", e)

    try:
        user = User("Alex", -5)
    except ValueError as e:
        print("Error:", e)


# ------------------------------------------------------------
# 5. OOP ERROR HANDLING BEST PRACTICES
# ------------------------------------------------------------
# ✔ Raise exceptions inside a class when invalid data is given
# ✔ Keep error messages clear and specific
# ✔ Never silently ignore harmful input
# ✔ Use custom exceptions when logic is domain-specific
# ✔ Fail early (validate as soon as possible)
# ✔ Use try/except in the calling code, not inside the class
#
# This makes your classes clean, predictable, and testable.


# ------------------------------------------------------------
# END OF FILE
# ------------------------------------------------------------
