# ==============================================
# Before Pattern: Observer
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how notifications were handled before the Observer pattern.
#   In this approach, the Teacher must directly call each student's method
#   manually. There is no registration, detachment, or automated notification
#   mechanism, leading to rigid and repetitive code.
#
# Classifier:
#   - Category: Behavioral
#   - Purpose: Show how notifications were sent manually before observers.
#   - Key idea: The Subject directly calls every dependent object.
#   - Common issue: Code duplication, manual management, and lack of flexibility.
# ==============================================

# -----------------------------
# Subject class (Teacher)
# -----------------------------
class Teacher:
    """Represents the Subject. Must manually notify each student."""

    def __init__(self, name):
        self.name = name

    def send_announcement(self, message, students):
        """Manually notify all students by calling each one directly."""
        print(f"\n{self.name} says: {message}")
        for student in students:
            student.receive_message(message)


# -----------------------------
# Observer class (Student)
# -----------------------------
class Student:
    """Represents the Observer. Receives messages directly from the Teacher."""

    def __init__(self, name):
        self.name = name

    def receive_message(self, message):
        """Receive a message sent manually by the teacher."""
        print(f"{self.name} received message: {message}")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Observer Example ---")

    teacher = Teacher("Mr. Smith")

    alice = Student("Alice")
    bob = Student("Bob")
    carol = Student("Carol")

    students = [alice, bob, carol]

    # Teacher manually sends messages to each student.
    teacher.send_announcement("Welcome to the lesson!", students)

    # If one student leaves, the list must be manually updated.
    students.remove(bob)
    teacher.send_announcement("Don't forget your homework!", students)

    # No dynamic attachment or detachment — everything is managed manually.


# -----------------------------
# Example Output
# -----------------------------
# --- Before Observer Example ---
#
# Mr. Smith says: Welcome to the lesson!
# Alice received message: Welcome to the lesson!
# Bob received message: Welcome to the lesson!
# Carol received message: Welcome to the lesson!
#
# Mr. Smith says: Don't forget your homework!
# Alice received message: Don't forget your homework!
# Carol received message: Don't forget your homework!


# ==============================================
# History
# ==============================================
# Before the Observer pattern was formalized in 1994 by the Gang of Four,
# developers often wrote manual notification logic, directly calling dependent
# objects one by one. This tightly coupled the sender (Teacher) and receivers
# (Students), making systems difficult to extend. The Observer pattern later
# introduced a cleaner, event-driven mechanism with attach/detach functionality.
# ==============================================
