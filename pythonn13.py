# Day 13: Polymorphism

# 1. Method Overriding

class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# 2. Polymorphism with Functions

class Car:

    def start(self):
        print("Car Started")


class Bike:

    def start(self):
        print("Bike Started")


def vehicle_start(vehicle):
    vehicle.start()


car = Car()
bike = Bike()

vehicle_start(car)
vehicle_start(bike)


# 3. Operator Overloading

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print("Addition:", num1 + num2)


# 4. Polymorphism with Built-in Functions

print(len("Python"))
print(len([10, 20, 30]))
print(len({"name": "Vikash", "age": 22}))