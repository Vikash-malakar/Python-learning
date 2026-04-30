print("=== Bank Account Manager ===")

balance = 0
transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Mini Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        transactions.append("Deposited: " + str(amount))
        print("Amount Deposited")

    elif choice == "2":
        amount = float(input("Enter withdraw amount: "))

        if amount <= balance:
            balance -= amount
            transactions.append("Withdrawn: " + str(amount))
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    elif choice == "3":
        print("Current Balance:", balance)

    elif choice == "4":
        print("\nMini Statement:")
        if len(transactions) == 0:
            print("No Transactions")
        else:
            for t in transactions:
                print(t)

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")