#input the score of the 11 players and print their score

# player score list
player_score = []

# input score from user
for i in range(1,11):
    score = int(input(f"Enter the score of player{i}: "))
    player_score.append(score)

# print the scores
print("\n.........PLAYER SCORES..........")
print("Scores of 11 players are:", player_score)

# finding highest score
max_score = player_score[0]

for index in range(1, len(player_score)):
    if player_score[index] > max_score:
        max_score = player_score[index]

print("Highest Score =", max_score)

