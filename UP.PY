print("Student Grade Manager")

students = int(input("Enter number of students: "))

for i in range(students):
    print("\nStudent", i + 1)

    name = input("Enter name: ")

    marks1 = float(input("Enter marks of Subject 1: "))
    marks2 = float(input("Enter marks of Subject 2: "))
    marks3 = float(input("Enter marks of Subject 3: "))

    total = marks1 + marks2 + marks3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("\nResult")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)