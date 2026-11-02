# Day 12: Inheritance

# 1. Single Inheritance

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


# 2. Multilevel Inheritance

class Grandfather:

    def property(self):
        print("Grandfather Property")


class Father(Grandfather):

    def car(self):
        print("Father has a car")


class Son(Father):

    def bike(self):
        print("Son has a bike")


son = Son()

son.property()
son.car()
son.bike()


# 3. Multiple Inheritance

class Father:

    def father_skill(self):
        print("Father: Business")


class Mother:

    def mother_skill(self):
        print("Mother: Cooking")


class Child(Father, Mother):

    def child_skill(self):
        print("Child: Programming")


child = Child()

child.father_skill()
child.mother_skill()
child.child_skill()


# 4. Hierarchical Inheritance

class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


car = Car()
bike = Bike()

car.start()
bike.start()