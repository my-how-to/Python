# ==============================================
# Before Pattern: Decorator
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how developers extended functionality before the Decorator pattern.
#   In this approach, every new combination of features required creating a new
#   subclass or adding complex conditional logic. This quickly led to code
#   duplication and made the system harder to maintain.
#
# Classifier:
#   - Category: Structural
#   - Purpose: Show how behavior was extended before using decorators.
#   - Key idea: Use subclassing or manual conditional code to add new functionality.
#   - Common issue: Many subclasses, duplicated code, or long conditional chains.
# ==============================================

# -----------------------------
# Base class (Ice Cream)
# -----------------------------
class IceCream:
    def serve(self):
        return "Plain ice cream"


# -----------------------------
# Old approach — using subclasses for every combination
# -----------------------------
class ChocolateIceCream(IceCream):
    def serve(self):
        return "Plain ice cream + chocolate"


class ChocolateSprinkleIceCream(IceCream):
    def serve(self):
        return "Plain ice cream + chocolate + sprinkles"


class FullOptionIceCream(IceCream):
    def serve(self):
        return "Plain ice cream + chocolate + sprinkles + whipped cream"


# -----------------------------
# Alternate old approach — using conditionals (hard to scale)
# -----------------------------
def make_ice_cream(has_chocolate=False, has_sprinkles=False, has_whipped_cream=False):
    base = "Plain ice cream"
    if has_chocolate:
        base += " + chocolate"
    if has_sprinkles:
        base += " + sprinkles"
    if has_whipped_cream:
        base += " + whipped cream"
    return base


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Decorator Example ---")

    # Using subclasses
    simple = IceCream()
    choco = ChocolateIceCream()
    fancy = FullOptionIceCream()

    print(simple.serve())
    print(choco.serve())
    print(fancy.serve())

    # Using conditionals
    print("\n--- Conditional version ---")
    print(make_ice_cream(True, False, False))
    print(make_ice_cream(True, True, True))

    print("\nAdding a new topping would require creating more subclasses,")
    print("or adding another condition everywhere this code appears.")


# -----------------------------
# Example Output
# -----------------------------
# --- Before Decorator Example ---
# Plain ice cream
# Plain ice cream + chocolate
# Plain ice cream + chocolate + sprinkles + whipped cream
#
# --- Conditional version ---
# Plain ice cream + chocolate
# Plain ice cream + chocolate + sprinkles + whipped cream
#
# Adding a new topping would require creating more subclasses,
# or adding another condition everywhere this code appears.


# ==============================================
# History
# ==============================================
# Before the Decorator pattern was described in 1994 by the Gang of Four,
# developers often relied on subclassing or nested conditional statements
# to add new behaviors to objects. This led to rigid, repetitive code that
# was difficult to maintain. The Decorator pattern solved this problem by
# allowing flexible composition — adding behavior dynamically at runtime.
# ==============================================
