# File names used by the expense tracker
EXPENSES_FILE = "expenses.txt"
REPORT_FILE = "report.txt"


def read_expenses():
    """Read expense records and return a list of dictionaries."""
    expenses = []

    try:
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                fields = line.strip().split(",")

                # A valid record contains a category and an amount.
                if len(fields) == 2:
                    category, amount_text = fields
                    try:
                        amount = int(amount_text)
                        if amount >= 0:
                            expenses.append(
                                {"category": category, "amount": amount}
                            )
                        else:
                            print("Skipped record with a negative amount:", line.strip())
                    except ValueError:
                        print("Skipped record with an invalid amount:", line.strip())
    except FileNotFoundError:
        # Create an empty data file if expenses.txt is missing.
        open(EXPENSES_FILE, "w").close()

    return expenses


def write_expenses(expenses):
    """Save all expense records back to the original file."""
    with open(EXPENSES_FILE, "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")


def find_expense(expenses, category):
    """Find an expense category without considering letter case."""
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            return expense
    return None


def display_expense(expense):
    """Display one expense record."""
    print(
        f"Category: {expense['category']}, "
        f"Amount: Rs. {expense['amount']:,}"
    )


def display_all_expenses():
    """Display every expense stored in expenses.txt."""
    expenses = read_expenses()

    if not expenses:
        print("No expense records found.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        display_expense(expense)


def calculate_total(expenses):
    """Return the total amount spent."""
    return sum(expense["amount"] for expense in expenses)


def display_total_expenditure():
    """Calculate and display total expenditure."""
    expenses = read_expenses()

    if not expenses:
        print("No expense records found.")
        return

    print(f"Total expenditure: Rs. {calculate_total(expenses):,}")


def get_expense_extremes(expenses):
    """Return the highest and lowest expense records."""
    highest = max(expenses, key=lambda expense: expense["amount"])
    lowest = min(expenses, key=lambda expense: expense["amount"])
    return highest, lowest


def display_expense_extremes():
    """Display categories with the highest and lowest spending."""
    expenses = read_expenses()

    if not expenses:
        print("No expense records found.")
        return

    highest, lowest = get_expense_extremes(expenses)

    print("\nHighest expense category:")
    display_expense(highest)
    print("\nLowest expense category:")
    display_expense(lowest)


def get_expenses_above_800(expenses):
    """Return all categories whose spending is greater than Rs. 800."""
    return [expense for expense in expenses if expense["amount"] > 800]


def display_expenses_above_800():
    """Display expenses greater than Rs. 800."""
    matching_expenses = get_expenses_above_800(read_expenses())

    if not matching_expenses:
        print("No expenses are greater than Rs. 800.")
        return

    print("\n--- Expenses Greater Than Rs. 800 ---")
    for expense in matching_expenses:
        display_expense(expense)


def add_expense():
    """Add a new expense category and save it immediately."""
    expenses = read_expenses()
    category = input("Enter new expense category: ").strip()

    if not category or "," in category:
        print("Enter a valid category without commas.")
        return

    if find_expense(expenses, category):
        print("This expense category already exists.")
        return

    try:
        amount = int(input("Enter expense amount: ").strip())
        if amount < 0:
            print("Expense amount cannot be negative.")
            return
    except ValueError:
        print("Expense amount must be a whole number.")
        return

    expenses.append({"category": category, "amount": amount})
    write_expenses(expenses)
    print("Expense category added successfully.")


def update_expense():
    """Update an existing expense amount and save the change."""
    expenses = read_expenses()
    category = input("Enter expense category to update: ").strip()
    expense = find_expense(expenses, category)

    if not expense:
        print("Expense category not found.")
        return

    try:
        new_amount = int(input("Enter the new expense amount: ").strip())
        if new_amount < 0:
            print("Expense amount cannot be negative.")
            return
    except ValueError:
        print("Expense amount must be a whole number.")
        return

    expense["amount"] = new_amount
    write_expenses(expenses)
    print("Expense amount updated successfully.")


def generate_summary_report():
    """Generate report.txt using the latest expense information."""
    expenses = read_expenses()

    if not expenses:
        print("No expense records found. Report was not generated.")
        return

    total = calculate_total(expenses)
    highest, lowest = get_expense_extremes(expenses)
    above_800 = get_expenses_above_800(expenses)

    # Write mode creates a fresh summary containing current values.
    with open(REPORT_FILE, "w") as file:
        file.write("DAILY EXPENSE SUMMARY REPORT\n")
        file.write("=" * 30 + "\n")
        file.write(f"Total Expenses: Rs. {total:,}\n")
        file.write(
            f"Highest Expense Category: {highest['category']} "
            f"(Rs. {highest['amount']:,})\n"
        )
        file.write(
            f"Lowest Expense Category: {lowest['category']} "
            f"(Rs. {lowest['amount']:,})\n"
        )
        file.write("\nCategories Spending More Than Rs. 800:\n")

        if above_800:
            for expense in above_800:
                file.write(
                    f"- {expense['category']}: Rs. {expense['amount']:,}\n"
                )
        else:
            file.write("- None\n")

    print(f"Summary report generated successfully in {REPORT_FILE}.")


def display_menu():
    """Display all available menu options."""
    print("\n===== Daily Expense Tracker and Report Generator =====")
    print("1. Display all expenses")
    print("2. Calculate total expenditure")
    print("3. Find highest and lowest spending categories")
    print("4. Display expenses greater than Rs. 800")
    print("5. Add a new expense category")
    print("6. Update an existing expense amount")
    print("7. Generate summary report in report.txt")
    print("8. Exit")


def main():
    """Run the menu repeatedly until the user chooses Exit."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            display_all_expenses()
        elif choice == "2":
            display_total_expenditure()
        elif choice == "3":
            display_expense_extremes()
        elif choice == "4":
            display_expenses_above_800()
        elif choice == "5":
            add_expense()
        elif choice == "6":
            update_expense()
        elif choice == "7":
            generate_summary_report()
        elif choice == "8":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


# Start the application only when this file is run directly.
if __name__ == "__main__":
    main()
