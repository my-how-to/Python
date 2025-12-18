# ============================================================
#                LESSON — NEGATIVE INDICES
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains how negative indexing works in Python:
#       - what negative indices are
#       - why they exist
#       - how to use them with lists, strings, tuples
#       - negative slicing
#       - out-of-range negatives
#       - where negative indexing does NOT work
#
# Each section prints a separator for clean, educational output.
# ============================================================

print("\n# -----------------------------")
print("# 1. BASIC IDEA OF NEGATIVE INDICES")
print("# -----------------------------\n")

nums = [10, 20, 30, 40, 50]

print(nums[-1])   # last element → 50
print(nums[-2])   # second from end → 40
print(nums[-3])   # third from end → 30

print("\n# -----------------------------")
print("# 2. WHY NEGATIVE INDICES EXIST")
print("# -----------------------------\n")

# Traditional way:
print(nums[len(nums) - 1])  # 50

# Cleaner way:
print(nums[-1])             # also 50

print("\n# -----------------------------")
print("# 3. NEGATIVE INDICES IN MULTIPLE COLLECTIONS")
print("# -----------------------------\n")

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_string = "Python"

print(my_list[-1])   # 3
print(my_tuple[-2])  # 5
print(my_string[-3]) # 'h'

print("\n# -----------------------------")
print("# 4. NEGATIVE INDICES IN SLICING")
print("# -----------------------------\n")

letters = ["a", "b", "c", "d", "e" , "f", "g"]

print(letters[-3:-1])   # ['e', 'f']  # from -3 to -2  
print(letters[:-2])     # ['a', 'b', 'c', 'd', 'e']  # all but last 2
print(letters[-4:-1])   # ['d', 'e', 'f']  # from -4 to -2
print(letters[-5:])     # ['c', 'd', 'e', 'f', 'g']  # from -5 to end       
print(letters[:])       # entire list



# Mixed example:
print(letters[1:-1])     # everything except first and last

print("\n# -----------------------------")
print("# 5. NEGATIVE STEP (REVERSING SEQUENCES)")
print("# -----------------------------\n")

nums = [1, 2, 3, 4, 5]
print(nums[::-1])   # reversed → [5, 4, 3, 2, 1]

# Partial reverse:
print(nums[4:1:-1])  # [5, 4, 3] from index 4 to 2 in reverse
print(nums[4:1:-2])  # [5, 3] every second element in reverse

print("\n# -----------------------------")
print("# 6. OUT-OF-RANGE NEGATIVE INDICES")
print("# -----------------------------\n")

test = [1, 2, 3]

try:
    print(test[-4])  # error → too negative
except Exception as e:
    print(f"Error: {type(e).__name__}")  

print("\n# -----------------------------")
print("# 7. COLLECTIONS WITHOUT NEGATIVE INDICES")
print("# -----------------------------\n")

# Sets and dicts have no meaningful order
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}

for obj in (my_set, my_dict):
    try:
        print(obj[-1])
    except Exception as e:
        print(f"{type(obj).__name__} → Error: {type(e).__name__}")

print("\n# -----------------------------")
print("# 8. CUSTOM CLASS SUPPORTING NEGATIVE INDICES")
print("# -----------------------------\n")

class MySeq:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        if idx < 0:
            idx = len(self.data) + idx
        return self.data[idx]

custom = MySeq(["x", "y", "z"])
print(custom[-1])   # 'z'
print(custom[-2])   # 'y'
