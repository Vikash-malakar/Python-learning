from datetime import date


def calculate_age(birth_date):
    today = date.today()

    years = today.year - birth_date.year

    if (
        today.month,
        today.day
    ) < (
        birth_date.month,
        birth_date.day
    ):
        years -= 1

    return years


def main():
    print("\n" + "=" * 45)
    print("             🎂 AGE CALCULATOR")
    print("=" * 45)

    try:
        year = int(input("\nBirth year: "))
        month = int(input("Birth month: "))
        day = int(input("Birth day: "))

        birth_date = date(year, month, day)

        if birth_date > date.today():
            print("❌ Birth date future me nahi ho sakti.")
            return

        age = calculate_age(birth_date)

        print(f"\n🎉 Your age is: {age} years")

    except ValueError:
        print("❌ Please enter a valid date.")


if __name__ == "__main__":
    main()