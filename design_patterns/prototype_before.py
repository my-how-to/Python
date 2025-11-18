# ==============================================
# Before Pattern: Prototype
# Pattern Type: Creational
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how developers created similar objects before the Prototype pattern.
#   Each new document had to be manually re-created, even if it shared most
#   attributes with an existing one. This was repetitive and error-prone.
#
# Classifier:
#   - Category: Creational
#   - Purpose: Show object duplication before cloning existed.
#   - Common issue: Code repetition and inconsistent copies.
# ==============================================

# -----------------------------
# Regular class (Document)
# -----------------------------
class Document:
    """Represents a document created manually each time."""

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def show(self):
        """Display document details."""
        print(f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Before Prototype Example ---")

    # Create first document
    original = Document("Company Report", "Quarterly results and analysis.", "Alex")
    print("Original Document:")
    original.show()

    # Create a similar document manually
    # Developer must copy all fields by hand
    copy_doc = Document("Company Report - Copy", original.content, "Maria")
    print("Manually Created Copy:")
    copy_doc.show()

    # Small change in content requires updating both versions separately
    original.content = "Updated with new sales data."
    print("After modifying the original:")
    original.show()
    print("The copy remains unchanged:")
    copy_doc.show()


# -----------------------------
# Example Output
# -----------------------------
# --- Before Prototype Example ---
# Original Document:
# Title: Company Report
# Author: Alex
# Content: Quarterly results and analysis.
#
# Manually Created Copy:
# Title: Company Report - Copy
# Author: Maria
# Content: Quarterly results and analysis.
#
# After modifying the original:
# Title: Company Report
# Author: Alex
# Content: Updated with new sales data.
#
# The copy remains unchanged:
# Title: Company Report - Copy
# Author: Maria
# Content: Quarterly results and analysis.
#
# ==============================================
# History
# ==============================================
# Before the Prototype pattern was introduced, developers often re-created
# objects manually, even if they were almost identical. This caused repetition
# and errors. The Prototype pattern solved this by introducing cloning, making
# object duplication efficient and consistent.
# ==============================================
