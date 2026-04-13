print("=== Prime Number Checker  ===")

num = int(input("Enter a number: "))

if num <= 1:
    print(" Not a Prime Number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(" It is a Prime Number")
    else:
        print(" Not a Prime Number")