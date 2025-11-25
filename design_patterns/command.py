# ==============================================
# Pattern Name: Command
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Command pattern turns actions (typing, deleting, etc.) into
#   separate command objects. Each command knows how to execute and undo
#   itself. This makes undo/redo clean, extendable, and decoupled from
#   the editor.
#
# What Makes It Unique:
#   Command decouples the object performing an action from the object
#   requesting it. Each action becomes an object with execute() and
#   undo() methods, enabling clean undo/redo stacks and macros.
# ==============================================


# -----------------------------
# Receiver: Text Editor
# -----------------------------
# The TextEditor performs the actual text modification.
# In the BEFORE version, undo/redo logic was mixed inside this class.
# In the Command version, the editor only provides primitive operations.
# All undo/redo logic is delegated to Command objects.
# -----------------------------
# Performs the real text operations.
# -----------------------------
class TextEditor:
    def __init__(self):
        self.text = ""

    def type_text(self, new_text):
        self.text += new_text

    def delete_last(self, num_chars):
        # Remove the last N characters (Python slice: text[:-N] means "all except last N characters")
        self.text = self.text[:-num_chars]


# -----------------------------
# Command Base Class
# -----------------------------
class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


# -----------------------------
# Concrete Command: Type Text
# -----------------------------
# This Command represents typing new text.
# It stores the typed text so it can undo itself by deleting it.
# -----------------------------
class TypeCommand(Command):
    def __init__(self, editor: TextEditor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.type_text(self.text)

    def undo(self):
        self.editor.delete_last(len(self.text))


# -----------------------------
# Concrete Command: Delete Text
# -----------------------------
# This Command represents deleting the last N characters.
# It stores the deleted characters so they can be restored on undo.
# -----------------------------
class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, num_chars):
        self.editor = editor
        self.num_chars = num_chars
        self.deleted_text = None

    def execute(self):
        self.deleted_text = self.editor.text[-self.num_chars:]
        self.editor.delete_last(self.num_chars)

    def undo(self):
        self.editor.type_text(self.deleted_text)


# -----------------------------
# Invoker: Stores history for undo/redo
# -----------------------------
# The CommandManager executes commands and maintains two stacks:
# - undo_stack: commands that can be undone
# - redo_stack: commands that were undone and can be redone
# The manager never knows what each command does internally.
# -----------------------------
class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command: Command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()  # clear redo history

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        cmd = self.undo_stack.pop()
        cmd.undo()
        self.redo_stack.append(cmd)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        cmd = self.redo_stack.pop()
        cmd.execute()
        self.undo_stack.append(cmd)


# -----------------------------
# Example usage (Command pattern)
# -----------------------------
if __name__ == "__main__":
    print("--- Command Pattern Example ---\n")

    editor = TextEditor()
    manager = CommandManager()

    # Type commands
    manager.execute_command(TypeCommand(editor, "Hello"))
    manager.execute_command(TypeCommand(editor, " World"))
    print("Current text:", editor.text)

    # Delete command
    # Delete the last word (instead of a number)
    manager.execute_command(DeleteCommand(editor, len(" World")))
    print("After deletion:", editor.text)

    # Show internal stacks for clarity
    #print("Undo stack:", [type(cmd).__name__ for cmd in manager.undo_stack])
    #print("Redo stack:", [type(cmd).__name__ for cmd in manager.redo_stack])

    # Undo
    manager.undo()
    print("After undo:", editor.text)

    # Show internal stacks
    print("Undo stack:", [type(cmd).__name__ for cmd in manager.undo_stack])
    print("Redo stack:", [type(cmd).__name__ for cmd in manager.redo_stack])

    # Redo
    manager.redo()
    print("After redo:", editor.text)

    # Show internal stacks
    #print("Undo stack:", [type(cmd).__name__ for cmd in manager.undo_stack])
    #print("Redo stack:", [type(cmd).__name__ for cmd in manager.redo_stack])


# -----------------------------
# Example Output
# -----------------------------
# --- Command Pattern Example ---
# Current text: Hello World
# After deletion: Hello
# After undo: Hello World
# After redo: Hello
#
#
# ==============================================
# History
# ==============================================
# The Command pattern grew from early GUI and text editor systems, where
# actions needed to be stored, executed later, undone, redone, logged,
# or combined into macros. Early editors mixed undo logic with editing
# code, causing tangled designs. Command provided a clean way to treat
# actions as first-class objects with execute() and undo() methods.
# ==============================================
