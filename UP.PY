print("Inventory Management System")

inventory = {}

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = quantity
        print("Product Added Successfully")

    elif choice == "2":
        print("\nAvailable Products")

        if len(inventory) == 0:
            print("No Products Found")
        else:
            for product, quantity in inventory.items():
                print(product, ":", quantity)

    elif choice == "3":
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Stock Updated")
        else:
            print("Product Not Found")

    elif choice == "4":
        product = input("Enter product name: ")

        if product in inventory:
            print("Stock:", inventory[product])
        else:
            print("Product Not Found")

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")