# ==============================================
# Pattern Name: Mediator
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Mediator pattern defines an object that encapsulates how a set of
#   objects interact. Instead of objects calling each other directly, they
#   communicate through a Mediator, reducing coupling and simplifying
#   collaboration. This example uses a **traffic intersection** analogy where
#   cars do not negotiate with each other directly — instead, they follow
#   rules enforced by a **TrafficMediator**.
#
# Classifier:
#   - Category: Behavioral
#   - Purpose: Centralize communication between objects.
#   - Key idea: Objects talk to the mediator instead of talking to each other.
#   - Common use: UI dialogs, messaging systems, traffic control, workflow engines.

# What Makes It Unique:
#   Mediator reduces complex many-to-many relationships into a simple
#   one-to-many relationship between participants and the mediator.
#   This keeps objects independent and focused only on their own behavior.
# ==============================================

# -----------------------------
# Mediator class (TrafficMediator)
# -----------------------------
class TrafficMediator:
    # Manages car movement and enforces traffic rules.

    def __init__(self):
        self.cars_waiting = []
        self.green_light_direction = None

    def register_car(self, car):
        self.cars_waiting.append(car)
        print(f"{car.name} arrived at the intersection from {car.direction}.")

    def set_green_light(self, direction):
        # Only cars from this direction may go.
        self.green_light_direction = direction
        print(f"GREEN LIGHT for {direction.upper()} traffic.")
        self.allow_cars_to_move()

    def allow_cars_to_move(self):
        for car in list(self.cars_waiting):
            if car.direction == self.green_light_direction:
                car.move()
                self.cars_waiting.remove(car)


# -----------------------------
# Colleague class (Car)
# -----------------------------
class Car:
    # Represents a participant that follows mediator rules.

    def __init__(self, name, direction, mediator):
        self.name = name
        self.direction = direction
        self.mediator = mediator
        mediator.register_car(self)

    def request_to_move(self):
        # Cars do not move on their own—they ask mediator.
        print(f"{self.name} requests to move.")

    def move(self):
        print(f"{self.name} is MOVING through the intersection.")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Mediator Pattern Example (Traffic Control) ---")

    mediator = TrafficMediator()

    car1 = Car("Car A", "north", mediator)
    car2 = Car("Car B", "south", mediator)
    car3 = Car("Car C", "east", mediator)
    car4 = Car("Car D", "north", mediator)

    # All cars request to move (they cannot move directly)
    car1.request_to_move()
    car2.request_to_move()
    car3.request_to_move()
    car4.request_to_move()

    # Mediator decides which direction moves
    mediator.set_green_light("north")
    mediator.set_green_light("east")
    mediator.set_green_light("south")


# -----------------------------
# Example Output
# -----------------------------
# --- Mediator Pattern Example (Traffic Control) ---
# Car A arrived at the intersection from north.
# Car B arrived at the intersection from south.
# Car C arrived at the intersection from east.
# Car D arrived at the intersection from north.
#
# Car A requests to move.
# Car B requests to move.
# Car C requests to move.
# Car D requests to move.
#
# GREEN LIGHT for NORTH traffic.
# Car A is MOVING through the intersection.
# Car D is MOVING through the intersection.
#
# GREEN LIGHT for EAST traffic.
# Car C is MOVING through the intersection.
#
# GREEN LIGHT for SOUTH traffic.
# Car B is MOVING through the intersection.
#
#
# ==============================================
# History
# ==============================================
# The Mediator pattern was formalized in the 1994 "Design Patterns" book by
# the Gang of Four. It arose from the need to simplify complex communication
# between UI components and system modules. Instead of components referencing
# each other directly, the Mediator centralizes coordination, improving
# modularity. The pattern inspired modern event dispatchers, UI dialog managers,
# and workflow orchestrators.
# ==============================================
