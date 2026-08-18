import secrets
import string


def generate_password(length):
    characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*()_+-="
    )

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password


def main():
    print("\n" + "=" * 40)
    print("       🔐 PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("\nEnter password length: "))

        if length < 6:
            print("❌ Password length should be at least 6.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    password = generate_password(length)

    print("\n✅ Password generated:")
    print("-" * 40)
    print(password)
    print("-" * 40)


if __name__ == "__main__":
    main()