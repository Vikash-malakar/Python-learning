print("=== Contact Book ===")

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number
        print("Contact Saved")

    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts Found")
        else:
            print("\nSaved Contacts:")
            for name, number in contacts.items():
                print(name, ":", number)

    elif choice == "3":
        search = input("Enter name to search: ")

        if search in contacts:
            print("Number:", contacts[search])
        else:
            print("Contact Not Found")

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")