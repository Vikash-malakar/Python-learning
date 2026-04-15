print("=== Expense Tracker ===")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Show Highest Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense Added")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found")
        else:
            print("Expenses List:")
            for i in range(len(expenses)):
                print(i + 1, "=", expenses[i])

    elif choice == "3":
        total = sum(expenses)
        print("Total Expense:", total)

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses found")
        else:
            print("Highest Expense:", max(expenses))

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")