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
print("\n# -----------------------------")
print("# 3. SIMPLE EXAMPLE")
print("# -----------------------------\n")

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


print("\n# -----------------------------")
print("# 4. MULTIPLE OBJECTS")
print("# -----------------------------\n")

car1 = Car("BMW", "black")
car2 = Car("Toyota", "red")

car1.drive()
car2.drive()
# Each instance has its own independent data.


print("\n# -----------------------------")
print("# 5. ATTRIBUTES AND SELF")
print("# -----------------------------\n")

print("\nBrand:", my_car.brand)
print("Color:", my_car.color)
# `self` gives access to each object's attributes inside the class.

print("\n# -----------------------------")
print("# 6. CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE")
print("# -----------------------------\n")
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

# Class-level counters are another common use of class attributes.
class Person:
    population = 0  # shared counter

    def __init__(self, name):
        self.name = name
        Person.population += 1  # update shared counter whenever a new instance is created

    def say_hi(self):
        print(f"Hi, I'm {self.name} (#{Person.population} in population count)")


alice = Person("Alice")
bob = Person("Bob")
alex = Person("Alex")
alice.say_hi()
bob.say_hi()
alex.say_hi()

print("People created so far:", Person.population)

# Attributes can be deleted dynamically, but accessing afterwards raises AttributeError.
del alex.name
try:
    print(alex.name)
except AttributeError as err:
    print("Attribute deleted:", err)

print("\n# -----------------------------")
print("# 7. EXPLORING __dict__")
print("# -----------------------------\n")
#
# Every Python object stores its instance-specific data in the __dict__ attribute.
# Class attributes live in the class dictionary, so they do NOT appear in an instance __dict__
# until you assign them on that instance.

class DictDemo:
    shared_value = 10  # class attribute available to all instances

    def __init__(self, label):
        self.label = label  # stored inside the instance dictionary


demo = DictDemo("alpha")

print("Instance __dict__:", demo.__dict__)     # only label is present
print("Class shared_value via class:", DictDemo.shared_value)
print("shared_value in class __dict__:", DictDemo.__dict__["shared_value"])

# Assigning to the instance adds entries to its own dictionary.
demo.shared_value = 99
print("Instance __dict__ after overriding shared_value:", demo.__dict__)

# Removing the instance override reveals the class attribute again.
del demo.shared_value
print("Instance __dict__ after deleting override:", demo.__dict__)
print("Class shared_value still:", DictDemo.shared_value)


print("\n# -----------------------------")
print("# 8. CLASS WITH DEFAULT VALUES & ENCAPSULATION")
print("# -----------------------------\n")

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


print("\n# -----------------------------")
print("# 9. INHERITANCE & POLYMORPHISM")
print("# -----------------------------\n")

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
