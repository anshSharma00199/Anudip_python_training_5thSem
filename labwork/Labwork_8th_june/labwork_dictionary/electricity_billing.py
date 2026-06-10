units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

print("Houses Consuming More Than 400 Units:")
for i in units:
    if units[i] > 400:
        print(i)

highest = max(units, key=units.get)
lowest = min(units, key=units.get)

total = sum(units.values())

low = []
medium = []
high = []

campaign = 0

for i in units:
    if units[i] < 200:
        low.append(i)
    elif units[i] <= 400:
        medium.append(i)
    else:
        high.append(i)

    if units[i] > 300:
        campaign += 1

print("Highest Consumption:", highest, "(", units[highest], "units )")
print("Lowest Consumption:", lowest, "(", units[lowest], "units )")
print("Total Units Consumed:", total)
print("Low Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)
print("Eligible for Energy-Saving Campaign:", campaign)