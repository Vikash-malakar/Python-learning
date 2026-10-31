# Day 09: Dataclasses

from dataclasses import dataclass, field


# 1. Basic Dataclass

@dataclass
class Student:

    name: str
    age: int
    course: str


student1 = Student("Vikash", 22, "Python")

print(student1)


# 2. Dataclass with Default Values

@dataclass
class Employee:

    name: str
    salary: int
    department: str = "IT"


employee1 = Employee("Rahul", 50000)

print(employee1)


# 3. Dataclass with Methods

@dataclass
class Calculator:

    a: int
    b: int

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b


calc = Calculator(10, 20)

print("Addition:", calc.add())
print("Multiplication:", calc.multiply())


# 4. Dataclass with Default Factory

@dataclass
class Team:

    name: str
    members: list = field(default_factory=list)


team1 = Team("Python Developers")

team1.members.append("Vikash")
team1.members.append("Rahul")

print(team1)