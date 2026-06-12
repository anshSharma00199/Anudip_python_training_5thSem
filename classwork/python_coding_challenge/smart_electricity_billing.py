#consumption of electricity in units
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
    "House110": 600,
}

#The houses consuming more than 400 units.  
houses_above_400 = [
    house for house, consumption in units.items() 
    if consumption > 400
]

#highest-consuming house. 
highest_house = max(units, key=units.get)

#lowest-consuming house. 
lowest_house = min(units, key=units.get)

# total units consumed.  
total_units = sum(units.values())

#Low Consumption (< 200)  
low_consumption = [
    house for house, consumption in units.items() 
    if consumption < 200
]

#Medium Consumption (200–400)  
medium_consumption = [
    house for house, consumption in units.items() 
    if 200 <= consumption <= 400
]

#High Consumption (> 400)  
high_consumption = [
    house for house, consumption in units.items() 
    if consumption > 400
]

#Count houses eligible for an energy-saving campaign (consumption > 300).  S
eligible_count = sum(consumption > 300 for consumption in units.values())

print("Houses Consuming More Than 400 Units:")
for house in houses_above_400:
    print(house)

print(f"\nHighest Consumption: {highest_house} ({units[highest_house]} units)")
print(f"Lowest Consumption: {lowest_house} ({units[lowest_house]} units)")
print(f"Total Units Consumed: {total_units}")
print(f"\nLow Consumption: {low_consumption}")
print(f"Medium Consumption: {medium_consumption}")
print(f"High Consumption: {high_consumption}")
print(f"\nEligible for Energy-Saving Campaign: {eligible_count}")

