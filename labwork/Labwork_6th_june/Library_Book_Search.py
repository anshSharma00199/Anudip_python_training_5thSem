books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

print("Unavailable Books:")
for book, copies in books:
    if copies == 0:
        print(book)

print("\nBooks With More Than 2 Copies:")
for book, copies in books:
    if copies > 2:
        print(book)

available = 0

for book, copies in books:
    if copies > 0:
        available += 1

print("\nAvailable Books:", available)

search = input("Enter Book Name: ")

for book, copies in books:
    if book.lower() == search.lower():
        print("Book Found")
        break
else:
    print("Book Not Found")