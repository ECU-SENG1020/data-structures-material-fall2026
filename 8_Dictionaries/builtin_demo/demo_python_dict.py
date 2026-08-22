"""
Python Dictionary Demonstration
A concise guide to Python's built-in dict data structure
"""

# ============================================================================
# 1. CREATING DICTIONARIES
# ============================================================================
empty = {}
print("Empty dict:", empty)

profile = {"name": "Ada", "role": "Engineer", "name": "Ada Lovelace"}
print("Profile (duplicate key overwritten):", profile)

pairs = [("a", 1), ("b", 2), ("c", 3)]
from_pairs = dict(pairs)
print("From pairs:", from_pairs)

print("\n" + "=" * 60 + "\n")

# ============================================================================
# 2. ADDING, UPDATING, REMOVING
# ============================================================================
scores = {"alice": 90, "bob": 82}
print("Original:", scores)

scores["carol"] = 95
print("After add carol:", scores)

scores["alice"] = 93
print("After update alice:", scores)

# removed = scores.pop("brian")
# print("Popped bob:", removed, "Remaining:", scores)

removed = scores.pop("bob")
print("Popped bob:", removed, "Remaining:", scores)

missing = scores.pop("missing", "n/a")
print("Pop missing with default:", missing)

del scores["carol"]
print("After del carol:", scores)

scores.clear()
print("After clear():", scores)

print("\n" + "=" * 60 + "\n")

# ============================================================================
# 3. MEMBERSHIP, LOOKUP, ITERATION
# ============================================================================
inventory = {"pen": 10, "notebook": 5, "eraser": 2}
print("Inventory:", inventory)
print("Is 'pen' a key?", "pen" in inventory)
print("Quantity for marker (safe):", inventory.get("marker", 0))

print("Keys:")
for k in inventory:
    print(" ", k)

print("Keys:")
for k in inventory.keys():
    print(" ", k)

print("Values:")
for v in inventory.values():
    print(" ", v)

print("Items:")
for k, v in inventory.items():
    print(" ", k, "->", v)

print("Items:")
for item in inventory.items():
    print(item, type(item))
    print("key: ", item[0])
    print("value: ", item[1])


print("\n" + "=" * 60 + "\n")

# ============================================================================
# 4. MERGE / COPY / COMPREHENSIONS
# ============================================================================
base = {"x": 1, "y": 2}
extra = {"y": 20, "z": 3}

merged = base | extra
print("Merged (base | extra):", merged)

copied = dict(merged)
copied.update({"w": 0})
print("Copied then update:", copied)

squares = {n: n * n for n in range(6)}
print("Squares dict:", squares)

print("\n" + "=" * 60 + "\n")

# ============================================================================
# 5. KEY TYPE NOTES
# ============================================================================
coords = {(0, 0): "origin", (1, 2): "point"}
print("Tuple keys are valid:", coords)

try:
    bad = {[1, 2]: "not allowed"}
    print(bad)
except TypeError as e:
    print("List keys are invalid (unhashable):", e)

print("\nDictionary demo complete (Python).")
