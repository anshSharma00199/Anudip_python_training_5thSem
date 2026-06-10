performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

print("Employees Scoring Above 80:")
for i in performance:
    if performance[i] > 80:
        print(i)

improvement = 0
for i in performance:
    if performance[i] < 60:
        improvement += 1

top = max(performance, key=performance.get)

total = sum(performance.values())
average = total / len(performance)

excellent = []
good = []
average_list = []
poor = []

for i in performance:
    if performance[i] >= 90:
        excellent.append(i)
    elif performance[i] >= 75:
        good.append(i)
    elif performance[i] >= 60:
        average_list.append(i)
    else:
        poor.append(i)

print("Top Performer:", top, "(", performance[top], ")")
print("Employees Needing Improvement:", improvement)
print("Average Score:", round(average, 1))
print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_list)
print("Poor:", poor)