print("=== Employee Salary System ===")

name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

bonus = basic_salary * 0.10
tax = basic_salary * 0.05
final_salary = basic_salary + bonus - tax

print("\n=== Salary Slip ===")
print("Employee Name:", name)
print("Basic Salary:", basic_salary)
print("Bonus (10%):", bonus)
print("Tax (5%):", tax)
print("Final Salary:", final_salary)
print("_______________--------______________")