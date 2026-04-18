print("=== ATM Machine ===")

pin = "1234"
balance = 5000

user_pin = input("Enter PIN: ")

if user_pin == pin:

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Updated Balance:", balance)

        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))

            if amount <= balance:
                balance -= amount
                print("Updated Balance:", balance)
            else:
                print("Insufficient Balance")

        elif choice == "4":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

else:
    print("Wrong PIN")