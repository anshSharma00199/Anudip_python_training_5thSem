vehicle = "MH12AB4589"

print("Vehicle Number:", vehicle)

# Extract parts
state = vehicle[:2]
district = vehicle[2:4]
series = vehicle[4:6]
number = vehicle[6:]

print("State Code:", state)
print("District Code:", district)
print("Series:", series)
print("Vehicle Number:", number)

# Count letters and digits
letters = 0
digits = 0

for ch in vehicle:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("\nTotal Letters:", letters)
print("Total Digits:", digits)

# Verify number plate
if (vehicle[:2].isalpha() and
    vehicle[2:4].isdigit() and
    vehicle[4:6].isalpha() and
    vehicle[6:].isdigit() and
    len(vehicle) == 10):
    print("\nVehicle Number Status: Valid")
else:
    print("\nVehicle Number Status: Invalid")