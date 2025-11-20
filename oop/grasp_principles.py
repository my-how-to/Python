#=========================================
#      GRASP OOP PRINCIPLES — OVERVIEW
#=========================================
# 
# GRASP = General Responsibility Assignment Software Patterns
# These explain how to assign responsibilities in OOP.
# 
# This file explains the 9 GRASP principles with:
#     - clear descriptions
#     - "What Makes It Unique" notes
#     - simple Python examples
#     - print demonstrations for all principles
# 
# GRASP stands for:
#     - Information Expert
#     - Creator
#     - Controller
#     - Low Coupling
#     - High Cohesion
#     - Polymorphism
#     - Pure Fabrication
#     - Indirection
#     - Protected Variations
# 

# ============================================================
# 1. INFORMATION EXPERT
# ============================================================

"""
Description:
    Assign responsibility to the class that has the necessary information
    to fulfill that responsibility.

What It Says:
    "Give the work to the object that has the data."

What Makes It Unique:
    Avoids guessing where methods belong.
    Lets the design emerge from the data that objects actually hold.
"""

class Order:
    # The Order has the data → it should compute the total.
    def __init__(self, items):
        self.items = items  # list of (name, price)

    def total(self):
        return sum(price for _, price in self.items)

# Demo
if __name__ == "__main__":
    print("=== INFORMATION EXPERT DEMO ===")
    order = Order([("Book", 10), ("Pen", 2)])
    print("Order total:", order.total())
    print()


# ============================================================
# 2. CREATOR
# ============================================================

"""
Description:
    A class should create objects if:
        - it contains the objects
        - it closely uses them
        - it has the initializing data

What It Says:
    "The one who knows how should create."

What Makes It Unique:
    Helps avoid random creation from unrelated classes.
"""

class User:
    def __init__(self, name):
        self.name = name

    # User creates its own notifications → natural creator.
    def create_notification(self, message):
        return Notification(self.name, message)

class Notification:
    def __init__(self, user_name, message):
        self.user_name = user_name
        self.message = message

# Demo
if __name__ == "__main__":
    print("=== CREATOR DEMO ===")
    user = User("Alex")
    n = user.create_notification("Welcome!")
    print("Notification created:", n.user_name, "-", n.message)
    print()


# ============================================================
# 3. CONTROLLER
# ============================================================

"""
Description:
    Assign the role of handling external system events
    to a "controller" object.

What It Says:
    "Let a controller coordinate the work, not the UI or low-level classes."

What Makes It Unique:
    Provides a single entry point for a use case.
"""

class OrderController:
    # Acts as the system controller for "place order" use case
    def place_order(self, user, items):
        order = Order(items)
        total = order.total()
        print(f"Controller: {user} placed an order worth {total}")

# Demo
if __name__ == "__main__":
    print("=== CONTROLLER DEMO ===")
    oc = OrderController()
    oc.place_order("Alex", [("Shoes", 50), ("Socks", 10)])
    print()


# ============================================================
# 4. LOW COUPLING
# ============================================================

"""
Description:
    Classes should depend on each other as little as possible.

What It Says:
    "Reduce how much classes know about each other."

What Makes It Unique:
    Improves flexibility, maintainability, and ease of testing.
"""

class EmailService:
    def send(self, user, message):
        print(f"Email to {user}: {message}")

class UserNotifierLowCoupling:
    # Depends only on EmailService interface-like class
    def __init__(self, email_service):
        self.email_service = email_service

    def notify(self, user, message):
        self.email_service.send(user, message)

# Demo
if __name__ == "__main__":
    print("=== LOW COUPLING DEMO ===")
    notifier = UserNotifierLowCoupling(EmailService())
    notifier.notify("Alex", "Your order shipped!")
    print()


# ============================================================
# 5. HIGH COHESION
# ============================================================

"""
Description:
    A class should do one well-focused task.

What It Says:
    "Keep classes tight and purposeful."

What Makes It Unique:
    Opposite of God-class anti-pattern.
"""

class ReportBuilder:
    # High cohesion: only builds reports, does not save or send them.
    def build(self, data):
        return f"Report: {data}"

# Demo
if __name__ == "__main__":
    print("=== HIGH COHESION DEMO ===")
    rb = ReportBuilder()
    print(rb.build("Sales increased"))
    print()


# ============================================================
# 6. POLYMORPHISM
# ============================================================

"""
Description:
    Use polymorphism to handle variations instead of switches/ifs.

What It Says:
    "Ask objects to behave, don't inspect their type."

What Makes It Unique:
    Replaces big if/elif/type-checking blocks.
"""

class Sender:
    def send(self, msg):
        raise NotImplementedError

class EmailSenderPoly(Sender):
    def send(self, msg):
        print("Email:", msg)

class SmsSenderPoly(Sender):
    def send(self, msg):
        print("SMS:", msg)

def notify(sender: Sender, msg):
    sender.send(msg)

# Demo
if __name__ == "__main__":
    print("=== POLYMORPHISM DEMO ===")
    notify(EmailSenderPoly(), "Hello by email")
    notify(SmsSenderPoly(), "Hello by SMS")
    print()


# ============================================================
# 7. PURE FABRICATION
# ============================================================

"""
Description:
    If a responsibility does not belong to any domain class,
    create a separate helper class.

What It Says:
    "If no natural object can do it, invent one."

What Makes It Unique:
    Protects cohesion in domain objects.
"""

class FileLogger:
    # Pure Fabrication: handles logging, does not belong to domain model.
    def log(self, text):
        print("[LOG]:", text)

# Demo
if __name__ == "__main__":
    print("=== PURE FABRICATION DEMO ===")
    logger = FileLogger()
    logger.log("Payment received")
    print()


# ============================================================
# 8. INDIRECTION
# ============================================================

"""
Description:
    Use an intermediate object to reduce coupling between other classes.

What It Says:
    "Use a middleman to keep classes independent."

What Makes It Unique:
    Often implemented using mediators, event dispatchers, etc.
"""

class PaymentGateway:
    def process(self, amount):
        print(f"Processing payment: {amount}")

class PaymentProcessor:
    # Indirection: acts as a middle layer between the system and the gateway.
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        self.gateway.process(amount)

# Demo
if __name__ == "__main__":
    print("=== INDIRECTION DEMO ===")
    pg = PaymentGateway()
    processor = PaymentProcessor(pg)
    processor.pay(99)
    print()


# ============================================================
# 9. PROTECTED VARIATIONS
# ============================================================

"""
Description:
    Protect the system from the impact of variations or changes.

What It Says:
    "Design so future changes don't break existing code."

What Makes It Unique:
    Often implemented using interfaces, wrappers, and abstraction.
"""

class Storage:
    # Abstract layer → protects rest of system from storage choice
    def save(self, data):
        raise NotImplementedError

class FileStorage(Storage):
    def save(self, data):
        print("Saving to file:", data)

class DatabaseStorage(Storage):
    def save(self, data):
        print("Saving to database:", data)

def save_data(storage: Storage, data):
    storage.save(data)

# Demo
if __name__ == "__main__":
    print("=== PROTECTED VARIATIONS DEMO ===")
    save_data(FileStorage(), "Hello")
    save_data(DatabaseStorage(), "Hello")
    print()
