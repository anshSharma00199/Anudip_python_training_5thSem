# Student Result Processing System

def read_students():
    students = []
    file = open("results.txt", "r")
    for line in file:
        data = line.strip().split(",")
        students.append(data)
    file.close()
    return students


def display_students():
    students = read_students()

    print("\nStudent Records")
    print("--------------------------")
    for student in students:
        print("ID:", student[0], "Name:", student[1], "Marks:", student[2])


def search_student():
    students = read_students()
    sid = input("Enter Student ID: ")

    for student in students:
        if student[0] == sid:
            print("\nStudent Found")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Marks:", student[2])
            return

    print("Student Not Found")


def topper_lowest():
    students = read_students()

    topper = students[0]
    lowest = students[0]

    for student in students:
        if int(student[2]) > int(topper[2]):
            topper = student

        if int(student[2]) < int(lowest[2]):
            lowest = student

    print("\nTopper")
    print(topper[0], topper[1], topper[2])

    print("\nLowest Scorer")
    print(lowest[0], lowest[1], lowest[2])


def class_average():
    students = read_students()
    total = 0

    for student in students:
        total += int(student[2])

    avg = total / len(students)
    print("Class Average =", avg)


def pass_fail():
    students = read_students()

    passed = 0
    failed = 0

    for student in students:
        if int(student[2]) >= 40:
            passed += 1
        else:
            failed += 1

    print("Pass Students =", passed)
    print("Fail Students =", failed)


def generate_grades():
    students = read_students()

    file = open("grades.txt", "w")

    print("\nGrade Report")

    for student in students:
        marks = int(student[2])

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "F"

        print(student[0], student[1], grade)
        file.write(student[0] + "," + student[1] + "," + grade + "\n")

    file.close()
    print("Grades saved in grades.txt")


while True:
    print("\n===== Student Result Processing System =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Topper and Lowest Scorer")
    print("4. Class Average")
    print("5. Pass and Fail Count")
    print("6. Generate Grades")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_students()

    elif choice == 2:
        search_student()

    elif choice == 3:
        topper_lowest()

    elif choice == 4:
        class_average()

    elif choice == 5:
        pass_fail()

    elif choice == 6:
        generate_grades()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")