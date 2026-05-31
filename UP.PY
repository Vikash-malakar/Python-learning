print("Expense Splitter")

total_expense = float(input("Enter total expense: "))
people = int(input("Enter number of people: "))

share = total_expense / people

print("\nExpense Details")
print("Total Expense:", total_expense)
print("Number of People:", people)
print("Each Person Pays:", round(share, 2))