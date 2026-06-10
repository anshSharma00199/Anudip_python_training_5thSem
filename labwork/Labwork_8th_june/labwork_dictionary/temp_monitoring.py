temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

print("Cities Above 40°C:")
for i in temperature:
    if temperature[i] > 40:
        print(i)

hot = max(temperature, key=temperature.get)
cool = min(temperature, key=temperature.get)

avg = sum(temperature.values()) / len(temperature)

pleasant = []
count = 0

for i in temperature:
    if temperature[i] < 35:
        pleasant.append(i)
    if 35 <= temperature[i] <= 40:
        count += 1

print("Hottest City:", hot, "(", temperature[hot], "°C )")
print("Coolest City:", cool, "(", temperature[cool], "°C )")
print("Average Temperature:", round(avg, 1), "°C")
print("Pleasant Cities:", pleasant)
print("Cities Between 35°C and 40°C:", count)