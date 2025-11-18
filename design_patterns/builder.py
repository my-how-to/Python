# ==============================================
# Pattern Name: Builder
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Builder pattern separates the construction steps of a complex object
#   (House) from its final representation. This allows the same construction
#   process to produce different types of houses.
#
# What Makes It Unique:
#   Builder focuses on *how* an object is created—step by step—rather than
#   *which* object is created. Factories instantiate objects in one call,
#   but Builder assembles them piece by piece in a controlled sequence.
# ==============================================


# -----------------------------
# Product: House
# -----------------------------
class House:
    def __init__(self):
        self.foundation = None
        self.walls = None
        self.roof = None
        self.windows = None
        self.has_garden = False
        self.has_pool = False
        self.floors = 1

    def show(self):
        print(f"Foundation: {self.foundation}")
        print(f"Walls: {self.walls}")
        print(f"Roof: {self.roof}")
        print(f"Windows: {self.windows}")
        print(f"Garden: {self.has_garden}")
        print(f"Pool: {self.has_pool}")
        print(f"Floors: {self.floors}")


# -----------------------------
# Abstract Builder
# -----------------------------
# NOTE:
#   When adding new house features (e.g., solar panels), we add a new method
#   here AND implement it only in concrete builders.
#   The Director and client code remain unchanged.
# -----------------------------
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        raise NotImplementedError

    def build_walls(self):
        raise NotImplementedError

    def build_roof(self):
        raise NotImplementedError

    def install_windows(self):
        raise NotImplementedError

    def add_garden(self):
        raise NotImplementedError

    def add_pool(self):
        raise NotImplementedError

    def set_floors(self):
        raise NotImplementedError

    def get_house(self):
        return self.house


# -----------------------------
# Concrete Builder: Wooden House
# -----------------------------
class WoodenHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "wood"

    def build_walls(self):
        self.house.walls = "wooden planks"

    def build_roof(self):
        self.house.roof = "shingles"

    def install_windows(self):
        self.house.windows = 4

    def add_garden(self):
        self.house.has_garden = False

    def add_pool(self):
        self.house.has_pool = False

    def set_floors(self):
        self.house.floors = 1


# -----------------------------
# Concrete Builder: Brick House
# -----------------------------
class BrickHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "concrete"

    def build_walls(self):
        self.house.walls = "brick"

    def build_roof(self):
        self.house.roof = "tile"

    def install_windows(self):
        self.house.windows = 6

    def add_garden(self):
        self.house.has_garden = True

    def add_pool(self):
        self.house.has_pool = False

    def set_floors(self):
        self.house.floors = 2


# -----------------------------
# Concrete Builder: Luxury Villa
# -----------------------------
class LuxuryVillaBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "reinforced concrete"

    def build_walls(self):
        self.house.walls = "glass + marble"

    def build_roof(self):
        self.house.roof = "flat modern roof"

    def install_windows(self):
        self.house.windows = 12

    def add_garden(self):
        self.house.has_garden = True

    def add_pool(self):
        self.house.has_pool = True

    def set_floors(self):
        self.house.floors = 2


# -----------------------------
# Director
# -----------------------------
# NOTE:
#   The Director controls the order of building steps.
#   This class NEVER changes, even when adding new house types
#   or new product features. Builders handle all variation.
# -----------------------------
class ConstructionDirector:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_foundation()
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.install_windows()
        self.builder.add_garden()
        self.builder.add_pool()
        self.builder.set_floors()
        return self.builder.get_house()


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Builder Pattern Example ---\n")

    director = ConstructionDirector(WoodenHouseBuilder())
    house1 = director.construct_house()
    print("Wooden House:")
    house1.show()

    print("\nBrick House:")
    director = ConstructionDirector(BrickHouseBuilder())
    house2 = director.construct_house()
    house2.show()

    print("\nLuxury Villa:")
    director = ConstructionDirector(LuxuryVillaBuilder())
    house3 = director.construct_house()
    house3.show()


# -----------------------------
# Example Output
# -----------------------------
# --- Builder Pattern Example ---
#
# Wooden House:
# Foundation: wood
# Walls: wooden planks
# Roof: shingles
# Windows: 4
# Garden: False
# Pool: False
# Floors: 1
#
# Brick House:
# Foundation: concrete
# Walls: brick
# Roof: tile
# Windows: 6
# Garden: True
# Pool: False
# Floors: 2
#
# Luxury Villa:
# Foundation: reinforced concrete
# Walls: glass + marble
# Roof: flat modern roof
# Windows: 12
# Garden: True
# Pool: True
# Floors: 2
#
#
# ==============================================
# History
# ==============================================
# The Builder pattern was included in the GoF book (1994) to solve the
# problem of creating complex objects with many optional parts. Instead of
# long constructors with many parameters, Builder organizes object creation
# into clear, reusable steps, allowing different final representations using
# the same construction process.
# ==============================================
