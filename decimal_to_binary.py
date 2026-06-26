number = int(input("Enter a decimal number: "))

binary = ""

if number == 0:
    binary = "0"

while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number //= 2

print("Binary Number:", binary)