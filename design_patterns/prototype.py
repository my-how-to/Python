# ==============================================
# Pattern Name: Prototype
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Prototype pattern allows creating new objects by copying existing ones,
#   instead of instantiating new classes each time.
#   This example uses a Document Template analogy — a new document is created
#   by cloning an existing one and adjusting its content.
#
#   Note: In real-world Python, cloning can also be done with the built-in
#   'copy' module (e.g., copy.deepcopy()), but here we use a custom .clone()
#   method for educational clarity. 
#   See also the "prototype_real.py" for a more realistic example.
#
# Classifier:
#   - Category: Creational
#   - Purpose: Create new objects by duplicating existing ones.
#   - Key idea: Avoid costly initialization by cloning prototypes.
#   - Common use: Editors, configuration objects, game object templates.
#
# What Makes It Unique:
#   Prototype bypasses constructors entirely by cloning.
#   This is especially useful when initialization is complex 
#   or when many similar objects are needed quickly.
# ==============================================

# -----------------------------
# Prototype class (Document)
# -----------------------------
class Document:
    """Represents a document that can be cloned."""

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def clone(self):
        """Return a new document with the same attributes."""
        return Document(self.title, self.content, self.author)

    def show(self):
        """Display document details."""
        print(f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Prototype Pattern Example ---")

    original = Document("Company Report", "Quarterly results and analysis.", "Alex")
    print("Original Document:")
    original.show()

    # Clone and modify
    copy_doc = original.clone()
    copy_doc.title = "Company Report - Copy"
    copy_doc.author = "Maria"
    print("Cloned Document:")
    copy_doc.show()

    print("Are objects the same?", original is copy_doc)
    print("Do they share the same content initially?", original.content == copy_doc.content)


# -----------------------------
# Example Output
# -----------------------------
# --- Prototype Pattern Example ---
# Original Document:
# Title: Company Report
# Author: Alex
# Content: Quarterly results and analysis.
#
# Cloned Document:
# Title: Company Report - Copy
# Author: Maria
# Content: Quarterly results and analysis.
#
# Are objects the same? False
# Do they share the same content initially? True
#
#
# ==============================================
# History
# ==============================================
# The Prototype pattern was formalized in 1994 by the Gang of Four.
# It originated from object cloning concepts in languages like Smalltalk.
# The goal is to simplify object creation by reusing existing instances
# rather than recreating them from scratch.
# ==============================================
