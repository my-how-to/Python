# ==============================================
# Pattern Name: Abstract Factory
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Abstract Factory pattern creates families of related GUI widgets
#   (Button, Checkbox, Icon) without specifying concrete classes.
#   When adding new widget types, the client code and most of the system
#   remain unchanged — only product classes and concrete factories update.
#
# What Makes It Unique:
#   Abstract Factory ensures all created objects fit together as a coherent family.
#   It prevents accidental mixing of incompatible components 
#   by defining product sets in one factory.
# ==============================================


# -----------------------------
# Abstract Product Interfaces
# -----------------------------
# NOTE:
# When adding a new widget type (e.g., Slider),
# we add a new abstract interface here.
class Button:
    def draw(self):
        raise NotImplementedError


class Checkbox:
    def draw(self):
        raise NotImplementedError


class Icon:
    def draw(self):
        raise NotImplementedError


# -----------------------------
# Concrete Products (Dark Theme)
# -----------------------------
# NOTE:
# Only these classes change when adding a new widget type.
class DarkButton(Button):
    def draw(self):
        print("Drawing Dark Button")


class DarkCheckbox(Checkbox):
    def draw(self):
        print("Drawing Dark Checkbox")


class DarkIcon(Icon):
    def draw(self):
        print("Drawing Dark Icon")


# -----------------------------
# Concrete Products (Light Theme)
# -----------------------------
# NOTE:
# Same update here when adding a new widget type.
class LightButton(Button):
    def draw(self):
        print("Drawing Light Button")


class LightCheckbox(Checkbox):
    def draw(self):
        print("Drawing Light Checkbox")


class LightIcon(Icon):
    def draw(self):
        print("Drawing Light Icon")


# -----------------------------
# Abstract Factory Interface
# -----------------------------
# NOTE:
# When adding a new widget type, only add a new method here.
class GUIFactory:
    def create_button(self):
        raise NotImplementedError

    def create_checkbox(self):
        raise NotImplementedError

    def create_icon(self):
        raise NotImplementedError


# -----------------------------
# Concrete Factories
# -----------------------------
# NOTE:
# Only these classes change when new widgets are added.
class DarkThemeFactory(GUIFactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()

    def create_icon(self):
        return DarkIcon()


class LightThemeFactory(GUIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()

    def create_icon(self):
        return LightIcon()


# -----------------------------
# Example usage
# -----------------------------
def application(factory: GUIFactory):
    """
    NOTE:
    This client code NEVER changes when adding new widget types.
    It depends only on abstract interfaces.
    """
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    icon = factory.create_icon()

    button.draw()
    checkbox.draw()
    icon.draw()


if __name__ == "__main__":
    print("--- Abstract Factory Pattern Example ---\n")

    print("Using Dark Theme:")
    application(DarkThemeFactory())

    print("\nUsing Light Theme:")
    application(LightThemeFactory())


# -----------------------------
# Example Output
# -----------------------------
# --- Abstract Factory Pattern Example ---
#
# Using Dark Theme:
# Drawing Dark Button
# Drawing Dark Checkbox
# Drawing Dark Icon
#
# Using Light Theme:
# Drawing Light Button
# Drawing Light Checkbox
# Drawing Light Icon
#
# ==============================================
# History
# ==============================================
# The Abstract Factory pattern (GoF, 1994) solved the problem of keeping
# product families consistent. Applications can create entire widget sets
# from one theme (Dark, Light, etc.) without mixing styles.
#
# Adding a new widget type affects only:
# - the abstract interface (add method)
# - the concrete product classes
# - the concrete factories
#
# The client code and overall architecture stay unchanged.
# This is the core benefit of Abstract Factory.
# ==============================================
