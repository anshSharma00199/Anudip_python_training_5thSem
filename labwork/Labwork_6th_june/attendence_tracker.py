attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = attendance.count('P')
absent = attendance.count('A')

print("Present Days:", present)
print("Absent Days:", absent)

percentage = (present / len(attendance)) * 100

print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

print("Absent Positions:")
for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)