number = int(input("Enter a number: "))

total = 0

for i in range(1, number):
    if number % i == 0:
        total += i

if total == number:
    print(number, "is a Perfect Number")
else:
    print(number, "is not a Perfect Number")