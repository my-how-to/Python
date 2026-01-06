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
# Contents:
#   1. Dictionaries — Mapped Data
#   2. Adding, Updating, and Removing
#   3. Looping Through a Dictionary
#   4. Checking Membership & Length
#
print("\n# -----------------------------")
print("# 1. Dictionaries — Mapped Data")
print("# -----------------------------\n")

empty_dict = {}
print("empty dict literal:", empty_dict, type(empty_dict))

person = {
    "name": "Alex",
    "age": 32,
    "city": "Chisinau",
}

# Each key is a unique label → use it to access the stored value.
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

# pop() returns and removes a key, while del just deletes it.
person.pop("city")
del person["age"]
print(person)

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

print("\n# -----------------------------")
print("# 4. Membership & Length")
print("# -----------------------------\n")

# Use `in` for membership checks, len() for how many pairs exist.
if "name" in person:
    print("Name exists!")

print(len(person))
