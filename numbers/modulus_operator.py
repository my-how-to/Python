# ============================================================
#            LESSON — MASTERING THE MODULUS OPERATOR
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   A focused walkthrough of Python's modulus operator (%) that
#   clarifies remainders, range wrapping, and why % often beats
#   manual conditional logic when enforcing limits or cycles.
#
# Contents:
#   1. What modulus means
#   2. Visualizing remainders
#   3. Keeping values within a range
#   4. Cycles, wrap-around, and scheduling
#   5. Why % is preferred over conditionals
#   6. Practice mini-exercises
#
# ============================================================

print("\n# -----------------------------")
print("# 1. WHAT MODULUS MEANS")
print("# -----------------------------\n")

# % returns the remainder of integer division. (the value left over after dividing one value by another)
segments = 17 % 5
print("17 % 5 =", segments)  # 5 fits 3 times with 2 leftover

# Rule: a % b returns a itself when a < b.
small = 3 % 10
print("3 % 10 (a < b) =", small) # 3 % 10 (a < b) = 3

# Rule: Reapplying % with unchanged values gives the same result.
first_pass = 42 % 10
second_pass = first_pass % 10
print("42 % 10 =", first_pass, "| applying % again ->", second_pass)

# The modulus operator exists to keep numbers within a fixed range 
# by returning what remains after division, enabling cycles, limits, and wrap-around logic.

# The modulus operator answers one question: “What is left after dividing by N?”
# When dividing by 4, the possible remainders are only: 0, 1, 2, 3 
# There are no other possibilities.
for i in range(20):
    print(f"i: {i}, i % 4: {i % 4}")


print("\n# -----------------------------")
print("# 2. VISUALIZING REMAINDERS")
print("# -----------------------------\n")

total_people = 23
car_capacity = 4
full_cars = total_people // car_capacity    # how many full cars
stragglers = total_people % car_capacity    # people left without a full car

print("Full cars:", full_cars)          # Full cars: 5  
print("People waiting:", stragglers)    # People waiting: 3

# Another way to see % is as "distance to the next multiple".
number = 28
step = 6
distance_to_next_multiple = (-number) % step  # how far until 30?
print("Next multiple distance:", distance_to_next_multiple) # Next multiple distance: 4


print("\n# -----------------------------")
print("# 3. KEEPING VALUES WITHIN A RANGE")
print("# -----------------------------\n")

# Example: Keep a score between 0-9 by wrapping every 10 points.
score = 0
for gained in [3, 4, 9, 2]:
    score = (score + gained) % 10
    print("Score after gaining", gained, "->", score)

# Example: Use % to select palette colors without exceeding list length.
colors = ["red", "green", "blue"]
for i in range(8):
    palette_index = i % len(colors)
    print(f"Brush {i}: {colors[palette_index]}")


print("\n# -----------------------------")
print("# 4. CYCLES, WRAP-AROUND, AND SCHEDULING")
print("# -----------------------------\n")

# Classic clock wrap: keep hours on a 12-hour clock.
hour = 10
for jump in [3, 4, 9]:
    hour = (hour + jump) % 12 or 12
    print("New clock hour:", hour)

# Scheduling: assign weekly tasks even if the counter grows large.
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
task_counter = 0

for task in ["deploy", "sync", "report", "plan", "review", "pair", "demo"]:
    day = weekdays[task_counter % len(weekdays)]
    print(day, "->", task)
    task_counter += 1


print("\n# -----------------------------")
print("# 5. WHY % BEATS CONDITIONALS")
print("# -----------------------------\n")

# Without %, wrap-around logic becomes a pile of branching rules.
def wrap_without_mod(position, limit):
    if position < 0:
        return limit + position
    if position >= limit:
        return position - limit
    return position

def wrap_with_mod(position, limit):
    return position % limit

tests = [-2, -1, 0, 1, limit := 5, 6, 12]

for value in tests:
    manual = wrap_without_mod(value, limit)
    modded = wrap_with_mod(value, limit)
    print(f"value={value:>3} -> manual:{manual}, mod:{modded}")

# Reasons % is preferred:
#   * It scales: works for any integer range or list length without new branches.
#   * It is declarative: "% limit" clearly signals wrap-around intent.
#   * It eliminates edge-case bugs from missing or duplicated conditional paths.


print("\n# -----------------------------")
print("# 6. PRACTICE MINI-EXERCISES")
print("# -----------------------------\n")

# Exercise 1: Bounce a character index inside an alphabet string.
alphabet = "abcdefghijklmnopqrstuvwxyz"

for shift in range(20):
    idx = shift % len(alphabet)
    print(f"Shift {shift:2} -> {alphabet[idx]}")

# Exercise 2: Simulate traffic light changes
lights = ["green", "yellow", "red"]

for second in range(9):
    light = lights[second % len(lights)]
    print(f"Second {second}: {light}")

# Exercise 3: Verify % equivalence with repeated subtraction for positive integers.
dividend, divisor = 29, 8
remainder = dividend
while remainder >= divisor:
    remainder -= divisor
print(f"{dividend} % {divisor} via subtraction -> {remainder}")
