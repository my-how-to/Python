# ===========================================
#   PYTHON LESSON — DICTIONARIES (COLLECTIONS)
# ===========================================

# A dictionary stores key-value pairs.
# Each key must be unique, and it points to a specific value — 
# like a real-world dictionary maps a word to its definition.

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
