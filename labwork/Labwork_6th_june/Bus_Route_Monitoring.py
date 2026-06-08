passengers = [12, 18, 25, 30, 28, 15, 8]

highest = max(passengers)

print("Busiest Stop:", passengers.index(highest) + 1)

print("Stops With Fewer Than 10 Passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

average = sum(passengers) / len(passengers)

print("Average Passengers:", average)

found = False

for count in passengers:
    if count > 25:
        found = True
        break

if found:
    print("A Stop Exceeded 25 Passengers")
else:
    print("No Stop Exceeded 25 Passengers")