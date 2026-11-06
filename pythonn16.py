# Day 16: Magic Methods

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # String Representation
    def __str__(self):
        return f"{self.name} scored {self.marks} marks"

    # Length Method
    def __len__(self):
        return len(self.name)

    # Greater Than
    def __gt__(self, other):
        return self.marks > other.marks

    # Addition
    def __add__(self, other):
        return self.marks + other.marks


student1 = Student("Vikash", 90)
student2 = Student("Rahul", 80)

print(student1)

print("Name Length:", len(student1))

print("Vikash has more marks:", student1 > student2)

print("Total Marks:", student1 + student2)