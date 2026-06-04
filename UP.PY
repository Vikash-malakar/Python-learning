expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense Added Successfully")

    elif choice == "2":

        if len(expenses) == 0:
            print("No Expenses Found")

        else:
            print("\nExpense List")

            for exp in expenses:
                print(
                    "Category:",
                    exp["category"],
                    "| Amount:",
                    exp["amount"]
                )

    elif choice == "3":

        total = 0

        for exp in expenses:
            total += exp["amount"]

        print("Total Expense =", total)

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")