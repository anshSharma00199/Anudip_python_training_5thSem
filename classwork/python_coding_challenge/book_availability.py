# Sample Data
books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}

# 1. Books with fewer than 3 copies
attention_books = [
    book for book, copies in books.items()
    if copies < 3
]

# 2. Book with maximum copies
max_book = max(books, key=books.get)

# 3. Book with minimum copies
min_book = min(books, key=books.get)

# 4. Total copies available
total_copies = sum(books.values())

# 5. Restocking list
restocking_list = []
for book, copies in books.items():
    if copies < 3:
        restocking_list.append(book)

# Output
print("Books Requiring Attention:")
for book in attention_books:
    print(book)

print(f"\nBook with Maximum Copies: {max_book} ({books[max_book]} copies)")
print(f"Book with Minimum Copies: {min_book} ({books[min_book]} copies)")
print("Total Copies Available:", total_copies)
print("Restocking List:", restocking_list)