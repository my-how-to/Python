# ==============================================
# Pattern Name: Observer
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Observer pattern defines a one-to-many dependency between objects so that
#   when one object (the Subject) changes state, all its dependents (Observers)
#   are automatically notified and updated. In this example, the Teacher acts as
#   the Subject, and Students are Observers who receive announcements.
#
# Classifier:
#   - Category: Behavioral
#   - Purpose: Enable communication between objects without tight coupling.
#   - Key idea: Observers register to listen for changes in a Subject.
#   - Common use: Event-driven systems, user interfaces, data synchronization.

# What Makes It Unique:
#   Observer enables automatic event broadcasting.
#   Objects stay in sync without manually calling them, 
#   creating loose coupling between publisher and subscribers.
# ==============================================

# -----------------------------
# Subject class (Teacher)
# -----------------------------
class Teacher:
    """Represents the Subject. Keeps a list of students and notifies them."""

    def __init__(self, name):
        self.name = name
        self._students = []

    def attach(self, student):
        """Register a student to receive notifications."""
        self._students.append(student)
        print(f"{student.name} has joined {self.name}'s class.")

    def detach(self, student):
        """Remove a student from the notification list."""
        if student in self._students:
            self._students.remove(student)
            print(f"{student.name} has left {self.name}'s class.")

    def notify(self, message):
        """Notify all attached students."""
        print(f"\n{self.name} says: {message}")
        for student in self._students:
            student.update(message)


# -----------------------------
# Observer class (Student)
# -----------------------------
class Student:
    """Represents the Observer. Reacts to notifications from the Teacher."""

    def __init__(self, name):
        self.name = name

    def update(self, message):
        """React to a message from the teacher."""
        print(f"{self.name} received message: {message}")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Observer Pattern Example ---")

    teacher = Teacher("Mr. Smith")

    alice = Student("Alice")
    bob = Student("Bob")
    carol = Student("Carol")

    # Students register to the teacher's class
    teacher.attach(alice)
    teacher.attach(bob)
    teacher.attach(carol)

    # Teacher sends first announcement
    teacher.notify("Welcome to the Observer pattern lesson!")

    # One student leaves the class
    teacher.detach(bob)

    # Teacher sends another announcement
    teacher.notify("Don't forget to read Chapter 5 for homework.")


# -----------------------------
# Example Output
# -----------------------------
# --- Observer Pattern Example ---
# Alice has joined Mr. Smith's class.
# Bob has joined Mr. Smith's class.
# Carol has joined Mr. Smith's class.
#
# Mr. Smith says: Welcome to the Observer pattern lesson!
# Alice received message: Welcome to the Observer pattern lesson!
# Bob received message: Welcome to the Observer pattern lesson!
# Carol received message: Welcome to the Observer pattern lesson!
#
# Bob has left Mr. Smith's class.
#
# Mr. Smith says: Don't forget to read Chapter 5 for homework.
# Alice received message: Don't forget to read Chapter 5 for homework.
# Carol received message: Don't forget to read Chapter 5 for homework.


# ==============================================
# History
# ==============================================
# The Observer pattern originated in early GUI frameworks and was formalized
# in the 1994 \"Design Patterns\" book by the Gang of Four. It provided a clear
# way for one object (the Subject) to broadcast updates to multiple dependents
# (Observers). This structure influenced the Model-View-Controller (MVC)
# architecture and modern event-driven programming.
# ==============================================
