print("Student Attendance System")

attendance = {}

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        status = input("Present or Absent: ")

        attendance[name] = status

        print("Attendance Marked")

    elif choice == "2":
        print("\nAttendance Record")

        if len(attendance) == 0:
            print("No Record Found")

        else:
            for name, status in attendance.items():
                print(name, ":", status)

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")