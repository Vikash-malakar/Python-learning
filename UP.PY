products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Headphone": 2000
}

cart = []

def show_products():
    print("\nAvailable Products")

    for product, price in products.items():
        print(product, "-", price)


def add_to_cart():
    product = input("Enter Product Name: ")

    if product in products:
        cart.append(product)
        print("Product Added To Cart")
    else:
        print("Product Not Found")


def view_cart():
    if len(cart) == 0:
        print("Cart Is Empty")

    else:
        total = 0

        print("\nCart Items")

        for item in cart:
            print(item, "-", products[item])
            total += products[item]

        print("Total Bill:", total)


while True:

    print("\n===== MINI E-COMMERCE =====")
    print("1. Show Products")
    print("2. Add To Cart")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        print("Thank You For Visiting")
        break

    else:
        print("Invalid Choice")