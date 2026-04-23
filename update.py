print("=== Library Management System ===")

books = ["Python", "Java", "C++", "Django"]

while True:
    print("\n1. View Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Add Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nAvailable Books:")
        for book in books:
            print(book)

    elif choice == "2":
        book_name = input("Enter book name to issue: ")

        if book_name in books:
            books.remove(book_name)
            print("Book Issued")
        else:
            print("Book Not Available")

    elif choice == "3":
        book_name = input("Enter book name to return: ")
        books.append(book_name)
        print("Book Returned")

    elif choice == "4":
        book_name = input("Enter new book name: ")
        books.append(book_name)
        print("Book Added")

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")