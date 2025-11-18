# ==============================================
# Before Pattern: Factory Method
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how developers used to create objects directly before
#   the Factory Method pattern was introduced. This approach uses
#   direct class instantiation and many if/else statements scattered
#   throughout the code, making it hard to maintain and extend.
#
# Classifier:
#   - Category: Creational
#   - Purpose: Show how object creation was done before the pattern.
#   - Key idea: Each part of the program directly creates its own objects.
#   - Common issue: Tight coupling, duplication, and poor scalability.
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
# Old approach — direct object creation everywhere
# -----------------------------
def main():
    print("--- Before Factory Method Example ---")

    # Direct instantiation in multiple places of the program.
    choco = ChocolateCake()
    fruit = FruitCake()
    vanilla = VanillaCake()

    print(choco.bake())
    print(fruit.bake())
    print(vanilla.bake())

    # Imagine this same code duplicated across several modules:
    print("\n--- Another module needing cakes ---")
    cake_list = [
        ChocolateCake(),
        FruitCake(),
        VanillaCake(),
    ]
    for cake in cake_list:
        print(cake.bake())

    # Now suppose a new cake type (CheeseCake) is added.
    # Developers must update every section like this manually.
    print(
        "\nAdding a new cake type means finding and changing code everywhere —\n"
        "each module that creates cakes must be updated."
    )


if __name__ == "__main__":
    main()


# -----------------------------
# Example Output
# -----------------------------
#--- Before Factory Method Example ---
# A delicious chocolate cake!
# A sweet fruit cake!
# A soft vanilla cake!
#
#--- Another module needing cakes ---
# A delicious chocolate cake!
# A sweet fruit cake!
# A soft vanilla cake!
#
# Adding a new cake type means finding and changing code everywhere —
# each module that creates cakes must be updated.


# ==============================================
# History
# ==============================================
# Before the Factory Method pattern was formalized in 1994,
# developers commonly used direct object instantiation with many
# if/else conditions or duplicated code. This approach tightly
# coupled the program to specific classes, making maintenance difficult.
# The Factory Method pattern later solved this by centralizing and
# standardizing object creation logic.
# ==============================================