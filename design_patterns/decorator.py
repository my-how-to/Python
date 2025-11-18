# ==============================================
# Pattern Name: Decorator
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Decorator pattern allows behavior to be added to individual objects,
#   dynamically and transparently, without affecting the behavior of other
#   objects from the same class. It wraps an object to extend or modify its
#   functionality at runtime.
#
# Classifier:
#   - Category: Structural
#   - Purpose: Dynamically add new behavior to an object.
#   - Key idea: Wrap an existing object with another that adds extra features.
#   - Common use: Extending functionality (e.g., logging, validation, styling).
#
# What Makes It Unique:
#   Decorator extends behavior without inheritance or modifying original classes.
#   It allows features to be layered dynamically at runtime.
# ==============================================

# -----------------------------
# Base class (Ice Cream)
# -----------------------------
class IceCream:
    def serve(self):
        return "Plain ice cream"


# -----------------------------
# Decorator base class
# -----------------------------
class IceCreamDecorator:
    """Wraps another ice cream object and extends its behavior."""

    def __init__(self, ice_cream):
        self.ice_cream = ice_cream

    def serve(self):
        return self.ice_cream.serve()


# -----------------------------
# Concrete decorators (add new flavors or toppings)
# -----------------------------
class ChocolateDecorator(IceCreamDecorator):
    def serve(self):
        return self.ice_cream.serve() + " + chocolate"


class SprinklesDecorator(IceCreamDecorator):
    def serve(self):
        return self.ice_cream.serve() + " + sprinkles"


class WhippedCreamDecorator(IceCreamDecorator):
    def serve(self):
        return self.ice_cream.serve() + " + whipped cream"


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Decorator Pattern Example ---")

    # Start with a simple ice cream
    dessert = IceCream()

    # Add toppings dynamically
    dessert = ChocolateDecorator(dessert)
    dessert = SprinklesDecorator(dessert)
    dessert = WhippedCreamDecorator(dessert)

    print(dessert.serve())


# -----------------------------
# Example Output
# -----------------------------
# --- Decorator Pattern Example ---
# Plain ice cream + chocolate + sprinkles + whipped cream


# ==============================================
# History
# ==============================================
# The Decorator pattern was formalized in the 1994
# "Design Patterns" book by the Gang of Four. However,
# the concept originated earlier in object composition
# practices in languages like Smalltalk. It provided
# an elegant alternative to subclassing for extending
# functionality — favoring composition over inheritance.
# ==============================================
