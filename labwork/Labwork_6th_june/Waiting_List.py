passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

print("Waiting List Passengers:")

for name, status in passengers:
    if status == "Waiting":
        print(name)

confirmed = 0
waiting = 0

for name, status in passengers:
    if status == "Confirmed":
        confirmed += 1
    else:
        waiting += 1

print("Confirmed:", confirmed)
print("Waiting:", waiting)

search = input("Enter Passenger Name: ")

found = False

for name, status in passengers:
    if name.lower() == search.lower() and status == "Confirmed":
        found = True
        break

if found:
    print("Confirmed Ticket Found")
else:
    print("Confirmed Ticket Not Found")

confirmed_list = []
waiting_list = []

for name, status in passengers:
    if status == "Confirmed":
        confirmed_list.append(name)
    else:
        waiting_list.append(name)

print("Confirmed Passengers:", confirmed_list)
print("Waiting Passengers:", waiting_list)