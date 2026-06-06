employees = {}

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))

    employees[emp_id] = {
        "name": name,
        "salary": salary
    }

    print("Employee Added Successfully")


def view_employees():
    if len(employees) == 0:
        print("No Employees Found")

    else:
        print("\nEmployee Records")

        for emp_id, data in employees.items():
            print(
                "ID:", emp_id,
                "| Name:", data["name"],
                "| Salary:", data["salary"]
            )


def calculate_bonus():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        salary = employees[emp_id]["salary"]

        bonus = salary * 0.10

        print("Employee:", employees[emp_id]["name"])
        print("Salary:", salary)
        print("Bonus:", bonus)

    else:
        print("Employee Not Found")


while True:

    print("\n===== Employee Salary Manager =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Calculate Bonus")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        calculate_bonus()

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")