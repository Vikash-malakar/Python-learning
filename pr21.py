import secrets


def generate_otp(length):
    start = 10 ** (length - 1)
    end = (10 ** length) - 1

    return str(secrets.randbelow(end - start + 1) + start)


def main():
    print("\n" + "=" * 40)
    print("             🔐 OTP GENERATOR")
    print("=" * 40)

    try:
        length = int(
            input("\nEnter OTP length (4-8): ")
        )

        if length < 4 or length > 8:
            print("❌ OTP length must be between 4 and 8.")
            return

    except ValueError:
        print("❌ Enter a valid number.")
        return

    otp = generate_otp(length)

    print("\n✅ Your OTP:")
    print("-" * 20)
    print(otp)
    print("-" * 20)


if __name__ == "__main__":
    main()