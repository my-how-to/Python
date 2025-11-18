# ==============================================
# Before Pattern: Adapter
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how systems operated before the Adapter pattern was used.
#   In this example, two classes use incompatible methods — one provides power
#   using a European standard, and another expects a USA standard. Before the
#   Adapter pattern, developers had to manually rewrite or duplicate code to
#   make them compatible, leading to tight coupling and reduced flexibility.
#
# Classifier:
#   - Category: Structural
#   - Purpose: Show how systems interacted without adapters.
#   - Key idea: Each incompatible system required manual conversion or code duplication.
#   - Common issue: Code was hard to maintain and extend when standards changed.
# ==============================================

# -----------------------------
# European-style charger
# -----------------------------
class EuropeanCharger:
    def provide_power_eu(self):
        return "Power from European outlet (220V)"


# -----------------------------
# USA-style socket
# -----------------------------
class USASocket:
    def supply_power_usa(self):
        return "Power from USA outlet (110V)"


# -----------------------------
# Old approach — incompatible systems
# -----------------------------
def main():
    print("--- Before Adapter Example ---")

    eu_charger = EuropeanCharger()
    usa_socket = USASocket()

    # These two systems are incompatible.
    print(eu_charger.provide_power_eu())
    print(usa_socket.supply_power_usa())

    # Developers used to handle this incompatibility manually.
    # For example, they might rewrite or patch conversion code
    # each time they needed to use the European charger in the USA.
    print("\nManual workaround:")
    eu_power = eu_charger.provide_power_eu()
    usa_ready_power = eu_power.replace("(220V)", "(110V)") + " [manually converted]"
    print(usa_ready_power)


if __name__ == "__main__":
    main()


# -----------------------------
# Example Output
# -----------------------------
# --- Before Adapter Example ---
# Power from European outlet (220V)
# Power from USA outlet (110V)
#
# Manual workaround:
# Power from European outlet (110V) [manually converted]


# ==============================================
# History
# ==============================================
# Before the Adapter pattern was described in the 1994
# "Design Patterns" book by the Gang of Four, developers
# often duplicated code or manually modified incompatible
# classes to make them work together. This created maintenance
# issues and reduced flexibility. The Adapter pattern later
# standardized this solution by introducing a single translator
# class to bridge mismatched interfaces.
# ==============================================