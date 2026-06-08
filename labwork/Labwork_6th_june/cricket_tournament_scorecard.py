scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Count half-centuries and centuries
half_centuries = 0
centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Half-Centuries:", half_centuries)
print("Centuries:", centuries)

# Find highest score
highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print("Highest Score:", highest)

# Display scores below 20
print("Scores Below 20:")
for score in scores:
    if score < 20:
        print(score)

# Calculate average score
total = 0

for score in scores:
    total += score

average = total / len(scores)

print("Average Score:", average)