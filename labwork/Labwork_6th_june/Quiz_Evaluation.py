correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

score = 0
wrong = []

for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong.append(i + 1)

print("Score:", score)

print("Incorrect Questions:", wrong)

correct_count = score
wrong_count = len(correct) - score

print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)

percentage = (score / len(correct)) * 100

if percentage >= 60:
    print("Pass")
else:
    print("Fail")