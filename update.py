
print("=== Student Result System ===")

name = input("Enter student name: ")

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

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

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\n=== Result ===")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Status:", result)