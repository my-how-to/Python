# ==============================================
# Before Pattern: Composite
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how shapes and shape groups were handled BEFORE
#   applying the Composite pattern. The client code must manually check
#   whether an item is a single shape or a group of shapes, leading to
#   complex type-checking logic and duplication.
# ==============================================


# -----------------------------
# Simple Shape Classes (No Common Interface)
# -----------------------------
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw_circle(self):
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")


class Square:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def draw_square(self):
        print(f"Drawing Square at ({self.x}, {self.y}) with side {self.side}")


# -----------------------------
# Group of Shapes (Stored as Raw Objects)
# -----------------------------
class ShapeGroup:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)


# -----------------------------
# Drawing Logic (Before Composite)
# -----------------------------
# NOTE:
#   The client must manually check the type of each item.
#   There is no common .draw() method.
#   Adding new shapes requires updating all type checks.
# -----------------------------

def draw_item(item):
    if isinstance(item, Circle):
        item.draw_circle()
    elif isinstance(item, Square):
        item.draw_square()
    elif isinstance(item, ShapeGroup):
        print("Drawing Group:")
        for sub_item in item.items:
            draw_item(sub_item)
    else:
        raise ValueError("Unknown item type")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Composite Pattern Example ---\n")

    circle = Circle(10, 20, 5)
    square = Square(5, 5, 3)

    group = ShapeGroup()
    group.add(circle)
    group.add(square)

    draw_item(group)

    print(
        "\nAdding a new shape (e.g., Triangle) requires:\n"
        " - A new class Triangle\n"
        " - Updating draw_item() with new type checks\n"
        " - Updating every nested group that may contain it\n"
        "This violates the Open–Closed Principle."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Before Composite Pattern Example ---
# Drawing Group:
# Drawing Circle at (10, 20) with radius 5
# Drawing Square at (5, 5) with side 3
#
# Adding a new shape requires updating type checks everywhere.
# This does not scale.
#
#
# ==============================================
# History
# ==============================================
# Before the Composite pattern (GoF 1994), tree-like structures were built
# manually and required repetitive type-checking logic. Composite unifies
# simple and complex objects under one interface so they can be treated
# uniformly.
# ==============================================
