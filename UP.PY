print("=== Notes Manager ===")

FILE_NAME = "notes.txt"

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open(FILE_NAME, "a") as file:
            file.write(note + "\n")

        print("Note Saved")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                data = file.read()

                if data == "":
                    print("No Notes Found")
                else:
                    print("\nYour Notes:\n")
                    print(data)

        except FileNotFoundError:
            print("No Notes Found")

    elif choice == "3":
        open(FILE_NAME, "w").close()
        print("All Notes Deleted")

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")