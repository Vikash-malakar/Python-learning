import random


def play_game():
    print("\n" + "=" * 45)
    print("        🔢 NUMBER GUESSING GAME")
    print("=" * 45)

    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ Enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < number:
            print("📈 Too low! Try a higher number.")

        elif guess > number:
            print("📉 Too high! Try a lower number.")

        else:
            print("\n🎉 Congratulations!")
            print(f"✅ Correct number: {number}")
            print(f"🎯 Attempts: {attempts}")
            break


def main():
    while True:
        play_again = input(
            "\nPlay again? (y/n): "
        ).lower().strip()

        if play_again == "y":
            play_game()

        elif play_again == "n":
            print("\n👋 Thanks for playing!")
            break

        else:
            print("❌ Enter y or n.")


if __name__ == "__main__":
    play_game()
    main()