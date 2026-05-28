print("Online Food Order System")

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Cold Drink": 60
}

cart = []
total = 0

while True:
    print("\nMenu")

    for item, price in menu.items():
        print(item, "-", price)

    print("\n1. Order Food")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        food = input("Enter food name: ")

        if food in menu:
            cart.append(food)
            total += menu[food]

            print(food, "Added To Cart")

        else:
            print("Food Item Not Available")

    elif choice == "2":
        print("\nYour Cart")

        if len(cart) == 0:
            print("Cart Is Empty")

        else:
            for item in cart:
                print(item)

            print("Current Total:", total)

    elif choice == "3":
        print("\nCheckout")

        if len(cart) == 0:
            print("Cart Is Empty")

        else:
            print("Ordered Items:")

            for item in cart:
                print(item)

            print("Final Bill:", total)

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")