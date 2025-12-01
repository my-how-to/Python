# ===========================================
#            LESSON 5 — DICTIONARIES (COLLECTIONS)
# ===========================================
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
# ============================================================
# 1) Dictionaries — Mapped Data
# ============================================================

person = {
    "name": "Alex",
    "age": 32,
    "city": "Chisinau",
}

# ------------------------------------------------------------
# Accessing values by key
# ------------------------------------------------------------
print(person["name"])  # Alex
print(person["age"])   # 32

# ------------------------------------------------------------
# Safe access
# ------------------------------------------------------------
print(person.get("country", "Not specified"))

# ============================================================
# 2) Adding, Updating, and Removing
# ============================================================

# ------------------------------------------------------------
# Adding / updating values
# ------------------------------------------------------------
person["job"] = "QA Engineer"
person["age"] = 33

# ------------------------------------------------------------
# Removing entries
# ------------------------------------------------------------
person.pop("city")
del person["age"]
print(person)

# ============================================================
# 3) Looping Through a Dictionary
# ============================================================

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, "→", value)

# ============================================================
# 4) Checking Membership & Length
# ============================================================

if "name" in person:
    print("Name exists!")

print(len(person))
