# Sample Data
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

# 1. Cities with temperature above 40°C
above_40 = []
for city, temp in temperature.items():
    if temp > 40:
        above_40.append(city)

# 2. Hottest city
hottest = max(temperature, key=temperature.get)

# 3. Coolest city
coolest = min(temperature, key=temperature.get)

# 4. Average temperature
average = sum(temperature.values()) / len(temperature)

# 5. Pleasant cities (<35°C)
pleasant = []
for city, temp in temperature.items():
    if temp < 35:
        pleasant.append(city)

# Output
print("Cities Above 40°C:")
for city in above_40:
    print(city)

print(f"\nHottest City: {hottest} ({temperature[hottest]}°C)")
print(f"Coolest City: {coolest} ({temperature[coolest]}°C)")
print(f"Average Temperature: {average:.1f}°C")
print("Pleasant Cities:", pleasant)