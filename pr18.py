import os
from datetime import datetime

OUTPUT_FOLDER = "invoices"


def create_invoice():
    print("\n" + "=" * 50)
    print("              🧾 INVOICE GENERATOR")
    print("=" * 50)

    customer = input("\nCustomer name: ").strip()

    if not customer:
        print("❌ Customer name required.")
        return

    items = []

    while True:
        name = input("\nProduct name (q to finish): ").strip()

        if name.lower() == "q":
            break

        if not name:
            print("❌ Product name cannot be empty.")
            continue

        try:
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))

            if quantity <= 0 or price < 0:
                print("❌ Invalid quantity or price.")
                continue

        except ValueError:
            print("❌ Enter valid numbers.")
            continue

        items.append({
            "name": name,
            "quantity": quantity,
            "price": price
        })

    if not items:
        print("❌ No products added.")
        return

    total = sum(
        item["quantity"] * item["price"]
        for item in items
    )

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(
        OUTPUT_FOLDER,
        f"invoice_{timestamp}.txt"
    )

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write("                    INVOICE\n")
        file.write("=" * 60 + "\n")
        file.write(f"Customer: {customer}\n")
        file.write(
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write("-" * 60 + "\n")

        for item in items:
            amount = item["quantity"] * item["price"]

            file.write(
                f"{item['name']:<20}"
                f"{item['quantity']:<8}"
                f"₹{item['price']:<12.2f}"
                f"₹{amount:.2f}\n"
            )

        file.write("-" * 60 + "\n")
        file.write(f"TOTAL: ₹{total:.2f}\n")
        file.write("=" * 60 + "\n")

    print("\n✅ Invoice generated!")
    print(f"📁 Saved: {file_path}")
    print(f"💰 Total: ₹{total:.2f}")


if __name__ == "__main__":
    create_invoice()