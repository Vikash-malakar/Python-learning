print("=== Login & Signup System ===")

FILE_NAME = "users.txt"

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print("Signup Successful")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open(FILE_NAME, "r") as file:
            users = file.readlines()

            for user in users:
                u, p = user.strip().split(",")

                if u == username and p == password:
                    print("Login Successful")
                    return

            print("Invalid Credentials")

    except FileNotFoundError:
        print("No users found. Please signup first.")

while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        signup()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")