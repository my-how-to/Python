# ==============================================
# Pattern Name: Factory Method (Registry Version)
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates the Factory Method pattern using a registry approach.
#   Each class registers itself, allowing the factory to create instances
#   dynamically without hardcoded if/else statements.
#
# Classifier:
#   - Category: Creational
#   - Purpose: Object creation without specifying the exact class name.
#   - Key idea: Classes register themselves, making code scalable.
#   - Common use: Plugin systems, dynamic type creation, modular architectures.
# ==============================================

# -----------------------------
# Base class (Cake)
# -----------------------------
class Cake:
    def bake(self):
        return "A plain cake."


# -----------------------------
# Factory class (Registry-based)
# -----------------------------
class CakeRegistryFactory:
    """A scalable factory where each class registers itself."""

    registry = {}  # stores all available cake types

    @classmethod
    def register_cake(cls, name, cake_class):
        cls.registry[name] = cake_class

    @classmethod
    def make_cake(cls, name):
        cake_class = cls.registry.get(name)
        if not cake_class:
            raise ValueError(f"Unknown cake type: {name}")
        return cake_class()


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

class CheeseCake(Cake):
    def bake(self):
        return "A smooth and creamy cheesecake!"


# -----------------------------
# Registration of classes
# -----------------------------
CakeRegistryFactory.register_cake("chocolate", ChocolateCake)
CakeRegistryFactory.register_cake("fruit", FruitCake)
CakeRegistryFactory.register_cake("vanilla", VanillaCake)
CakeRegistryFactory.register_cake("cheese", CheeseCake)


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Factory Method: Registry Version ---")

    cake1 = CakeRegistryFactory.make_cake("cheese")
    cake2 = CakeRegistryFactory.make_cake("chocolate")
    cake3 = CakeRegistryFactory.make_cake("fruit")

    print(cake1.bake())
    print(cake2.bake())
    print(cake3.bake())


# -----------------------------
# Example Output
# -----------------------------
# A smooth and creamy cheesecake!
# A delicious chocolate cake!
# A sweet fruit cake!


# ==============================================
# History
# ==============================================
# The Factory Method pattern was formalized in 1994 by the "Gang of Four".
# The registry-based approach evolved later as developers sought more flexible
# designs. 
# 
# It removes the need for repetitive if/else checks and allows new
# classes to integrate automatically — perfect for plugin-like systems.
# ==============================================
