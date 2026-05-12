print("Expense Tracker")

balance = float(input("Enter your total balance: "))

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Check Remaining Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        expense = float(input("Enter expense amount: "))
        expenses.append(expense)
        print("Expense Added")

    elif choice == "2":
        print("\nExpenses List")

        total = 0

        for e in expenses:
            print(e)
            total += e

        print("Total Expense:", total)

    elif choice == "3":
        total = sum(expenses)
        remaining = balance - total

        print("Remaining Balance:", remaining)

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")