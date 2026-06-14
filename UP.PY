students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    marks1 = float(input("Enter Physics Marks: "))
    marks2 = float(input("Enter Chemistry Marks: "))
    marks3 = float(input("Enter Math Marks: "))

    total = marks1 + marks2 + marks3
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students[roll_no] = {
        "name": name,
        "percentage": percentage,
        "grade": grade
    }

    print("Student Added Successfully")


def view_students():
    if len(students) == 0:
        print("No Students Found")
        return

    print("\nStudent Records")

    for roll_no, data in students.items():
        print(
            "Roll No:", roll_no,
            "| Name:", data["name"],
            "| Percentage:", round(data["percentage"], 2),
            "| Grade:", data["grade"]
        )


def find_topper():
    if len(students) == 0:
        print("No Students Found")
        return

    topper = max(
        students,
        key=lambda x: students[x]["percentage"]
    )

    print("\nTopper Details")
    print("Name:", students[topper]["name"])
    print("Percentage:", round(students[topper]["percentage"], 2))


while True:

    print("\n===== STUDENT RESULT MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        find_topper()

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")