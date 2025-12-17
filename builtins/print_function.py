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


print("\n# -----------------------------")
print("# 1. print() Basics")
print("# -----------------------------\n")

# print() collects every positional argument, converts each to a string, and joins them with sep.
# Keyword arguments such as sep, end, file, and flush fine-tune how the text is joined and delivered.
print("Hello, world!")          # simplest usage
print("Mix types:", 1, True)    # accepts any number of arguments
print("Inline", "space", "separated")  # default sep=" "


print("\n# -----------------------------")
print("# 2. Separators & Endings")
print("# -----------------------------\n")

# Custom sep replaces the default single space separator (sep=" ") between args.
# Think of sep as the glue inserted between each converted argument.
print("comma", "separated", sep=", ")
# Custom end overrides the default newline (end="\n") appended after every print call.
# Useful when you want progress text on one line or to add a custom suffix.
print("no newline", end="")
print(" — appended thanks to end=''")  # resumes normal newline here

print("countdown", 3, 2, 1, sep=" 🕒 ", end="... go!\n")


print("\n# -----------------------------")
print("# 3. Redirecting Output")
print("# -----------------------------\n")

from pathlib import Path
import sys

log_path = Path("print_demo.log")
with log_path.open("w", encoding="utf-8") as fh:
    # file=<stream> lets you pick the destination: stdout (default), stderr, or an opened file.
    # Here every print call writes directly to print_demo.log instead of the console.
    print("Logged line 1", file=fh)
    print("Logged line 2", file=fh)

print(f"Wrote to {log_path.resolve()}")
print("This goes to stderr", file=sys.stderr)  # demonstrate stderr target


print("\n# -----------------------------")
print("# 4. Flushing Output")
print("# -----------------------------\n")

import time

for n in range(3):
    # flush=True forces Python to push the text to the terminal immediately
    # rather than waiting for the buffer to fill—ideal for status updates or logs.
    print("Tick", n, end="\r", flush=True)
    time.sleep(0.1)
print("\nFlushed tick loop complete.")


print("\n# -----------------------------")
print("# 5. Formatting Helpers")
print("# -----------------------------\n")

name = "Alex"
score = 9.375

# f-strings evaluate expressions inline; {score:.2f} formats score as fixed-point with 2 decimals.
print(f"f-string → {name} scored {score:.2f}")
# str.format() accepts placeholders and optional format specifiers for alignment/precision control.
print("format() → {} scored {:.2f}".format(name, score))
# Percent formatting mirrors C's printf%; handy for legacy code or when translators expect % tokens.
print("percent style → %s scored %.2f" % (name, score))


print("\n# -----------------------------")
print("# 6. Iterable Unpacking")
print("# -----------------------------\n")

values = ["python", "rocks", 2024]
print(*values)                        # expands into positional args
print("CSV:", *values, sep=", ")


print("\n# -----------------------------")
print("# 7. Custom Objects")
print("# -----------------------------\n")

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


print("\n# -----------------------------")
print("# 8. Debug Output")
print("# -----------------------------\n")

def fetch_user(user_id):
    print(f"[DEBUG] fetch_user id={user_id}")
    return {"id": user_id, "name": "Demo"}

result = fetch_user(101)
print("Result:", result)


print("\n# -----------------------------")
print("# 9. Pitfalls & Tips")
print("# -----------------------------\n")

print("Joining numbers directly:", 1, 2, 3)
print("Better for strings:", " ".join(str(n) for n in (1, 2, 3)))

print("Beware repeated sep usage:", "path", "to", "file", sep="\\")
print(r"Better to join manually: \"\\\".join(...)")  # raw string for clarity

