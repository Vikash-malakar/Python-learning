import json
import os

FILE_NAME = "inventory.json"


def load_inventory():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_inventory(inventory):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)


def add_product(inventory):
    print("\n--- ➕ ADD PRODUCT ---")

    name = input("Product name: ").strip()

    if not name:
        print("❌ Product name cannot be empty.")
        return

    try:
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        if price < 0 or quantity < 0:
            print("❌ Price and quantity cannot be negative.")
            return

    except ValueError:
        print("❌ Please enter valid numbers.")
        return

    product = {
        "id": len(inventory) + 1,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    save_inventory(inventory)

    print("✅ Product added successfully!")


def view_products(inventory):
    print("\n--- 📦 INVENTORY ---")

    if not inventory:
        print("❌ No products found.")
        return

    print("-" * 65)
    print(f"{'ID':<5}{'Product':<25}{'Price':<15}{'Quantity':<10}")
    print("-" * 65)

    for product in inventory:
        print(
            f"{product['id']:<5}"
            f"{product['name']:<25}"
            f"₹{product['price']:<14.2f}"
            f"{product['quantity']:<10}"
        )

    print("-" * 65)


def update_product(inventory):
    print("\n--- ✏️ UPDATE PRODUCT ---")

    if not inventory:
        print("❌ No products available.")
        return

    view_products(inventory)

    try:
        product_id = int(input("\nEnter product ID: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for product in inventory:
        if product["id"] == product_id:

            try:
                price = float(input("New price: "))
                quantity = int(input("New quantity: "))

                if price < 0 or quantity < 0:
                    print("❌ Values cannot be negative.")
                    return

            except ValueError:
                print("❌ Enter valid numbers.")
                return

            product["price"] = price
            product["quantity"] = quantity

            save_inventory(inventory)

            print("✅ Product updated successfully!")
            return

    print("❌ Product not found.")


def delete_product(inventory):
    print("\n--- 🗑️ DELETE PRODUCT ---")

    if not inventory:
        print("❌ No products available.")
        return

    view_products(inventory)

    try:
        product_id = int(input("\nEnter product ID: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for product in inventory:
        if product["id"] == product_id:

            inventory.remove(product)

            for index, product in enumerate(inventory, start=1):
                product["id"] = index

            save_inventory(inventory)

            print("🗑️ Product deleted successfully!")
            return

    print("❌ Product not found.")


def low_stock(inventory):
    print("\n--- ⚠️ LOW STOCK PRODUCTS ---")

    low_stock_products = [
        product
        for product in inventory
        if product["quantity"] <= 5
    ]

    if not low_stock_products:
        print("✅ No low-stock products.")
        return

    for product in low_stock_products:
        print(
            f"⚠️ {product['name']} "
            f"→ Only {product['quantity']} left"
        )


def main():
    inventory = load_inventory()

    while True:
        print("\n" + "=" * 50)
        print("             📦 INVENTORY MANAGER")
        print("=" * 50)

        print("1. ➕ Add Product")
        print("2. 📋 View Products")
        print("3. ✏️ Update Product")
        print("4. 🗑️ Delete Product")
        print("5. ⚠️ Low Stock")
        print("6. 🚪 Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_product(inventory)

        elif choice == "2":
            view_products(inventory)

        elif choice == "3":
            update_product(inventory)

        elif choice == "4":
            delete_product(inventory)

        elif choice == "5":
            low_stock(inventory)

        elif choice == "6":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()