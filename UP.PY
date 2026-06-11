products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000
}

cart = {}

def show_products():
    print("\nAvailable Products")

    for product, price in products.items():
        print(product, "-", price)


def buy_product():
    product = input("Enter Product Name: ")

    if product in products:

        quantity = int(input("Enter Quantity: "))

        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity

        print("Product Added To Cart")

    else:
        print("Product Not Found")


def generate_bill():

    if len(cart) == 0:
        print("Cart Is Empty")
        return

    total = 0

    print("\n===== BILL =====")

    for product, quantity in cart.items():

        amount = products[product] * quantity

        print(
            product,
            "| Price:", products[product],
            "| Qty:", quantity,
            "| Amount:", amount
        )

        total += amount

    print("\nTotal Bill =", total)


while True:

    print("\n===== INVENTORY BILLING SYSTEM =====")
    print("1. Show Products")
    print("2. Buy Product")
    print("3. Generate Bill")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        buy_product()

    elif choice == "3":
        generate_bill()

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")