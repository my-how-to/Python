# ==============================================
# Pattern Name: Factory Method (Basic Version)
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates the Factory Method pattern using simple if/else statements.
#   The Factory Method defines an interface for creating objects
#   but lets subclasses or factories decide which class to instantiate.
#
# Classifier:
#   - Category: Creational
#   - Purpose: Object creation without specifying the exact class name.
#   - Key idea: Delegate object creation to a factory.
#   - Common use: When code must create many types of objects dynamically.
#
# What Makes It Unique:
#   Factory centralizes object creation decisions.
#   Instead of scattering if/else logic across your codebase, 
#   it puts the choice of which subclass to instantiate in one place.
# ==============================================

# -----------------------------
# Base class (Cake)
# -----------------------------
class Cake:
    def bake(self):
        return "A plain cake."


# -----------------------------
# Subclasses (Different Cake Types)
# -----------------------------
class ChocolateCake(Cake):
    def bake(self):
        return "A delicious chocolate cake!"

class FruitCake(Cake):
    def bake(self):
        return "A sweet fruit cake!"

class VanillaCake(Cake):
    def bake(self):
        return "A soft vanilla cake!"


# -----------------------------
# Factory class (Basic with if/else)
# -----------------------------
class CakeFactory:
    """A simple factory that creates cakes using if/else statements."""

    def make_cake(self, cake_type):
        if cake_type == "chocolate":
            return ChocolateCake()
        elif cake_type == "fruit":
            return FruitCake()
        elif cake_type == "vanilla":
            return VanillaCake()
        else:
            return Cake()  # default fallback


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Factory Method: Basic Version ---")
    factory = CakeFactory()

    choco = factory.make_cake("chocolate")
    fruit = factory.make_cake("fruit")
    vanilla = factory.make_cake("vanilla")

    print(choco.bake())
    print(fruit.bake())
    print(vanilla.bake())

# -----------------------------
# Example Output
# -----------------------------
# A delicious chocolate cake!
# A sweet fruit cake!
# A soft vanilla cake!

# ==============================================
# History
# ==============================================
# The Factory Method pattern appeared in the 1994 book
# "Design Patterns: Elements of Reusable Object-Oriented Software"
# by the Gang of Four. 
# 
# It evolved from the need to simplify object
# creation in large systems where many classes existed.
# ==============================================
