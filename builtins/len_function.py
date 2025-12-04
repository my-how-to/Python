# ============================================================
#                    BUILT-IN FUNCTION — len()
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains Python's built-in len() function:
#       - what len() does
#       - how sequences use __len__()
#       - which data types support len()
#       - when len() raises errors
#       - len() performance characteristics
#       - custom classes implementing __len__()
#
# Each section prints a separator for clear output.
# ============================================================


# ============================================================
# 1. WHAT len() DOES
# ============================================================

print("\n--- SECTION 1: What len() Does ---")

numbers = [10, 20, 30]
text = "Python"

print(len(numbers))  # 3
print(len(text))     # 6


# ============================================================
# 2. len() CALLS __len__() INTERNALLY
# ============================================================

print("\n--- SECTION 2: len() Uses __len__ Under the Hood ---")

class Demo:
    def __len__(self):
        return 5

obj = Demo()
print(len(obj))      # 5
print(obj.__len__()) # also 5


# ============================================================
# 3. COLLECTIONS THAT SUPPORT len()
# ============================================================

print("\n--- SECTION 3: Supported Collections ---")

print(len([1, 2, 3]))              # list
print(len((4, 5)))                 # tuple
print(len("hello"))                # string
print(len({"a": 1, "b": 2}))       # dict → counts keys
print(len({1, 2, 3}))              # set
print(len(range(0, 20, 2)))        # range → mathematical length
print(len(bytearray([1, 2, 3])))   # bytearray


# ============================================================
# 4. COLLECTIONS THAT DO NOT SUPPORT len()
# ============================================================

print("\n--- SECTION 4: Unsupported Objects ---")

items = [42, 3.14, None, (x for x in range(5))]

for obj in items:
    try:
        print(len(obj))
    except Exception as e:
        print(f"{obj!r} → Error: {type(e).__name__}")


# ============================================================
# 5. len() MUST RETURN A NON-NEGATIVE INTEGER
# ============================================================

print("\n--- SECTION 5: Return Value Must Be >= 0 ---")

class Bad1:
    def __len__(self):
        return -10

class Bad2:
    def __len__(self):
        return "five"

for obj in (Bad1(), Bad2()):
    try:
        print(len(obj))
    except Exception as e:
        print(f"{type(obj).__name__} → Error: {type(e).__name__}")


# ============================================================
# 6. PERFORMANCE — len() IS O(1)
# ============================================================

print("\n--- SECTION 6: Performance ---")

big = list(range(1_000_000))

# Python stores sequence length internally → no counting required
print(len(big))  # instant


# ============================================================
# 7. CUSTOM CLASS WITH PROPER __len__()
# ============================================================

print("\n--- SECTION 7: Custom Class Implementation ---")

class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

b = Bag(["apple", "banana", "pear"])
print(len(b))   # 3

