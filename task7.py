from datetime import date


def birthday_countdown(month, day):
    today = date.today()

    try:
        birthday = date(today.year, month, day)
    except ValueError:
        print("❌ Invalid birthday.")
        return

    if birthday < today:
        birthday = date(today.year + 1, month, day)

    remaining = birthday - today

    print("\n" + "=" * 45)
    print("          🎂 BIRTHDAY COUNTDOWN")
    print("=" * 45)

    print(f"\n🎂 Next birthday: {birthday}")
    print(f"⏳ Days remaining: {remaining.days}")

    if remaining.days == 0:
        print("🎉 HAPPY BIRTHDAY! 🎉")


def main():
    print("\n🎂 Birthday Countdown")

    try:
        month = int(input("Birth month (1-12): "))
        day = int(input("Birth day: "))

        if not 1 <= month <= 12:
            print("❌ Invalid month.")
            return

        birthday_countdown(month, day)

    except ValueError:
        print("❌ Enter valid numbers.")


if __name__ == "__main__":
    main()