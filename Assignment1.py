# TITLE :- Introduction to OOP Concepts

"""
AIM : Write a program to create a simplified Library Management System using object-oriented
programming principles in Python. This system should manage books and patrons (library users),
allowing for basic operations such as adding new books, registering patrons, borrowing books, and
returning books.
"""

# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Patron ID: {self.patron_id}, Name: {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is currently unavailable.")

    # Return a book
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[patron_id]

        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.available = True
                patron.borrowed_books.remove(book)
                print(f"{patron.name} returned '{book.title}'.")
                return

        print("This book was not borrowed by the patron.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(book)

    # Display all patrons
    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            print(patron)


# ---------------- Main Program ----------------

library = Library()

# Adding books
library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Mark Lee"))
library.add_book(Book(103, "Machine Learning", "Andrew Ng"))

# Registering patrons
library.register_patron(Patron(1, "Alice"))
library.register_patron(Patron(2, "Bob"))

# Display books
library.display_books()

# Borrow books
library.borrow_book(1, 101)
library.borrow_book(2, 102)

# Display books after borrowing
library.display_books()

# Return a book
library.return_book(1, 101)

# Display books after returning
library.display_books()