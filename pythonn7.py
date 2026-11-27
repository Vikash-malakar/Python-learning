# Day 07: Context Managers

# 1. Using with Statement

with open("example.txt", "w") as file:
    file.write("Welcome to Advanced Python!")

print("File Created Successfully")


# 2. Reading File

with open("example.txt", "r") as file:
    content = file.read()

print("File Content:", content)


# 3. Custom Context Manager

class MyContextManager:

    def __enter__(self):
        print("Entering Context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")


with MyContextManager():
    print("Inside Context Manager")


# 4. Context Manager with contextlib

from contextlib import contextmanager


@contextmanager
def my_manager():

    print("Starting")

    try:
        yield
    finally:
        print("Closing")


with my_manager():
    print("Working Inside Manager")