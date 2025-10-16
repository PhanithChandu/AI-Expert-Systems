# Simple Monkey and Banana Problem

monkey = "floor"
box = "corner"
banana = "ceiling"
has_banana = False

print("Initial State:")
print("Monkey is on the", monkey)
print("Box is in the", box)
print("Banana is hanging from the", banana)
print()

# Step 1: Move box under banana
print("Monkey moves the box under the banana.")
box = "under_banana"

# Step 2: Climb on the box
print("Monkey climbs on the box.")
monkey = "on_box"

# Step 3: Take the banana
print("Monkey takes the banana!")
has_banana = True

# Final state
print("\nFinal State:")
print("Monkey is", monkey)
print("Box is", box)
print("Banana is taken:", has_banana)
