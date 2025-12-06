# ============================================================
#                 BUILT-IN FUNCTION — print()
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explores Python's print() function in depth:
#       - positional vs keyword arguments
#       - controlling separators and line endings
#       - printing to files and stderr
#       - flushing output for real-time logs
#       - string formatting helpers (f-strings, format(), *)
#       - custom __str__/__repr__ hooks
#       - debugging patterns and pitfalls
#
# Run the file to observe each section's output.
# ============================================================


# ============================================================
# 1. BASIC USAGE & MULTIPLE ARGUMENTS
# ============================================================
print("\n--- SECTION 1: print() Basics ---")

print("Hello, world!")          # simplest usage
print("Mix types:", 1, True)    # accepts any number of arguments
print("Inline", "space", "separated")  # default sep=" "


# ============================================================
# 2. CUSTOM SEPARATORS AND LINE ENDINGS
# ============================================================
print("\n--- SECTION 2: Separators & Endings ---")

print("comma", "separated", sep=", ")
print("no newline", end="")
print(" — appended thanks to end=''")

print("countdown", 3, 2, 1, sep=" 🕒 ", end="... go!\n")


# ============================================================
# 3. PRINTING TO FILES OR STDERR
# ============================================================
print("\n--- SECTION 3: Redirecting Output ---")

from pathlib import Path
import sys

log_path = Path("print_demo.log")
with log_path.open("w", encoding="utf-8") as fh:
    print("Logged line 1", file=fh)
    print("Logged line 2", file=fh)

print(f"Wrote to {log_path.resolve()}")
print("This goes to stderr", file=sys.stderr)


# ============================================================
# 4. FORCE FLUSHING FOR REAL-TIME OUTPUT
# ============================================================
print("\n--- SECTION 4: Flushing Output ---")

import time

for n in range(3):
    print("Tick", n, end="\r", flush=True)  # flush sends text immediately
    time.sleep(0.1)
print("\nFlushed tick loop complete.")


# ============================================================
# 5. FORMATTING STRINGS
# ============================================================
print("\n--- SECTION 5: Formatting Helpers ---")

name = "Alex"
score = 9.375

print(f"f-string → {name} scored {score:.2f}")
print("format() → {} scored {:.2f}".format(name, score))
print("percent style → %s scored %.2f" % (name, score))


# ============================================================
# 6. UNPACKING ITERABLES WITH *
# ============================================================
print("\n--- SECTION 6: Iterable Unpacking ---")

values = ["python", "rocks", 2024]
print(*values)                        # expands into positional args
print("CSV:", *values, sep=", ")


# ============================================================
# 7. CUSTOM OBJECTS (__str__ vs __repr__)
# ============================================================
print("\n--- SECTION 7: Custom Objects ---")

class Sample:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Pretty view: {self.data}"

    def __repr__(self):
        return f"Sample(data={self.data!r})"

obj = Sample({"active": True})
print(obj)           # uses __str__
print([obj])         # list display falls back to __repr__


# ============================================================
# 8. DEBUGGING PATTERNS
# ============================================================
print("\n--- SECTION 8: Debug Output ---")

def fetch_user(user_id):
    print(f"[DEBUG] fetch_user id={user_id}")
    return {"id": user_id, "name": "Demo"}

result = fetch_user(101)
print("Result:", result)


# ============================================================
# 9. PITFALLS & TIPS
# ============================================================
print("\n--- SECTION 9: Pitfalls & Tips ---")

print("Joining numbers directly:", 1, 2, 3)
print("Better for strings:", " ".join(str(n) for n in (1, 2, 3)))

print("Beware repeated sep usage:", "path", "to", "file", sep="\\")
print(r"Better to join manually: \"\\\".join(...)")  # raw string for clarity

print("\nLesson complete: print() is flexible once you learn its keyword controls.")
