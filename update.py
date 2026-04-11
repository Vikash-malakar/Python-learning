print("=== Number Pyramid  ===")

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # spaces
    for j in range(rows - i):
        print(" ", end="")

    # numbers
    for k in range(1, i + 1):
        print(k, end=" ")

    print()