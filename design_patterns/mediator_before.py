# ==============================================
# Pattern Name: Mediator (Before Refactoring)
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   This file shows how code looks **before** applying the Mediator pattern.
#   Cars interact with each other directly, creating a tangled web of
#   dependencies. Each car must know about all others and decide whether it
#   can move. This leads to:
#       - high coupling
#       - repeated logic in each car
#       - difficulty adding new rules or new car types
#   This example intentionally illustrates the problem.
# ==============================================

# -----------------------------
# "Before" Version (Without Mediator)
# -----------------------------
class Car:
    # Each car checks against every other car.

    def __init__(self, name, direction):
        self.name = name
        self.direction = direction
        self.other_cars = []

    def add_other_car(self, car):
        # Every car stores references to all other cars.
        self.other_cars.append(car)

    def can_move(self):
        # Cars decide by examining others (BAD DESIGN).
        for other in self.other_cars:
            if other.direction == self.direction:
                print(f"{self.name}: Waiting, {other.name} is also coming from {self.direction}.")
                return False
        return True

    def move(self):
        if self.can_move():
            print(f"{self.name} is MOVING through the intersection.")
        else:
            print(f"{self.name} cannot move right now.")


# -----------------------------
# Example usage (Before Mediator)
# -----------------------------
if __name__ == "__main__":
    print("--- BEFORE Mediator Example (Direct Car-to-Car Communication) ---")

    car1 = Car("Car A", "north")
    car2 = Car("Car B", "north")
    car3 = Car("Car C", "east")

    # Cars must know about each other manually
    car1.add_other_car(car2)
    car1.add_other_car(car3)

    car2.add_other_car(car1)
    car2.add_other_car(car3)

    car3.add_other_car(car1)
    car3.add_other_car(car2)

    # They try to move
    car1.move()
    car2.move()
    car3.move()


# -----------------------------
# Example Output
# -----------------------------
# --- BEFORE Mediator Example (Direct Car-to-Car Communication) ---
# Car A: Waiting, Car B is also coming from north.
# Car A cannot move right now.
# Car B: Waiting, Car A is also coming from north.
# Car B cannot move right now.
# Car C is MOVING through the intersection.
#
#
# ==============================================
# History Note
# ==============================================
# This "before" example demonstrates exactly why the Mediator pattern was
# introduced. Early UI frameworks suffered from similar tangled communication
# between components. The Mediator pattern centralized this logic, making
# maintenance and extension dramatically easier.
# ==============================================
