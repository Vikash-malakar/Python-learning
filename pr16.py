import requests

API_URL = "https://api.frankfurter.app/latest"


def convert_currency(amount, from_currency, to_currency):
    params = {
        "amount": amount,
        "from": from_currency.upper(),
        "to": to_currency.upper()
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            print("❌ Currency conversion failed.")
            return

        data = response.json()

        converted_amount = data["rates"][to_currency.upper()]

        print("\n" + "=" * 45)
        print("        💱 CURRENCY CONVERTER")
        print("=" * 45)

        print(f"\n{amount:.2f} {from_currency.upper()} = "
              f"{converted_amount:.2f} {to_currency.upper()}")

        print("\n✅ Conversion successful!")

    except requests.exceptions.Timeout:
        print("⏰ Request timed out.")

    except requests.exceptions.RequestException as error:
        print(f"❌ Network error: {error}")

    except KeyError:
        print("❌ Invalid currency code.")


def main():
    print("\n" + "=" * 45)
    print("        💱 PYTHON CURRENCY CONVERTER")
    print("=" * 45)

    try:
        amount = float(input("\nEnter amount: "))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter a valid amount.")
        return

    from_currency = input(
        "From currency (e.g. USD): "
    ).strip()

    to_currency = input(
        "To currency (e.g. INR): "
    ).strip()

    if not from_currency or not to_currency:
        print("❌ Currency code cannot be empty.")
        return

    convert_currency(
        amount,
        from_currency,
        to_currency
    )


if __name__ == "__main__":
    main()