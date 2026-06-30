number = int(input("Enter a number: "))

visited = []

while number != 1 and number not in visited:

    visited.append(number)

    total = 0

    while number > 0:
        digit = number % 10
        total += digit * digit
        number //= 10

    number = total

if number == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")