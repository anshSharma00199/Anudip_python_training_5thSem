FILE_NAME = "employees.txt"


def read_employees():
    """Read employee records from the file and return a list of dictionaries."""
    employees = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                fields = line.strip().split(",")

                if len(fields) == 3:
                    employee_id, name, salary_text = fields
                    try:
                        employees.append(
                            {
                                "id": employee_id,
                                "name": name,
                                "salary": int(salary_text),
                            }
                        )
                    except ValueError:
                        print("Skipped a record with an invalid salary:", line.strip())
    except FileNotFoundError:
        open(FILE_NAME, "w").close()

    return employees


def display_employee(employee):
    print(
        f"Employee ID: {employee['id']}, "
        f"Name: {employee['name']}, "
        f"Salary: Rs. {employee['salary']:,}"
    )


def display_all_employees():
    employees = read_employees()

    if not employees:
        print("No employee records found.")
        return

    print("\n--- All Employee Records ---")
    for employee in employees:
        display_employee(employee)


def search_employee():
    employee_id = input("Enter Employee ID: ").strip().upper()
    employees = read_employees()

    for employee in employees:
        if employee["id"].upper() == employee_id:
            print("\nEmployee found:")
            display_employee(employee)
            return

    print("Employee ID not found.")


def calculate_average_salary():
    employees = read_employees()

    if not employees:
        print("No employee records found.")
        return

    total_salary = sum(employee["salary"] for employee in employees)
    average_salary = total_salary / len(employees)
    print(f"Average salary: Rs. {average_salary:,.2f}")


def display_salary_extremes():
    employees = read_employees()

    if not employees:
        print("No employee records found.")
        return

    highest_paid = max(employees, key=lambda employee: employee["salary"])
    lowest_paid = min(employees, key=lambda employee: employee["salary"])

    print("\nHighest-paid employee:")
    display_employee(highest_paid)
    print("\nLowest-paid employee:")
    display_employee(lowest_paid)


def display_above_50000():
    employees = read_employees()
    matching_employees = [
        employee for employee in employees if employee["salary"] > 50000
    ]

    if not matching_employees:
        print("No employees earn above Rs. 50,000.")
        return

    print("\n--- Employees Earning Above Rs. 50,000 ---")
    for employee in matching_employees:
        display_employee(employee)


def add_employee():
    employees = read_employees()
    employee_id = input("Enter Employee ID: ").strip().upper()

    if not employee_id:
        print("Employee ID cannot be empty.")
        return

    if any(employee["id"].upper() == employee_id for employee in employees):
        print("An employee with this ID already exists.")
        return

    name = input("Enter employee name: ").strip()
    if not name or "," in name:
        print("Enter a valid name without commas.")
        return

    try:
        salary = int(input("Enter salary: ").strip())
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Salary must be a whole number.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{employee_id},{name},{salary}\n")

    print("Employee record added successfully.")


def display_salary_categories():
    employees = read_employees()
    categories = {"High": [], "Medium": [], "Low": []}

    for employee in employees:
        if employee["salary"] >= 60000:
            categories["High"].append(employee)
        elif employee["salary"] >= 40000:
            categories["Medium"].append(employee)
        else:
            categories["Low"].append(employee)

    if not employees:
        print("No employee records found.")
        return

    for category, category_employees in categories.items():
        print(f"\n--- {category} Salary Category ---")
        if category_employees:
            for employee in category_employees:
                display_employee(employee)
        else:
            print("No employees in this category.")


def display_menu():
    print("\n===== Employee Payroll Management System =====")
    print("1. Display all employee records")
    print("2. Search employee using Employee ID")
    print("3. Calculate average salary")
    print("4. Find highest-paid and lowest-paid employee")
    print("5. Display employees earning above Rs. 50,000")
    print("6. Add a new employee record")
    print("7. Display salary categories")
    print("8. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            display_all_employees()
        elif choice == "2":
            search_employee()
        elif choice == "3":
            calculate_average_salary()
        elif choice == "4":
            display_salary_extremes()
        elif choice == "5":
            display_above_50000()
        elif choice == "6":
            add_employee()
        elif choice == "7":
            display_salary_categories()
        elif choice == "8":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
