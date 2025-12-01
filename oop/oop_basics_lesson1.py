# ===========================================
#  OOP BASICS — LESSON 1: INTRODUCTION
# ===========================================
#
# What is OOP?
# ------------
# Object-Oriented Programming (OOP) is a way of structuring code
# around *objects* — bundles of related data (attributes) and
# behaviors (methods).
#
# Instead of writing many separate functions that pass data around,
# you model real-world things (like a Car, User, or BankAccount)
# as *objects* that manage their own data and actions.
#
# Main Benefits:
#   - Organizes related code into units (classes)
#   - Makes programs reusable and maintainable
#   - Encourages modular and scalable design
#
# ===========================================
# 1 KEY CONCEPTS
# ===========================================
#
# Class          — a blueprint for creating objects.
# Object         — a specific instance created from a class.
# Attribute      — variable stored inside an object.
# Method         — function defined inside a class.
# __init__       — special method that initializes new objects.
# Encapsulation  — keeping data + methods together.
# Inheritance    — reuse behavior from another class.
# Polymorphism   — same method name acting differently.
#
# ===========================================
# 2 PYTHON BEHAVIOR IF __init__ IS OMITTED
# ===========================================
#
# If a class has NO __init__ method:
#   - Python automatically creates a DEFAULT constructor.
#   - That constructor takes ONLY `self` and does NOTHING.
#
# Example:
#
#   class A:
#       pass
#
# This is equivalent to:
#
#   class A:
#       def __init__(self):
#           pass
#
# IMPORTANT:
# - If you need attributes (brand, color, etc.), you MUST define __init__ yourself.
# - If __init__ is omitted BUT the parent class has __init__, Python uses the parent's version.
# - If __init__ is omitted AND the parent requires parameters → calling the class will raise TypeError.
#
# ===========================================
# 3 SIMPLE EXAMPLE
# ===========================================

class Car:
    """A simple Car class demonstrating attributes and methods."""

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")


# Create an object (instance)
my_car = Car("Opel Astra", "silver")
my_car.drive()     # Output: The silver Opel Astra is driving.


# ===========================================
# 4 MULTIPLE OBJECTS
# ===========================================

car1 = Car("BMW", "black")
car2 = Car("Toyota", "red")

car1.drive()
car2.drive()
# Each instance has its own independent data.


# ===========================================
# 5 ATTRIBUTES AND SELF
# ===========================================

print("\nBrand:", my_car.brand)
print("Color:", my_car.color)
# `self` gives access to each object's attributes inside the class.

# ===========================================
# 6. CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
# ===========================================
#
# Class attribute:
#   - defined at class level
#   - shared by ALL instances
#
# Instance attribute:
#   - defined inside __init__
#   - unique to each object
#
# Example:

class A:
    x = 5  # class attribute

a = A()
a.x = 10  # creates an INSTANCE attribute with the same name

print(A.x)  # 5  (class attribute unchanged)
print(a.x)  # 10 (instance attribute shadows class attribute)

# Key rule:
# Changing an attribute through an instance does NOT modify the class attribute.

# ===========================================
# 7 CLASS WITH DEFAULT VALUES & ENCAPSULATION
# ===========================================

class BankAccount:
    """Demonstrates attributes, default values, and encapsulation."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance  # instance attribute

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")


alex = BankAccount("Alex", 100)
alex.deposit(50)
alex.withdraw(30)


# ===========================================
# 8 INHERITANCE & POLYMORPHISM
# ===========================================

class ElectricCar(Car):
    """Child class inheriting from Car."""

    def __init__(self, brand, color, battery_size=75):
        super().__init__(brand, color)  # call parent constructor
        self.battery_size = battery_size

    def charge(self):
        print(f"{self.brand} battery ({self.battery_size} kWh) is charging...")

    # Overriding (polymorphism)
    def drive(self):
        print(f"The {self.color} {self.brand} drives silently ⚡")


tesla = ElectricCar("Tesla", "white")
tesla.drive()   # overridden method
tesla.charge()


# ===========================================
# 9 SUMMARY NOTES
# ===========================================
#
# Key Points:
# -----------
# * `self` refers to the current object instance.
# * `__init__` runs automatically to set up new objects.
# * If `__init__` is missing, Python uses a default empty constructor.
# * You can create many independent objects from one class blueprint.
# * Inheritance extends or customizes class behavior.
# * Polymorphism lets child classes override parent methods.
#
# Practical Uses:
# ---------------
# - Modeling entities (Cars, Users, Accounts)
# - Building modular systems (engines, dashboards, analyzers)
# - Reusing logic across classes via inheritance or composition
