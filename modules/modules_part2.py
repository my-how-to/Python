# ============================================================
#            LESSON — MODULES (PART 2: STANDARD LIBRARY+)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Extends the modules lesson beyond PCEP basics. Explore key
#   standard-library modules, packages/submodules, __all__
#   controls, module caching & reloads, dynamic imports, and
#   lazy imports for performance-sensitive code.
#
# Contents:
#   1. Standard library tour (math, random, datetime, pathlib)
#   2. Packages and submodules
#   3. __all__ and controlled star-imports
#   4. Module caching and importlib.reload()
#   5. Dynamic imports with importlib.import_module()
#   6. Lazy imports inside functions
#
# ============================================================

import datetime as dt
import importlib
import random
import sys
import types
from collections import Counter
from decimal import Decimal
from pathlib import Path


print("\n# -----------------------------")
print("# 1. Standard library tour")
print("# -----------------------------\n")

# math/random: scientific constants and pseudo-random numbers
angles = [0, 30, 45, 60, 90]
print("Random sample angle:", random.choice(angles))
print("Random float in [0, 1):", random.random())

# decimal: precise financial arithmetic
subtotal = Decimal("19.99") + Decimal("4.99")
tax = subtotal * Decimal("0.0825")
print("Decimal subtotal:", subtotal)
print("Decimal tax:", tax.quantize(Decimal("0.01")))

# datetime: timestamps and differences
start = dt.datetime(2024, 1, 1)
now = dt.datetime.now()
print("Days since New Year:", (now - start).days)

# pathlib: path-safe filesystem handling
lesson_path = Path(__file__)
print("This lesson lives at:", lesson_path)
print("Parent directory:", lesson_path.parent)


print("\n# -----------------------------")
print("# 2. Packages and submodules")
print("# -----------------------------\n")

# collections is a package; Counter is a class defined inside.
tech_stack = ["python", "sql", "python", "bash", "python", "git"]
stack_counts = Counter(tech_stack)
print("Stack counts:", stack_counts)
print("Most common language:", stack_counts.most_common(1))

# pathlib exposes classes via its package namespace as well.
tmp_dir = Path.cwd() / "tmp_modules_demo"
print("Temporary folder path:", tmp_dir)


print("\n# -----------------------------")
print("# 3. __all__ and star-import control")
print("# -----------------------------\n")

demo_module = types.ModuleType("demo_module")
demo_module.__all__ = ["public_value"]
demo_module.public_value = "You can import me with *"
demo_module._secret = "Hidden unless accessed via module attribute."
sys.modules["demo_module"] = demo_module

from demo_module import *  # type: ignore # noqa: F401,F403

print("Star import sees:", public_value)
try:
    print(_secret)  # type: ignore # noqa: F821
except NameError:
    print("_secret stays hidden because it's not in __all__.")


print("\n# -----------------------------")
print("# 4. Module caching and importlib.reload()")
print("# -----------------------------\n")

print("random stored in sys.modules:", sys.modules["random"])
second_random = importlib.import_module("random")
print("Re-import returns the SAME object:", random is second_random)

random.seed(42)
print("First number after seeding:", random.random())
importlib.reload(random)
print("Number after reload (state reset):", random.random())


print("\n# -----------------------------")
print("# 5. Dynamic imports with importlib.import_module()")
print("# -----------------------------\n")

module_name = "math"
math_module = importlib.import_module(module_name)
print("Dynamically imported:", math_module)
print("math_module.sqrt(81) =", math_module.sqrt(81))

json_module = importlib.import_module("json")
print("Dumps JSON dynamically:", json_module.dumps({"status": "ok"}))


print("\n# -----------------------------")
print("# 6. Lazy imports inside functions")
print("# -----------------------------\n")


def load_yaml_example():
    # Import inside the function so PyYAML (if installed) is only
    # loaded when the feature is actually used.
    import json  # using json as a stand-in to keep this lesson runnable

    example = {"lesson": "modules", "level": "advanced"}
    return json.dumps(example)


print("Lazy import function result:", load_yaml_example())
