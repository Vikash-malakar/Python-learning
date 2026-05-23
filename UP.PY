print("Library Book Manager")

books = ["Python", "Java", "C++"]

issued_books = []

while True:
    print("\n1. View Books")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. View Issued Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Books")

        if len(books) == 0:
            print("No Books Available")

        else:
            for book in books:
                print(book)

    elif choice == "2":
        new_book = input("Enter new book name: ")

        books.append(new_book)

        print("Book Added Successfully")

    elif choice == "3":
        issue_book = input("Enter book name to issue: ")

        if issue_book in books:
            books.remove(issue_book)
            issued_books.append(issue_book)

            print("Book Issued Successfully")

        else:
            print("Book Not Available")

    elif choice == "4":
        print("\nIssued Books")

        if len(issued_books) == 0:
            print("No Books Issued")

        else:
            for book in issued_books:
                print(book)

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")