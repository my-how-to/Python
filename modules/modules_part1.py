# ============================================================
#            LESSON — MODULES (PART 1: ESSENTIALS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Introduces Python modules at the PCEP level: what they are,
#   why we use them, import statements, aliases, selective
#   imports, inspection helpers, the module search path, and
#   the __name__ guard that keeps scripts reusable.
#
# Contents:
#   1. What is a module?
#   2. Basic import and attribute access
#   3. Import aliases with "as"
#   4. Selective imports with "from"
#   5. Inspecting a module (dir, help, __doc__)
#   6. Module search path (sys.path)
#   7. __name__ and the script guard pattern
#
# ============================================================

import importlib
import math
import statistics as stats
import sys
import textwrap


print("\n# -----------------------------")
print("# 1. What is a module?")
print("# -----------------------------\n")

# Any Python file (.py) is a module. The import system loads it once
# and keeps the resulting module object in memory.

print("math is a module object:", math)
print("type(math):", type(math))
print("textwrap module:", textwrap)
print("textwrap.__name__:", textwrap.__name__)
print("textwrap file path:", textwrap.__file__)


print("\n# -----------------------------")
print("# 2. Basic import and attribute access")
print("# -----------------------------\n")

# After importing, you access functions/variables with dot notation.
radius_cm = 7
circumference = 2 * math.pi * radius_cm
sample_text = "Modules make Python code organized and reusable."
print(f"Circumference for radius {radius_cm}cm:", circumference)
print("Wrapped text (textwrap.fill):")
print(textwrap.fill(sample_text, width=40))


print("\n# -----------------------------")
print("# 3. Import aliases with 'as'")
print("# -----------------------------\n")

# Aliases shorten long module names and prevent collisions.
sample_scores = [7, 8, 10, 9]
print("statistics module alias is 'stats'")
print("Mean:", stats.mean(sample_scores))
print("Median:", stats.median(sample_scores))


print("\n# -----------------------------")
print("# 4. Selective imports with 'from'")
print("# -----------------------------\n")

# Bring only the names you need into the current namespace.
from math import factorial, tau  # noqa: E402 (kept here for teaching flow)

print("Factorial of 5:", factorial(5))
print("Tau constant:", tau)


print("\n# -----------------------------")
print("# 5. Inspecting a module (dir, help, __doc__)")
print("# -----------------------------\n")

public_api = [name for name in dir(textwrap) if not name.startswith("_")]
print("textwrap public names:", public_api[:5], "...")
print("Docstring first line:", textwrap.fill.__doc__.splitlines()[0])
print("Use help(math) for interactive docs (not shown here).")


print("\n# -----------------------------")
print("# 6. Module search path (sys.path)")
print("# -----------------------------\n")

# When you import, Python searches the directories in sys.path.
print("First 3 entries on sys.path:")
for entry in sys.path[:3]:
    print("  ->", entry)

# Current directory (where this file lives) appears near the top,
# which is why imports of neighboring files normally succeed.


print("\n# -----------------------------")
print("# 7. __name__ and the script guard")
print("# -----------------------------\n")


def guard_demo():
    print("modules_part1.__name__:", __name__)
    if __name__ == "__main__":
        print("Running modules_part1 directly → safe to execute demos.")
    else:
        print("modules_part1 was imported → skip auto-execution.")


guard_demo()

if __name__ == "__main__":
    # Sample logic that should only run when executing this file directly.
    print("Re-importing this module dynamically:")
    self_again = importlib.import_module(__name__)
    print("Same object?", self_again is sys.modules[__name__])
