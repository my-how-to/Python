# ==============================================
# BEFORE — Strategy Pattern
# Theme: Cooking Eggs Without Strategy
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Before the Strategy pattern, different cooking styles (fried, boiled,
#   scrambled) were implemented using long if/elif chains. Every time a
#   new cooking style was added, ALL existing cooking logic had to be
#   modified. This violates the Open–Closed Principle.
#
#   This file shows the old, rigid, branching-based approach.
# ==============================================


# -----------------------------
# BEFORE: Single function with if/elif logic
# -----------------------------
def cook_egg(style):
    print(f"Cooking egg using style: {style}\n")

    # Branching determines behavior
    if style == "fried":
        print("Heating pan...")
        print("Frying egg...")

    elif style == "boiled":
        print("Boiling water...")
        print("Cooking egg in boiling water...")

    elif style == "scrambled":
        print("Whisking egg...")
        print("Scrambling egg in pan...")

    else:
        print("Unknown style — cannot cook egg.")

    print()  # spacing


# -----------------------------
# Example Usage (Before Strategy)
# -----------------------------
if __name__ == "__main__":
    print("--- BEFORE Strategy Example (Cooking Eggs) ---\n")

    cook_egg("fried")
    cook_egg("boiled")
    cook_egg("scrambled")

    print("# -----------------------------")
    print("# DISADVANTAGE DEMO (Adding New Style Breaks Logic)")
    print("# -----------------------------\n")

    print("Attempting new style: 'steamed' (not implemented)\n")
    cook_egg("steamed")   # Unsupported


# -----------------------------
# Example Output
# -----------------------------
# --- BEFORE Strategy Example (Cooking Eggs) ---
#
# Cooking egg using style: fried
# Heating pan...
# Frying egg...
#
# Cooking egg using style: boiled
# Boiling water...
# Cooking egg in boiling water...
#
# Cooking egg using style: scrambled
# Whisking egg...
# Scrambling egg in pan...
#
# -----------------------------
# DISADVANTAGE DEMO (Adding New Style Breaks Logic)
# -----------------------------
# Attempting new style: 'steamed'
# Unknown style — cannot cook egg.
#
# ==============================================
# Why This Approach Fails (Before → After Comparison)
# ==============================================
# 1. Adding a new cooking method requires editing this function.
# 2. All branching logic is mixed together.
# 3. Violates the Open–Closed Principle.
# 4. Hard to test and maintain.
#
# The Strategy pattern fixes this by placing each cooking method into
# its own class and letting the client swap strategies at runtime.
# ==============================================

# ==============================================
# History
# ==============================================
# The Strategy pattern was formalized by the Gang of Four in 1994.
# It emerged to solve the problem of large conditional blocks used to
# select algorithms at runtime. By encapsulating each algorithm inside
# its own class, Strategy enabled flexible behavior changes without
# modifying existing code. This improved maintainability and supported
# the Open–Closed Principle.
# ==============================================
