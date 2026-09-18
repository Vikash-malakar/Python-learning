def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def main():
    print("\n" + "=" * 40)
    print("             🧮 CALCULATOR")
    print("=" * 40)

    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nChoose operation: ")

        if choice == "5":
            print("👋 Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("❌ Invalid choice.")
            continue

        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
        except ValueError:
            print("❌ Enter valid numbers.")
            continue

        if choice == "1":
            result = add(first, second)

        elif choice == "2":
            result = subtract(first, second)

        elif choice == "3":
            result = multiply(first, second)

        else:
            result = divide(first, second)

            if result is None:
                print("❌ Cannot divide by zero.")
                continue

        print(f"\n✅ Result: {result}")


if __name__ == "__main__":
    main()