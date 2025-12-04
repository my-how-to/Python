# ==============================================
# Pattern Name: Template Method
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   The Template Method pattern defines the *skeleton* of an algorithm
#   in a base class and lets subclasses override the specific steps
#   without changing the overall workflow.
#
#   In this example, the process of growing plants has five steps:
#       1. prepare_soil()     (same for all plants)
#       2. plant_seed()       (differs per plant)
#       3. water()            (differs per plant)
#       4. care()             (differs per plant)
#       5. harvest()          (same for all plants)
#
# What Makes It Unique:
#   Template Method allows consistent multi-step workflows while letting
#   subclasses customize only the parts that vary. Adding a new plant type
#   requires creating a new subclass — the main algorithm stays unchanged.
# ==============================================


# -----------------------------
# Template Class (Base Algorithm)
# -----------------------------
class PlantGrowthTemplate:
    # The "template method" defining the full algorithm
    def grow(self):
        self.prepare_soil()
        self.plant_seed()
        self.water()
        self.care()
        self.harvest()

    # --- Steps (subclasses may override these) ---

    def prepare_soil(self):
        print("Preparing soil...")

    def plant_seed(self):
        raise NotImplementedError("Subclasses must implement plant_seed()")

    def water(self):
        raise NotImplementedError("Subclasses must implement water()")

    def care(self):
        raise NotImplementedError("Subclasses must implement care()")

    def harvest(self):
        print("Harvesting when ready!\n")


# -----------------------------
# Concrete Implementations (Tomato / Sunflower / Onion)
# -----------------------------
class TomatoPlant(PlantGrowthTemplate):
    def plant_seed(self):
        print("Planting tomato seeds shallowly...")

    def water(self):
        print("Watering regularly (tomatoes need steady moisture)...")

    def care(self):
        print("Adding support sticks for tomato plants...")


class SunflowerPlant(PlantGrowthTemplate):
    def plant_seed(self):
        print("Planting sunflower seeds with spacing...")

    def water(self):
        print("Watering moderately...")

    def care(self):
        print("Ensuring lots of sunlight for sunflowers...")


class OnionPlant(PlantGrowthTemplate):
    def plant_seed(self):
        print("Planting onion bulbs deeper into the soil...")

    def water(self):
        print("Watering lightly (onions need less water)...")

    def care(self):
        print("Removing weeds to help onions grow...")


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    print("--- Template Method Example (Growing Plants) ---\n")

    print("# -----------------------------")
    print("# USING TEMPLATE METHOD")
    print("# -----------------------------\n")

    tomato = TomatoPlant()
    sunflower = SunflowerPlant()
    onion = OnionPlant()

    tomato.grow()
    sunflower.grow()
    onion.grow()


# -----------------------------
# Example Output
# -----------------------------
# --- Template Method Example (Growing Plants) ---
#
# -----------------------------
# USING TEMPLATE METHOD
# -----------------------------
# Preparing soil...
# Planting tomato seeds shallowly...
# Watering regularly (tomatoes need steady moisture)...
# Adding support sticks for tomato plants...
# Harvesting when ready!
#
# Preparing soil...
# Planting sunflower seeds with spacing...
# Watering moderately...
# Ensuring lots of sunlight for sunflowers...
# Harvesting when ready!
#
# Preparing soil...
# Planting onion bulbs deeper into the soil...
# Watering lightly (onions need less water)...
# Removing weeds to help onions grow...
# Harvesting when ready!
#
#
# ==============================================
# History
# ==============================================
# The Template Method pattern was formalized in the 1994
# "Design Patterns" book by the Gang of Four. It emerged from
# the need to manage common algorithm structures shared among
# different classes while allowing subclasses to define the
# specific steps. This allowed large systems to maintain
# stability while supporting variation.
# ==============================================
