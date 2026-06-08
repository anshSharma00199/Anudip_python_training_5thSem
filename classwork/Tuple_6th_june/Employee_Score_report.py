# Employee Performance Evaluation

employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# 1. Employees scoring 80 or above
print("Employees Scoring 80 or Above:")
for emp in employees:
    if emp[2] >= 80:
        print(emp[0], emp[1], emp[2])

# 2. Count employees needing improvement
count = 0
for emp in employees:
    if emp[2] < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# 3. Find highest performer
highest = employees[0]

for emp in employees:
    if emp[2] > highest[2]:
        highest = emp

print("\nHighest Performer:")
print(highest[0], highest[1], highest[2])

# 4. List of employees scoring above 75
high_performers = []

for emp in employees:
    if emp[2] > 75:
        high_performers.append(emp[1])

print("\nHigh Performers:", high_performers)

# 5. Performance categories
print("\nPerformance Categories:")

for emp in employees:
    score = emp[2]

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)