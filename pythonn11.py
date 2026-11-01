# Day 11: Object-Oriented Programming (OOP)

# 1. Creating a Class

class Student:

    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Instance Method
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Creating Objects
student1 = Student("Vikash", 22, "Python")
student2 = Student("Rahul", 23, "Java")

# Calling Methods
student1.display_details()

print("----------------")

student2.display_details()


# 2. Class Variable

class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary, self.company)


emp1 = Employee("Vikash", 50000)
emp2 = Employee("Rahul", 60000)

emp1.display()
emp2.display()


# 3. Class Method

class School:

    school_name = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school_name = name


School.change_school("XYZ School")

print("School:", School.school_name)


# 4. Static Method

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print("Addition:", Calculator.add(10, 20))