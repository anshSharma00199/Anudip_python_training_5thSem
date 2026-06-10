attendance = "PPAPPPAAPPPPAPP"

print("Attendance Record:", attendance)

present = attendance.count("P")
absent = attendance.count("A")

print("Present Days:", present)
print("Absent Days:", absent)

percentage = (present / len(attendance)) * 100
print("Attendance Percentage:", round(percentage, 2), "%")

# Longest present streak
max_p = 0
count = 0

for ch in attendance:
    if ch == "P":
        count += 1
        if count > max_p:
            max_p = count
    else:
        count = 0

# Longest absent streak
max_a = 0
count = 0

for ch in attendance:
    if ch == "A":
        count += 1
        if count > max_a:
            max_a = count
    else:
        count = 0

print("Longest Present Streak:", max_p)
print("Longest Absent Streak:", max_a)

if percentage < 75:
    print("Attendance Status: Below 75%")
else:
    print("Attendance Status: Above 75%")