# Sample Data
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

# 1. Orange Cap winner
orange_cap = max(runs, key=runs.get)

# 2. Lowest scorer
lowest_scorer = min(runs, key=runs.get)

# 3. Total runs scored
total_runs = sum(runs.values())

# 4. Players scoring more than 500 runs
above_500 = []
for player, score in runs.items():
    if score > 500:
        above_500.append(player)

# 5. Players scoring below 400 runs
below_400 = []
for player, score in runs.items():
    if score < 400:
        below_400.append(player)

# Output
print(f"Orange Cap Winner: {orange_cap} ({runs[orange_cap]} runs)")
print(f"Lowest Scorer: {lowest_scorer} ({runs[lowest_scorer]} runs)")
print("Total Runs:", total_runs)

print("Players Scoring Above 500:")
for player in above_500:
    print(player)

print("Players Scoring Below 400:", below_400)