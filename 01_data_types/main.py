# -------------------------------
# Immutable Example (int type)
# -------------------------------

# Integers are immutable in Python. This means their value cannot be changed
# in-place. Any update to a variable holding an int will create a new object.

sugar_amount = 3
print(f"Initial Sugar: {sugar_amount}")  # prints 3

# Reassigning 'sugar_amount' to 12 creates a NEW integer object (12)
# and updates the variable 'sugar_amount' to reference this new object.
sugar_amount = 12
print(f"Second Initial Sugar: {sugar_amount}")  # prints 12

# To confirm immutability, we check the memory IDs of different integers.
# Notice that integers 2 and 12 have different IDs (different objects in memory).
print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")


# -------------------------------
# Mutable Example (set type)
# -------------------------------

# Sets are mutable in Python. This means their content can be changed in-place
# without creating a new object in memory.

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")  # prints object ID
print(f"Initial spice mix: {spice_mix}")  # prints empty set

# Adding elements modifies the same set object in-place.
spice_mix.add("one")
spice_mix.add("two")

# The contents of the set have changed, but its ID remains the same.
print(f"After spice mix: {spice_mix}")  
print(f"after spice mix id: {id(spice_mix)}")  # same as initial ID
