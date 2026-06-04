balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance = Rs.", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: Rs."))
        balance += amount
        print("Rs.", amount, "deposited successfully.")
        print("Updated Balance = Rs.", balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: Rs."))

        if amount <= balance:
            balance -= amount
            print("Rs.", amount, "withdrawn successfully.")
            print("Remaining Balance = Rs.", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid Choice! Please try again.")