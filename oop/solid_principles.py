#=========================================
#      SOLID OOP PRINCIPLES — OVERVIEW
#=========================================
#
# This file explains the 5 SOLID principles with:
#     - short descriptions
#     - "What Makes It Unique" notes
#     - simple Python examples
# 
# SOLID stands for:
#     - S: Single Responsibility Principle
#     - O: Open–Closed Principle
#     - L: Liskov Substitution Principle
#     - I: Interface Segregation Principle
#     - D: Dependency Inversion Principle

# ============================================================
# 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# ============================================================

"""
Description:
    A class should have only one reason to change.
    In other words, it should be responsible for only one thing.

What It Says:
    "One class — one main responsibility."

What Makes It Unique:
    SRP focuses on separating *kinds of changes*.
    If a class keeps changing for different unrelated reasons
    (business rules, UI, logging, storage), it violates SRP.
"""

class Invoice:
    # Handles invoice data and total calculation only.
    def __init__(self, items):
        self.items = items  # list of (name, price)

    def total(self):
        return sum(price for _, price in self.items)


class InvoicePrinter:
    # Prints invoice only — does NOT save or calculate.
    def print(self, invoice: Invoice):
        print("=== INVOICE ===")
        for name, price in invoice.items:
            print(f"{name}: {price:.2f}")
        print(f"TOTAL: {invoice.total():.2f}")


class InvoiceSaver:
    # Saves invoice to a file — nothing else.
    def save_to_file(self, invoice: Invoice, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            for name, price in invoice.items:
                f.write(f"{name}: {price:.2f}\n")
            f.write(f"TOTAL: {invoice.total():.2f}\n")


# SRP demo
if __name__ == "__main__":
    print("=== SRP DEMO ===")

    items = [("Book", 10.0), ("Pen", 2.5)]
    invoice = Invoice(items)

    printer = InvoicePrinter()
    printer.print(invoice)

    saver = InvoiceSaver()
    saver.save_to_file(invoice, "invoice.txt")
    print()


# ============================================================
# 2. OPEN–CLOSED PRINCIPLE (OCP)
# ============================================================

"""
Description:
    Software entities (classes, modules, functions) should be:
        - open for extension
        - closed for modification

What It Says:
    "You can extend behavior without editing existing, tested code."

What Makes It Unique:
    OCP encourages using abstraction (base classes / interfaces)
    so that we add new features by creating new classes, 
    not by changing old ones everywhere.
"""

class Shape:
    # Base interface-like class
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def total_area(shapes):
    # Works with any future shapes (Triangle, Polygon, etc.)
    return sum(shape.area() for shape in shapes)


# OCP demo
if __name__ == "__main__":
    print("=== OCP DEMO ===")

    shapes = [
        Circle(3),
        Rectangle(4, 5)
    ]

    print("Circle area:", shapes[0].area())
    print("Rectangle area:", shapes[1].area())
    print("Total area:", total_area(shapes))
    print()


# ============================================================
# 3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
# ============================================================

"""
Description:
    Objects of a superclass should be replaceable with objects of its subclasses
    without breaking the correctness of the program.

What It Says:
    "Subclass objects must behave like their base class promises."

What Makes It Unique:
    LSP is about *behavioral compatibility*, not just types.
    A subclass must not:
        - weaken preconditions
        - strengthen postconditions
        - throw unexpected behavior that breaks client expectations.
"""

class Bird:
    def fly(self):
        return "Flapping wings and flying!"


class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying low."


class Penguin(Bird):
    # Violates LSP because penguins cannot fly
    def fly(self):
        raise NotImplementedError("Penguins cannot fly!")


def let_bird_fly(bird: Bird):
    print(bird.fly())


# LSP demo
if __name__ == "__main__":
    print("=== LSP DEMO ===")

    sparrow = Sparrow()
    let_bird_fly(sparrow)

    penguin = Penguin()
    try:
        let_bird_fly(penguin)
    except Exception as e:
        print("LSP VIOLATION:", e)
    print()


# ============================================================
# 4. INTERFACE SEGREGATION PRINCIPLE (ISP)
# ============================================================

"""
Description:
    Clients should not be forced to depend on methods they do not use.
    It's better to have many small, specific interfaces than one large, general one.

What It Says:
    "Don't make fat interfaces. Split them into focused ones."

What Makes It Unique:
    ISP protects clients from unnecessary responsibilities.
    Classes implement only what they really need, 
    which reduces fake or empty method implementations.
"""

class PrinterInterface:
    def print_document(self, content):
        raise NotImplementedError


class ScannerInterface:
    def scan_document(self):
        raise NotImplementedError


class MultiFunctionDevice(PrinterInterface, ScannerInterface):
    # Device that supports both print and scan
    def print_document(self, content):
        print(f"Printing: {content}")

    def scan_document(self):
        print("Scanning document...")
        return "Scanned content"


class SimplePrinter(PrinterInterface):
    # Printer that does not scan
    def print_document(self, content):
        print(f"Simple printer: {content}")


# ISP demo
if __name__ == "__main__":
    print("=== ISP DEMO ===")

    sp = SimplePrinter()
    sp.print_document("Invoice summary")

    mfd = MultiFunctionDevice()
    mfd.print_document("Full Report")
    result = mfd.scan_document()
    print("Scan result:", result)
    print()


# ============================================================
# 5. DEPENDENCY INVERSION PRINCIPLE (DIP)
# ============================================================

"""
Description:
    - High-level modules should not depend on low-level modules.
      Both should depend on abstractions.
    - Abstractions should not depend on details.
      Details should depend on abstractions.

What It Says:
    "Depend on interfaces, not concrete classes."

What Makes It Unique:
    DIP pushes you to inject dependencies via interfaces or abstract classes.
    This makes code more testable, flexible, and independent from details
    like concrete DBs, loggers, or external services.
"""

class MessageSender:
    # Abstraction
    def send(self, to, message):
        raise NotImplementedError


class EmailSender(MessageSender):
    def send(self, to, message):
        print(f"[EMAIL to {to}] {message}")


class SmsSender(MessageSender):
    def send(self, to, message):
        print(f"[SMS to {to}] {message}")


class NotificationService:
    # High-level class depends on abstraction
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify_user(self, user_contact, text):
        self.sender.send(user_contact, text)


# DIP demo
if __name__ == "__main__":
    print("=== DIP DEMO ===")

    email_service = NotificationService(EmailSender())
    email_service.notify_user("user@example.com", "Welcome!")

    sms_service = NotificationService(SmsSender())
    sms_service.notify_user("+123456789", "Your code is 1234.")
    print()
