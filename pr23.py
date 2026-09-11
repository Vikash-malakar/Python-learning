import re


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None


def main():
    print("\n" + "=" * 45)
    print("           📧 EMAIL VALIDATOR")
    print("=" * 45)

    email = input("\nEnter email: ").strip()

    if not email:
        print("❌ Email cannot be empty.")
        return

    if validate_email(email):
        print("\n✅ Valid email address!")
    else:
        print("\n❌ Invalid email address.")


if __name__ == "__main__":
    main()