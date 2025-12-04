# ==============================================
# BEFORE — Template Method Pattern
# Theme: Growing Plants (Tomato / Sunflower / Onion)
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Before the Template Method pattern, complex multi-step processes
#   were implemented using long if/elif chains. Every new variation
#   required rewriting or modifying many steps.
#
#   In this BEFORE example, growing different plants (tomato, sunflower,
#   onion) is handled manually inside a single function containing
#   repetitive logic. This creates duplication and violates the
#   Open–Closed Principle.
# ==============================================


# -----------------------------
# BEFORE: Manual multi-step process with if/elif
# -----------------------------
def grow_plant(plant_type):
    print(f"Growing: {plant_type.upper()}\n")

    # Step 1: Prepare soil (same for all)
    print("Preparing soil...")

    # Step 2: Plant seed (varies)
    if plant_type == "tomato":
        print("Planting tomato seeds shallowly...")
    elif plant_type == "sunflower":
        print("Planting sunflower seeds with spacing...")
    elif plant_type == "onion":
        print("Planting onion bulbs deeper into the soil...")
    else:
        print("Unknown plant type — cannot continue.")
        return

    # Step 3: Water (varies)
    if plant_type == "tomato":
        print("Watering regularly (tomatoes need steady moisture)...")
    elif plant_type == "sunflower":
        print("Watering moderately...")
    elif plant_type == "onion":
        print("Watering lightly (onions need less water)...")

    # Step 4: Care (varies)
    if plant_type == "tomato":
        print("Adding support sticks for tomato plants...")
    elif plant_type == "sunflower":
        print("Ensuring lots of sunlight for sunflowers...")
    elif plant_type == "onion":
        print("Removing weeds to help onions grow...")

    # Step 5: Harvest (same for all)
    print("Harvesting when ready!\n")


# -----------------------------
# Example Usage (Before Template Method)
# -----------------------------
if __name__ == "__main__":
    print("--- BEFORE Template Method Example (Growing Plants) ---\n")

    grow_plant("tomato")
    grow_plant("sunflower")
    grow_plant("onion")

    print("# -----------------------------")
    print("# DISADVANTAGE DEMO (Adding New Plant Breaks Logic)")
    print("# -----------------------------\n")

    print("Attempting to grow a new plant type: 'cucumber'\n")
    grow_plant("cucumber")   # Fails — not supported


# -----------------------------
# Example Output
# -----------------------------
# --- BEFORE Template Method Example (Growing Plants) ---
#
# Growing: TOMATO
# Preparing soil...
# Planting tomato seeds shallowly...
# Watering regularly (tomatoes need steady moisture)...
# Adding support sticks for tomato plants...
# Harvesting when ready!
#
# Growing: SUNFLOWER
# Preparing soil...
# Planting sunflower seeds with spacing...
# Watering moderately...
# Ensuring lots of sunlight for sunflowers...
# Harvesting when ready!
#
# Growing: ONION
# Preparing soil...
# Planting onion bulbs deeper into the soil...
# Watering lightly (onions need less water)...
# Removing weeds to help onions grow...
# Harvesting when ready!
#
# -----------------------------
# DISADVANTAGE DEMO (Adding New Plant Breaks Logic)
# -----------------------------
# Attempting to grow a new plant type: 'cucumber'
# Unknown plant type — cannot continue.
#
#
# ==============================================
# History
# ==============================================
# Before the Template Method pattern, multi-step processes were often
# implemented with conditional logic. When new variations needed to be
# added, developers had to change many if/elif sections. This created
# rigid and error-prone code.
#
# Template Method was introduced to define the *overall algorithm* in
# a superclass, while letting subclasses override only the specific
# steps that change. This dramatically improved flexibility and enabled
# the Open–Closed Principle.
# ==============================================
