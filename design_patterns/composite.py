# ==============================================
# Pattern Name: Composite
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Composite pattern allows individual objects (Leaves) and groups
#   of objects (Composites) to be treated uniformly. In this example,
#   both single shapes and groups of shapes support the same .draw()
#   method, enabling recursive tree-like structures.
#
# What Makes It Unique:
#   Composite lets clients interact with single objects and whole
#   collections through the SAME interface. This removes the need
#   for type-checking and enables flexible nested structures.
# ==============================================


# -----------------------------
# Component Interface
# -----------------------------
# Defines the common interface for both simple shapes (Leaves)
# and composite groups that can contain other Graphics.
# -----------------------------
class Graphic:
    def draw(self):
        raise NotImplementedError


# -----------------------------
# Leaf Objects
# -----------------------------
# These are basic shapes that know how to draw themselves.
# -----------------------------
class Circle(Graphic):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")


class Square(Graphic):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def draw(self):
        print(f"Drawing Square at ({self.x}, {self.y}) with side {self.side}")


# -----------------------------
# Composite Object
# -----------------------------
# This object can contain multiple Graphics (both Leaves and Composites).
# Calling .draw() on the group draws everything it contains.
# -----------------------------
class GraphicGroup(Graphic):
    def __init__(self):
        self.items = []

    def add(self, graphic: Graphic):
        self.items.append(graphic)

    def draw(self):
        print("Drawing Group:")
        for item in self.items:
            item.draw()


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Composite Pattern Example ---\n")

    # Single shapes
    circle = Circle(10, 20, 5)
    square = Square(5, 5, 3)

    # A group containing both shapes
    group = GraphicGroup()
    group.add(circle)
    group.add(square)

    # Nested group (groups inside groups)
    nested = GraphicGroup()
    nested.add(Circle(1, 1, 2))
    nested.add(group)

    # Drawing the nested structure
    nested.draw()


# -----------------------------
# Example Output
# -----------------------------
# --- Composite Pattern Example ---
# Drawing Group:
# Drawing Circle at (1, 1) with radius 2
# Drawing Group:
# Drawing Circle at (10, 20) with radius 5
# Drawing Square at (5, 5) with side 3
#
#
# ==============================================
# History
# ==============================================
# The Composite pattern (GoF 1994) was created to manage hierarchical
# structures like file systems, UI components, and graphics scenes.
# It unifies simple objects and complex containers under a single
# interface so they can be used interchangeably without special logic.
# ==============================================
