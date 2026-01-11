# ============================================================
#            LESSON — DICTIONARIES (COLLECTIONS)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson covers dictionaries in Python: what they are,
#   how to create them, accessing, adding, updating, and
#   removing items, looping through dictionaries, checking
#   membership, and getting the length.
#   
#   A dictionary stores key-value pairs.
#   Each key must be unique, and it points to a specific value — 
#   like a real-world dictionary maps a word to its definition.
#
# Why use dictionaries?
#   They provide a way to organize and retrieve data efficiently using meaningful keys,
#   making them ideal for scenarios where you need to associate related information.
#   for example, storing user profiles, configurations, or any data that requires quick lookups.
#
# Contents:
#   1. Dictionaries — Mapped Data
#     - get()
#   2. Adding, Updating, and Removing
#     - update()
#     - pop()
#     - popitem()
#     - copy()
#     - clear()
#   3. Looping Through a Dictionary
#     - values()
#     - items()
#   4. Checking Membership & Length
#   5. keys()
#   6. setdefault()
#
print("\n# -----------------------------")
print("# 1. Dictionaries — Mapped Data")
print("# -----------------------------\n")

empty_dict = {}
print("empty dict literal:", empty_dict, type(empty_dict))

# Hanging indent keeps multi-line dicts readable and aligned.
person = {
    "name": "Alex",
    "age": 32,
    "city": "Chisinau",
}

# Each key is a unique label → use it to access the stored value.
# Keys are case-sensitive ("Name" and "name" are different keys).
print(person["name"])  # Alex
print(person["age"])   # 32

# Accessing a missing key directly raises KeyError.
try:
    print(person["country"])
except KeyError as err:
    print("KeyError:", err)

# The dictionary's get() method lets you supply a fallback instead of crashing on missing keys.
# dict_obj.get(key) returns None if the key is not found, instead of raising an exception.
print(person.get("country", "Not specified"))       # Not specified

# default value returned when key is missing
print({"x": 1}.get("y", 5))     # 5

# No default value provided, None is returned when key is missing
print({"x": 1}.get("y"))        # None, Get method does not raise an error!

print("\n# -----------------------------")
print("# 2. Adding, Updating, Removing")
print("# -----------------------------\n")

# Assignment creates a new key or overwrites the existing value.
person["job"] = "QA Engineer"
person["age"] = 33

# update() merges in new pairs or overwrites existing keys.
person.update({"city": "Chisinau", "age": 34})

# pop() returns and removes a key, while del just deletes it.
person.pop("city")
del person["age"]
print(person)

# popitem() removes and returns the most recently inserted pair.
last_item = person.popitem()
print("popped:", last_item)
print("after popitem:", person)

# ------------------------------------------------------------
# copy() and clear()
# ------------------------------------------------------------
# copy() makes a shallow copy; clear() removes all items.

# why use copy()?
# It creates a new dictionary with the same key-value pairs, allowing you to modify
# the copy without affecting the original dictionary.
# This is useful when you need a duplicate dictionary to work with independently.
snapshot = person.copy()
# why use clear()?
# It removes all items from the dictionary, effectively resetting it to an empty state.
# This is useful when you want to reuse the same dictionary variable without retaining
# any of its previous data.
person.clear()
print("snapshot:", snapshot)
print("cleared:", person)

print("\n# -----------------------------")
print("# 3. Looping Through a Dictionary")
print("# -----------------------------\n")

# Iterating over the dictionary gives keys; .values() and .items() expose more detail.
for key in person:
    print(key)  # keys only

for value in person.values():
    print(value)  # values only

for key, value in person.items():
    print(key, "→", value)  # key/value pairs

# values() and items() are dictionary-only; lists/tuples/sets don't have them.

# ------------------------------------------------------------
# Sorted keys/items (use case: predictable order for output)
# ------------------------------------------------------------

grades = {"Biology": 88, "Math": 95, "Art": 76}

print("\n# Sorted keys")
for subject in sorted(grades):
    print(subject, grades[subject]) # sorted keys 

print("\n# Sorted items (key-value pairs)")
for subject, score in sorted(grades.items()):
    print(subject, "→", score)

# ------------------------------------------------------------
# values() use case (summaries, thresholds)
# ------------------------------------------------------------
# Calculate average score from dictionary values.

# why use values()?
# It provides a dynamic view of the dictionary's values, which is useful for calculations
# and summaries without needing to extract them into a separate list.

scores = {"Alex": 90, "Maria": 84, "Lee": 96}
average = sum(scores.values()) / len(scores)
print("average score:", average) # 90.0



print("\n# -----------------------------")
print("# 4. Membership & Length")
print("# -----------------------------\n")

# Use `in` for membership checks, len() for how many pairs exist.
if "name" in person:
    print("Name exists!")

print(len(person))


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)


print("\n# -----------------------------")
print("# 5. keys()")
print("# -----------------------------\n")
# why use keys()?
# It provides a dynamic view of the dictionary's keys, which is useful for iteration and membership
# checks, especially when the dictionary may change during runtime.

# Example:
person = {"name": "Alex", "age": 32, "city": "Chisinau"}
print(person.keys())  # dict_keys(['name', 'age', 'city'])
# the dict_keys variable behaves like a set


print("\n# -----------------------------")
print("# 6. setdefault()")
print("# -----------------------------\n")
# why use setdefault?
# It simplifies checking for a key and inserting a default value if the key is absent.
# This is especially useful for initializing dictionary entries.

# Example:
# setdefault() gets a value or inserts a default if missing.
profile = {"name": "Maria"}
profile.setdefault("city", "Unknown")
print(profile)  # {'name': 'Maria', 'city': 'Unknown'}

# If the key exists, it returns the current value and does nothing.
profile.setdefault("name", "Other")
print(profile["name"])  # Maria
