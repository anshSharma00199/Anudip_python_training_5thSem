# Employee Payroll Management System

def read_employees():
    employees = []
    file = open("employees.txt", "r")
    for line in file:
        data = line.strip().split(",")
        employees.append(data)
    file.close()
    return employees


def write_employees(employees):
    file = open("employees.txt", "w")
    for emp in employees:
        file.write(emp[0] + "," + emp[1] + "," + str(emp[2]) + "\n")
    file.close()


def display_employees():
    employees = read_employees()
    print("\nEmployee Records")
    print("-------------------------")
    for emp in employees:
        print("ID:", emp[0], "Name:", emp[1], "Salary:", emp[2])


def search_employee():
    employees = read_employees()
    eid = input("Enter Employee ID: ")

    for emp in employees:
        if emp[0] == eid:
            print("\nEmployee Found")
            print("ID:", emp[0])
            print("Name:", emp[1])
            print("Salary:", emp[2])
            return

    print("Employee Not Found")


def average_salary():
    employees = read_employees()
    total = 0

    for emp in employees:
        total += int(emp[2])

    avg = total / len(employees)
    print("Average Salary =", avg)


def highest_lowest_salary():
    employees = read_employees()

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:
        if int(emp[2]) > int(highest[2]):
            highest = emp

        if int(emp[2]) < int(lowest[2]):
            lowest = emp

    print("\nHighest Paid Employee")
    print(highest[0], highest[1], highest[2])

    print("\nLowest Paid Employee")
    print(lowest[0], lowest[1], lowest[2])


def salary_above_50000():
    employees = read_employees()

    print("\nEmployees earning above 50000")
    for emp in employees:
        if int(emp[2]) > 50000:
            print(emp[0], emp[1], emp[2])


def add_employee():
    employees = read_employees()

    eid = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    employees.append([eid, name, salary])

    write_employees(employees)

    print("Employee Added Successfully")


def salary_category():
    employees = read_employees()

    print("\nSalary Categories")
    for emp in employees:
        salary = int(emp[2])

        if salary >= 60000:
            category = "High"
        elif salary >= 40000:
            category = "Medium"
        else:
            category = "Low"

        print(emp[0], emp[1], ":", category)


while True:
    print("\n===== Employee Payroll Management System =====")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Calculate Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Display Employees Above 50000")
    print("6. Add New Employee")
    print("7. Generate Salary Categories")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_employees()

    elif choice == 2:
        search_employee()

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest_salary()

    elif choice == 5:
        salary_above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_category()

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")