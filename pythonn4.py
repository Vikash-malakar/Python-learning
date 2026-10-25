# Day 04: Decorators in Python

# A decorator modifies the behavior of another function.

def my_decorator(func):

    def wrapper():
        print("Before Function Execution")

        func()

        print("After Function Execution")

    return wrapper


@my_decorator
def say_hello():
    print("Hello! Welcome to Python.")


say_hello()


# 2. Decorator with Arguments

def calculate_time(func):

    def wrapper(*args, **kwargs):
        print("Function Started")

        result = func(*args, **kwargs)

        print("Function Completed")

        return result

    return wrapper


@calculate_time
def add(a, b):
    return a + b


print("Addition:", add(10, 20))