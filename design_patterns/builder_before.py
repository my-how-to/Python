# ==============================================
# Before Pattern: Builder
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how a House object was constructed BEFORE the Builder pattern.
#   Complex objects with many optional parts required long constructors,
#   many parameters, and repeated logic. Adding new house types required
#   modifying large chunks of code, leading to errors and unreadable logic.
# ==============================================


# -----------------------------
# House class (complex object)
# -----------------------------
class House:
    def __init__(
        self,
        foundation,
        walls,
        roof,
        windows,
        has_garden=False,
        has_pool=False,
        floors=1,
    ):
        self.foundation = foundation
        self.walls = walls
        self.roof = roof
        self.windows = windows
        self.has_garden = has_garden
        self.has_pool = has_pool
        self.floors = floors

    def show(self):
        print(f"Foundation: {self.foundation}")
        print(f"Walls: {self.walls}")
        print(f"Roof: {self.roof}")
        print(f"Windows: {self.windows}")
        print(f"Garden: {self.has_garden}")
        print(f"Pool: {self.has_pool}")
        print(f"Floors: {self.floors}")


# -----------------------------
# House creation (Before Builder)
# -----------------------------
# NOTE:
# Without the Builder pattern, developers must manually pass ALL values every time.
# Optional features multiply constructor arguments and create confusion.
# Adding a new house feature (e.g., solar panels) requires editing constructor
# AND every place where houses are built.
# -----------------------------

def create_house(style):
    """
    Simulate messy house creation using manual if/else logic.
    Each style requires manually constructing all attributes.
    """

    if style == "wooden":
        return House(
            foundation="wood",
            walls="wooden planks",
            roof="shingles",
            windows=4,
            has_garden=False,
            has_pool=False,
            floors=1,
        )

    elif style == "brick":
        return House(
            foundation="concrete",
            walls="brick",
            roof="tile",
            windows=6,
            has_garden=True,
            has_pool=False,
            floors=2,
        )

    elif style == "luxury_villa":
        return House(
            foundation="reinforced concrete",
            walls="glass + marble",
            roof="flat modern roof",
            windows=12,
            has_garden=True,
            has_pool=True,
            floors=2,
        )

    else:
        raise ValueError("Unknown house style")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Builder Pattern Example ---\n")

    house = create_house("luxury_villa")
    house.show()

    print(
        "\nAdding a new feature (like solar panels) requires updating:\n"
        " - The House constructor\n"
        " - Every call to the constructor (like create_house)\n"
        " - All logic building houses manually\n"
        "This leads to duplicated logic and maintenance problems."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Before Builder Pattern Example ---
# Foundation: reinforced concrete
# Walls: glass + marble
# Roof: flat modern roof
# Windows: 12
# Garden: True
# Pool: True
# Floors: 2
#
# Adding a new feature (like solar panels) requires updating:
#  - The House constructor
#  - Every call to the constructor (like create_house)
#  - All logic building houses manually
# This leads to duplicated logic and maintenance problems.
#
#
# ==============================================
# History
# ==============================================
# Before the Builder pattern (popularized in the 1990s along with the GoF book),
# complex objects were created using long constructors with many optional
# parameters or nested if/else logic. This made code harder to maintain.
# The Builder pattern separates the construction process into steps, making
# object creation flexible, readable, and easier to extend.
# ==============================================
