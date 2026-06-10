FILE_NAME = "passwords.txt"

def add_password():
    website = input("Enter Website: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{website},{username},{password}\n")

    print("Password Saved Successfully")


def view_passwords():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No Records Found")

            else:
                print("\nSaved Credentials")

                for line in data:
                    website, username, password = line.strip().split(",")

                    print("Website :", website)
                    print("Username:", username)
                    print("Password:", password)
                    print("-" * 30)

    except FileNotFoundError:
        print("No Records Found")


def search_password():
    website_name = input("Enter Website Name: ")

    try:
        with open(FILE_NAME, "r") as file:

            found = False

            for line in file:
                website, username, password = line.strip().split(",")

                if website.lower() == website_name.lower():

                    print("\nRecord Found")
                    print("Username:", username)
                    print("Password:", password)

                    found = True
                    break

            if not found:
                print("Website Not Found")

    except FileNotFoundError:
        print("No Records Found")


while True:

    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")