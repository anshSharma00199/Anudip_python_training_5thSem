runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

print("Players Scoring More Than 500 Runs:")
for i in runs:
    if runs[i] > 500:
        print(i)

orange = max(runs, key=runs.get)
lowest = min(runs, key=runs.get)

total = sum(runs.values())

below400 = []
count = 0

for i in runs:
    if runs[i] < 400:
        below400.append(i)
    if 400 <= runs[i] <= 600:
        count += 1

print("Orange Cap Winner:", orange, "(", runs[orange], ")")
print("Lowest Scorer:", lowest, "(", runs[lowest], ")")
print("Total Tournament Runs:", total)
print("Players Scoring Below 400:", below400)
print("Players Between 400 and 600 Runs:", count)