# ==============================================
# Before Pattern: Command
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how an editor (text editor) handles operations such as
#   typing text, deleting text, undo, and redo BEFORE using the Command
#   pattern. All logic is tangled together inside the editor itself.
#   There is no clean way to store actions, undo them, or redo them.
# ==============================================


# -----------------------------
# Simple Editor (No Command Pattern)
# -----------------------------
# All operations are handled directly.
# Undo/Redo logic is mixed together with editing logic.
# Adding new actions requires modifying this entire class.
# -----------------------------
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def type_text(self, new_text):
        # Save previous state for undo
        previous = self.text
        self.undo_stack.append(previous)
        self.text += new_text

    def delete_last(self, num_chars):
        previous = self.text
        self.undo_stack.append(previous)
        self.text = self.text[:-num_chars]

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        # Save current state for redo
        current = self.text
        self.redo_stack.append(current)
        # Restore previous state
        self.text = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        # Save current state for undo
        current = self.text
        self.undo_stack.append(current)
        # Restore redo state
        self.text = self.redo_stack.pop()


# -----------------------------
# Example usage (Before Command)
# -----------------------------
if __name__ == "__main__":
    print("--- Before Command Pattern Example ---\n")

    editor = TextEditor()

    editor.type_text("Hello")
    editor.type_text(" World")
    print("Current text:", editor.text)

    editor.delete_last(6)
    print("After deletion:", editor.text)

    editor.undo()
    print("After undo:", editor.text)

    editor.redo()
    print("After redo:", editor.text)

    print(
        "\nProblem: All actions are handled directly in the editor.\n"
        "Undo/Redo logic is mixed with editing logic. Adding new actions like\n"
        "Cut, Copy, Paste, Insert, Replace requires modifying the core class."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Before Command Pattern Example ---
# Current text: Hello World
# After deletion: Hello
# After undo: Hello World
# After redo: Hello
#
#
# ==============================================
# History
# ==============================================
# The Command pattern has roots in early text editors and GUI frameworks,
# where actions needed to be stored, undone, redone, queued, and logged.
# Before commands were treated as separate objects, editors had tangled
# logic mixing state changes with undo/redo operations. The GoF book
# (1994) formalized the pattern, enabling clean undo stacks and macros.
# ==============================================
