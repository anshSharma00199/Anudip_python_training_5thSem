employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

print("Employees Earning Above ₹50000:")
for name, salary in employees:
    if salary > 50000:
        print(name, salary)

highest = employees[0]

for emp in employees:
    if emp[1] > highest[1]:
        highest = emp

print("Highest Paid Employee:", highest)

total = 0
count = 0

for name, salary in employees:
    total += salary
    if salary < 40000:
        count += 1

print("Total Salary Expenditure:", total)
print("Employees Earning Below ₹40000:", count)