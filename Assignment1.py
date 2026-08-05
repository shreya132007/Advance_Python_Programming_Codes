# TITLE :- Introduction to OOP Concepts

"""
AIM : Write a program to create a simplified Library Management System using object-oriented
programming principles in Python. This system should manage books and patrons (library users),
allowing for basic operations such as adding new books, registering patrons, borrowing books, and
returning books.
"""


class Library:

    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def display(self):
        if self.available:
            print(self.book_name, self.author, "Available")
        else:
            print(self.book_name, self.author, "Not Available")

    def issue_book(self):
        if self.available:
            self.available = False
            print("Book Issued Successfully")
        else:
            print("Book is Not Available")

    def return_book(self):
        if self.available:
            print("Book is Already in Library")
        else:
            self.available = True
            print("Book Returned Successfully")


# Creating Objects
book1 = Library("1984", "George Orwell")
book2 = Library("The Alchemist", "Paulo Coelho")
book3 = Library("The Starks", "John Smith")

books = [book1, book2, book3]

while True:

    print("\n------ Library Menu ------")
    print("1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        for book in books:
            book.display()

    elif choice == "2":
        name = input("Enter Book Name: ")

        found = False
        for book in books:
            if book.book_name.lower() == name.lower():
                book.issue_book()
                found = True
                break

        if not found:
            print("Book Not Found")

    elif choice == "3":
        name = input("Enter Book Name: ")

        found = False
        for book in books:
            if book.book_name.lower() == name.lower():
                book.return_book()
                found = True
                break

        if not found:
            print("Book Not Found")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")


#output 
# ------ Library Menu ------
# 1. Display Books
# 2. Issue Book
# 3. Return Book
# 4. Exit
# Enter Choice: 1
# 1984 George Orwell Available
# The Alchemist Paulo Coelho Available
# The Starks John Smith Available