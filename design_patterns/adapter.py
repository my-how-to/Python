# ==============================================
# Pattern Name: Adapter
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Adapter pattern allows incompatible classes to work together
#   by converting the interface of one class into another that
#   clients expect. It acts like a translator between two systems
#   that speak different “languages”.
#
# Classifier:
#   - Category: Structural
#   - Purpose: Bridge between incompatible interfaces.
#   - Key idea: Wrap an existing class with a new interface.
#   - Common use: Integrating old code or external APIs into new systems.
#
# What Makes It Unique:
#   Adapter works without changing existing classes.
#   It connects incompatible interfaces externally, acting as a plug-in compatibility layer.
# ==============================================

# -----------------------------
# Old class (European charger)
# -----------------------------
class EuropeanCharger:
    def provide_power_eu(self):
        """Simulates providing power from a European outlet (220V)."""
        return "Power from European outlet (220V)"


# -----------------------------
# New class (USA socket)
# -----------------------------
class USASocket:
    def supply_power_usa(self):
        """Simulates providing power from a USA outlet (110V)."""
        return "Power from USA outlet (110V)"


# -----------------------------
# Adapter class
# -----------------------------
class PowerAdapter:
    """Adapter that allows a EuropeanCharger to be used with a USASocket."""

    def __init__(self, charger: EuropeanCharger):
        # Keep a reference to the object we're adapting
        self.charger = charger

    def supply_power_usa(self):
        """Translate the EU-style power output to USA standard."""
        return f"{self.charger.provide_power_eu()} adapted to USA standard!"


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    # Create the original (incompatible) object
    eu_charger = EuropeanCharger()

    # Wrap it with an adapter
    adapter = PowerAdapter(eu_charger)

    # Now it can work with the USA socket system
    print(adapter.supply_power_usa())

# -----------------------------
# Example Output
# -----------------------------
# Power from European outlet (220V) adapted to USA standard!


# ==============================================
# History
# ==============================================
# The Adapter pattern was first described in the
# 1994 book “Design Patterns: Elements of Reusable
# Object-Oriented Software” by the Gang of Four.
# 
# It was inspired by the real-world idea of electrical
# adapters — connecting incompatible systems without
# modifying them.
# ==============================================
