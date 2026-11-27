# Day 08: Exception Handling

# 1. Basic Exception Handling

try:
    num = int(input("Enter a number: "))

    result = 100 / num

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter a valid integer!")

finally:
    print("Program Finished")


# 2. Custom Exception

class InvalidAgeError(Exception):
    pass


def check_age(age):

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above!")

    else:
        print("You are eligible.")


try:
    check_age(16)

except InvalidAgeError as error:
    print("Error:", error)


# 3. Raising an Exception

def withdraw(balance, amount):

    if amount > balance:
        raise ValueError("Insufficient Balance!")

    return balance - amount


try:
    remaining = withdraw(5000, 6000)
    print("Remaining Balance:", remaining)

except ValueError as error:
    print(error)