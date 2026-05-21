print("Simple Banking System")

balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Money Deposited Successfully")

    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))

        if amount <= balance:
            balance -= amount
            print("Money Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")