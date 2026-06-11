# Library Book Issue System

def read_books():
    books = []
    file = open("books.txt", "r")
    for line in file:
        data = line.strip().split(",")
        books.append(data)
    file.close()
    return books


def write_books(books):
    file = open("books.txt", "w")
    for book in books:
        file.write(book[0] + "," + book[1] + "," + str(book[2]) + "\n")
    file.close()


def display_books():
    books = read_books()
    print("\nBook Records")
    print("-------------------------")
    for book in books:
        print("ID:", book[0], "Book:", book[1], "Copies:", book[2])


def search_book():
    books = read_books()
    bid = input("Enter Book ID: ")

    for book in books:
        if book[0] == bid:
            print("\nBook Found")
            print("ID:", book[0])
            print("Title:", book[1])
            print("Copies:", book[2])
            return

    print("Book Not Found")


def issue_book():
    books = read_books()
    bid = input("Enter Book ID to Issue: ")

    for book in books:
        if book[0] == bid:
            if int(book[2]) > 0:
                book[2] = str(int(book[2]) - 1)
                write_books(books)
                print("Book Issued Successfully")
            else:
                print("Book Not Available")
            return

    print("Book Not Found")


def return_book():
    books = read_books()
    bid = input("Enter Book ID to Return: ")

    for book in books:
        if book[0] == bid:
            book[2] = str(int(book[2]) + 1)
            write_books(books)
            print("Book Returned Successfully")
            return

    print("Book Not Found")


def unavailable_books():
    books = read_books()

    print("\nUnavailable Books")
    for book in books:
        if int(book[2]) == 0:
            print(book[0], book[1])


def restocking_books():
    books = read_books()

    print("\nBooks Requiring Restocking")
    for book in books:
        if int(book[2]) < 2:
            print(book[0], book[1], "Copies:", book[2])


while True:
    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restocking_books()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")