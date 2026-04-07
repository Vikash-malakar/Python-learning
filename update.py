# Day 1 Logical Program


print("=== Student Info System  ===")

# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

# Logic
is_adult = age >= 18

if marks >= 90:
    grade = "A+ "
elif marks >= 75:
    grade = "A "
elif marks >= 60:
    grade = "B "
elif marks >= 40:
    grade = "C "
else:
    grade = "Fail "

# Output
print("\n=== Result ===")
print("Name:", name)
print("Adult:", is_adult)
print("Marks:", marks)
print("Grade:", grade)