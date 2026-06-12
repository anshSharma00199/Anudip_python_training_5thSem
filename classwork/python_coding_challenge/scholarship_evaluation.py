# Sample data of students and their marks
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90,
}

# Students scoring above 85 marks
students_above_85 = [
    student for student, score in marks.items() 
    if score > 85
]

# Highest and lowest scorers
topper = max(marks, key=marks.get)
lowest_scorer = min(marks, key=marks.get)

# Class average
average_marks = sum(marks.values()) / len(marks)

# Grade for each student
grades = {}
for student, score in marks.items():
    if score >= 90:
        grades[student] = "A"
    elif score >= 75:
        grades[student] = "B"
    elif score >= 50:
        grades[student] = "C"
    else:
        grades[student] = "F"

# Students eligible for a scholarship
scholarship_students = [
    student for student, score in marks.items() 
    if score >= 90
]

print("Students Scoring Above 85:")
for student in students_above_85:
    print(student)

print(f"\nTopper: {topper} ({marks[topper]})")
print(f"Lowest Scorer: {lowest_scorer} ({marks[lowest_scorer]})")
print(f"Average Marks: {average_marks:.1f}")

print("\nStudent Grades:")
for student, grade in grades.items():
    print(f"{student}: {grade}")

print(f"\nScholarship Students: {scholarship_students}")
