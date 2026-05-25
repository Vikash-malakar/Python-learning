print("Employee Record System")

employees = {}

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        employees[emp_id] = {
            "name": name,
            "salary": salary
        }

        print("Employee Added Successfully")

    elif choice == "2":
        print("\nEmployee Records")

        if len(employees) == 0:
            print("No Records Found")

        else:
            for emp_id, details in employees.items():
                print("ID:", emp_id)
                print("Name:", details["name"])
                print("Salary:", details["salary"])
                print()

    elif choice == "3":
        search_id = input("Enter Employee ID: ")

        if search_id in employees:
            print("\nEmployee Found")
            print("Name:", employees[search_id]["name"])
            print("Salary:", employees[search_id]["salary"])

        else:
            print("Employee Not Found")

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")