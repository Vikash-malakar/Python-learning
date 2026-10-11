import re


def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    return score, suggestions


def main():
    print("\n" + "=" * 50)
    print("         🔐 PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    password = input("\nEnter password: ")

    score, suggestions = check_password(password)

    print("\n📊 Result")

    if score <= 2:
        print("🔴 Weak Password")
    elif score <= 4:
        print("🟡 Medium Password")
    else:
        print("🟢 Strong Password")

    print(f"Score: {score}/5")

    if suggestions:
        print("\n💡 Suggestions:")
        for suggestion in suggestions:
            print(f"• {suggestion}")


if __name__ == "__main__":
    main()