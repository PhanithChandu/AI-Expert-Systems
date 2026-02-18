# Vacuum Cleaner Problem

# Taking input
room_A = input("Enter status of Room A (Clean/Dirty): ").strip().lower()
room_B = input("Enter status of Room B (Clean/Dirty): ").strip().lower()
location = input("Enter vacuum location (A/B): ").strip().upper()

rooms = {"A": room_A, "B": room_B}

# Cleaning process
for _ in range(2):
    if rooms[location] == "dirty":
        print("Cleaning Room", location)
        rooms[location] = "clean"
    else:
        print("Room", location, "is already clean")

    # Move to other room
    location = "B" if location == "A" else "A"

print("\nFinal Status:")
print("Room A:", rooms["A"])
print("Room B:", rooms["B"])
