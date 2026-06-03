print("Student Management System")

students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students[roll_no] = {
            "name": name,
            "marks": marks
        }

        print("Student Added Successfully")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found")
        else:
            print("\nStudent Records")
            for roll_no, details in students.items():
                print(
                    "Roll No:", roll_no,
                    "| Name:", details["name"],
                    "| Marks:", details["marks"]
                )

    elif choice == "3":
        roll_no = input("Enter Roll Number: ")

        if roll_no in students:
            print("Name:", students[roll_no]["name"])
            print("Marks:", students[roll_no]["marks"])
        else:
            print("Student Not Found")

    elif choice == "4":
        roll_no = input("Enter Roll Number: ")

        if roll_no in students:
            del students[roll_no]
            print("Student Deleted")
        else:
            print("Student Not Found")

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")