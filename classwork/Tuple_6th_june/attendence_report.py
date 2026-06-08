attendance = {}

for i in range(1, 31):
    roll_no = input("Enter Roll Number: ")
    status = input("Enter Attendance (Present/Absent): ")

    attendance[roll_no] = status

print("\nStudents Present:")

for roll_no, status in attendance.items():
    if status.lower() == "present":
        print(roll_no)