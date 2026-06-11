FILE_NAME = "books.txt"


def read_books():
    """Read book records from the file into a list of dictionaries."""
    books = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                fields = line.strip().split(",")

                if len(fields) == 3:
                    book_id, title, quantity_text = fields
                    try:
                        books.append(
                            {
                                "id": book_id,
                                "title": title,
                                "quantity": int(quantity_text),
                            }
                        )
                    except ValueError:
                        print("Skipped a record with an invalid quantity:", line.strip())
    except FileNotFoundError:
        open(FILE_NAME, "w").close()

    return books


def write_books(books):
    """Rewrite the original file with the updated book records."""
    with open(FILE_NAME, "w") as file:
        for book in books:
            file.write(f"{book['id']},{book['title']},{book['quantity']}\n")


def display_book(book):
    print(
        f"Book ID: {book['id']}, "
        f"Title: {book['title']}, "
        f"Available Copies: {book['quantity']}"
    )


def find_book(books, book_id):
    for book in books:
        if book["id"].upper() == book_id.upper():
            return book
    return None


def display_all_books():
    books = read_books()

    if not books:
        print("No book records found.")
        return

    print("\n--- All Books ---")
    for book in books:
        display_book(book)


def search_book():
    book_id = input("Enter Book ID: ").strip().upper()
    book = find_book(read_books(), book_id)

    if book:
        print("\nBook found:")
        display_book(book)
    else:
        print("Book ID not found.")


def issue_book():
    books = read_books()
    book_id = input("Enter Book ID to issue: ").strip().upper()
    book = find_book(books, book_id)

    if not book:
        print("Book ID not found.")
        return

    if book["quantity"] == 0:
        print(f"'{book['title']}' is currently unavailable.")
        return

    book["quantity"] -= 1
    write_books(books)
    print(f"'{book['title']}' issued successfully.")
    print(f"Remaining copies: {book['quantity']}")


def return_book():
    books = read_books()
    book_id = input("Enter Book ID to return: ").strip().upper()
    book = find_book(books, book_id)

    if not book:
        print("Book ID not found.")
        return

    book["quantity"] += 1
    write_books(books)
    print(f"'{book['title']}' returned successfully.")
    print(f"Available copies: {book['quantity']}")


def display_unavailable_books():
    books = read_books()
    unavailable_books = [book for book in books if book["quantity"] == 0]

    if not unavailable_books:
        print("All books are currently available.")
        return

    print("\n--- Unavailable Books ---")
    for book in unavailable_books:
        display_book(book)


def display_restocking_books():
    books = read_books()
    restocking_books = [book for book in books if book["quantity"] < 2]

    if not restocking_books:
        print("No books currently require restocking.")
        return

    print("\n--- Books Requiring Restocking ---")
    for book in restocking_books:
        display_book(book)


def display_menu():
    print("\n===== Library Book Issue System =====")
    print("1. Display all books")
    print("2. Search a book using Book ID")
    print("3. Issue a book")
    print("4. Return a book")
    print("5. Display unavailable books")
    print("6. Display books requiring restocking")
    print("7. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_all_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            display_unavailable_books()
        elif choice == "6":
            display_restocking_books()
        elif choice == "7":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
