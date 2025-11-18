# ==============================================
# Prototype (Real-World Example)
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   A realistic example of the Prototype pattern using Python's built-in
#   'copy' module to clone complex objects that contain nested data.
#   This approach is common in production code when duplicating configurations,
#   templates, or objects with expensive initialization.
#
# Classifier:
#   - Category: Creational
#   - Purpose: Efficiently duplicate complex or expensive-to-create objects.
#   - Key idea: Use cloning (deepcopy) to reuse and modify prototypes.
#   - Common use: Config management, game entities, document templates.
# ==============================================

import copy # Used for cloning complex (nested) objects safely

# -----------------------------
# Complex class (Document with nested data)
# -----------------------------
class Document:
    """Represents a document with nested metadata."""

    def __init__(self, title, content, metadata):
        self.title = title
        self.content = content
        self.metadata = metadata  # dictionary (nested structure)

    def clone(self):
        """Create a deep copy of the document."""
        return copy.deepcopy(self)

    def show(self):
        """Display document details."""
        print(f"Title: {self.title}\nAuthor: {self.metadata['author']}\nStatus: {self.metadata['status']}\nContent: {self.content}\n")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Prototype Real-World Example ---")

    original = Document(
        title="Project Plan",
        content="Define milestones and resource allocation.",
        metadata={"author": "Alex", "status": "draft", "reviewed": False}
    )

    print("Original Document:")
    original.show()

    # Clone and adjust
    copy_doc = original.clone()
    copy_doc.title = "Project Plan - Final"
    copy_doc.metadata["author"] = "Maria"
    copy_doc.metadata["status"] = "approved"
    copy_doc.metadata["reviewed"] = True

    print("Cloned Document:")
    copy_doc.show()

    # Demonstrate independence
    print("After modifying clone, original remains unchanged:")
    original.show()

    print("Are objects the same?", original is copy_doc)
    print("Do they share the same metadata?", original.metadata is copy_doc.metadata)


# -----------------------------
# Example Output
# -----------------------------
# --- Prototype Real-World Example ---
# Original Document:
# Title: Project Plan
# Author: Alex
# Status: draft
# Content: Define milestones and resource allocation.
#
# Cloned Document:
# Title: Project Plan - Final
# Author: Maria
# Status: approved
# Content: Define milestones and resource allocation.
#
# After modifying clone, original remains unchanged:
# Title: Project Plan
# Author: Alex
# Status: draft
# Content: Define milestones and resource allocation.
#
# Are objects the same? False
# Do they share the same metadata? False
#
#
# ==============================================
# History
# ==============================================
# In real-world Python development, the Prototype pattern is often implemented
# using the 'copy' module (especially deepcopy) to duplicate objects safely.
# This prevents shared references between complex data structures. It's widely
# used in game development, configuration management, and document systems.
# ==============================================
