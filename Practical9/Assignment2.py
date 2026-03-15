#Lab Assignment-2

"""
Create a Library Management System with the following mechanisms:

a) Design classes for Book, Member, and Library

b) Implement methods for adding books, lending books to members, returning books, and displaying book information.

C) Create a menu-driven interface for the library management system.
"""

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        book = Book(title)
        self.books.append(book)
        print("Book added successfully")

    def lend_book(self):
        title = input("Enter book title to lend: ")
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book lent successfully")
                return
        print("Book not available")

    def return_book(self):
        title = input("Enter book title to return: ")
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned successfully")
                return
        print("Book not found")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(book.title, "-", status)


library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Lend Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.lend_book()
    elif choice == 3:
        library.return_book()
    elif choice == 4:
        library.display_books()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")