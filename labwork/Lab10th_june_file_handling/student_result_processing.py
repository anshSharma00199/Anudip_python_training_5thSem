# File names used by the program
RESULTS_FILE = "results.txt"
GRADES_FILE = "grades.txt"


def read_students():
    """Read student records and return them as a list of dictionaries."""
    students = []

    try:
        with open(RESULTS_FILE, "r") as file:
            for line in file:
                fields = line.strip().split(",")

                # A valid record must contain ID, name, and marks.
                if len(fields) == 3:
                    student_id, name, marks_text = fields
                    try:
                        marks = int(marks_text)
                        if 0 <= marks <= 100:
                            students.append(
                                {
                                    "id": student_id,
                                    "name": name,
                                    "marks": marks,
                                }
                            )
                        else:
                            print("Skipped record with marks outside 0-100:", line.strip())
                    except ValueError:
                        print("Skipped record with invalid marks:", line.strip())
    except FileNotFoundError:
        # Create an empty file if results.txt does not exist.
        open(RESULTS_FILE, "w").close()

    return students


def calculate_grade(marks):
    """Return the grade for the given marks."""
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 40:
        return "C"
    return "F"


def display_student(student):
    """Display one student record in a readable format."""
    print(
        f"Student ID: {student['id']}, "
        f"Name: {student['name']}, "
        f"Marks: {student['marks']}"
    )


def display_all_students():
    """Display every record stored in results.txt."""
    students = read_students()

    if not students:
        print("No student records found.")
        return

    print("\n--- All Student Records ---")
    for student in students:
        display_student(student)


def search_student():
    """Search for a student by Student ID."""
    student_id = input("Enter Student ID: ").strip().upper()

    for student in read_students():
        if student["id"].upper() == student_id:
            print("\nStudent found:")
            display_student(student)
            return

    print("Student ID not found.")


def display_score_extremes():
    """Display the topper and the student with the lowest marks."""
    students = read_students()

    if not students:
        print("No student records found.")
        return

    # max() and min() compare records using the marks field.
    topper = max(students, key=lambda student: student["marks"])
    lowest_scorer = min(students, key=lambda student: student["marks"])

    print("\nTopper:")
    display_student(topper)
    print("\nLowest scorer:")
    display_student(lowest_scorer)


def calculate_class_average():
    """Calculate and display the average marks of the class."""
    students = read_students()

    if not students:
        print("No student records found.")
        return

    total_marks = sum(student["marks"] for student in students)
    average = total_marks / len(students)
    print(f"Class average: {average:.2f}")


def count_pass_and_fail():
    """Count students with passing and failing marks."""
    students = read_students()

    if not students:
        print("No student records found.")
        return

    # Students scoring 40 or more are considered passed.
    pass_count = sum(1 for student in students if student["marks"] >= 40)
    fail_count = len(students) - pass_count

    print(f"Pass students: {pass_count}")
    print(f"Fail students: {fail_count}")


def display_grades():
    """Display each student's grade on the screen."""
    students = read_students()

    if not students:
        print("No student records found.")
        return

    print("\n--- Student Grades ---")
    for student in students:
        grade = calculate_grade(student["marks"])
        print(
            f"Student ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}, Grade: {grade}"
        )


def write_grade_report():
    """Write all student grades into grades.txt."""
    students = read_students()

    if not students:
        print("No student records found. Grade report was not created.")
        return

    # Write mode replaces an older report with the latest student data.
    with open(GRADES_FILE, "w") as file:
        for student in students:
            grade = calculate_grade(student["marks"])
            file.write(
                f"{student['id']},{student['name']},"
                f"{student['marks']},{grade}\n"
            )

    print(f"Grade report written successfully to {GRADES_FILE}.")


def display_menu():
    """Display the available menu choices."""
    print("\n===== Student Result Processing System =====")
    print("1. Display all student records")
    print("2. Search a student using Student ID")
    print("3. Find topper and lowest scorer")
    print("4. Calculate class average")
    print("5. Count pass and fail students")
    print("6. Display grades")
    print("7. Write grade report to grades.txt")
    print("8. Exit")


def main():
    """Run the menu repeatedly until the user chooses Exit."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            display_all_students()
        elif choice == "2":
            search_student()
        elif choice == "3":
            display_score_extremes()
        elif choice == "4":
            calculate_class_average()
        elif choice == "5":
            count_pass_and_fail()
        elif choice == "6":
            display_grades()
        elif choice == "7":
            write_grade_report()
        elif choice == "8":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


# Start the program only when this file is run directly.
if __name__ == "__main__":
    main()
