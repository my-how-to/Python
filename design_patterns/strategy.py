# ==============================================
# Pattern Name: Strategy
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   The Strategy pattern defines a family of interchangeable algorithms.
#   Instead of using if/elif chains, each cooking style becomes its own
#   class. The client can swap strategies at runtime.
#
# What Makes It Unique:
#   Strategy removes branching logic by encapsulating each behavior in a
#   separate class. Adding new cooking methods (e.g., steamed eggs)
#   requires *only* creating a new strategy class — no existing code
#   changes.
# ==============================================


# -----------------------------
# Strategy Interface
# -----------------------------
class CookingStrategy:
    def cook(self):
        raise NotImplementedError


# -----------------------------
# Concrete Strategies
# -----------------------------
class FryStrategy(CookingStrategy):
    def cook(self):
        print("Heating pan...")
        print("Frying egg...\n")


class BoilStrategy(CookingStrategy):
    def cook(self):
        print("Boiling water...")
        print("Cooking egg in boiling water...\n")


class ScrambleStrategy(CookingStrategy):
    def cook(self):
        print("Whisking egg...")
        print("Scrambling egg in pan...\n")


# -----------------------------
# Context
# -----------------------------
class EggCooker:
    # Holds a reference to a strategy.
    def __init__(self, strategy: CookingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CookingStrategy):
        print(f"Switching to: {strategy.__class__.__name__}")
        self.strategy = strategy

    def cook(self):
        self.strategy.cook()


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    print("--- Strategy Pattern Example (Cooking Eggs) ---\n")

    print("# -----------------------------")
    print("# USING STRATEGY PATTERN")
    print("# -----------------------------\n")

    cooker = EggCooker(FryStrategy())
    cooker.cook()

    cooker.set_strategy(BoilStrategy())
    cooker.cook()

    cooker.set_strategy(ScrambleStrategy())
    cooker.cook()


# -----------------------------
# Example Output
# -----------------------------
# --- Strategy Pattern Example (Cooking Eggs) ---
#
# -----------------------------
# USING STRATEGY PATTERN
# -----------------------------
# Heating pan...
# Frying egg...
#
# Switching to: BoilStrategy
# Boiling water...
# Cooking egg in boiling water...
#
# Switching to: ScrambleStrategy
# Whisking egg...
# Scrambling egg in pan...
#
# ==============================================
# History
# ==============================================
# The Strategy pattern was introduced to solve the problem of large
# conditional logic for choosing algorithms. By placing each algorithm
# inside its own class, developers can extend systems by adding new
# strategies without modifying existing code. This promotes flexibility
# and supports the Open–Closed Principle.
# ==============================================
