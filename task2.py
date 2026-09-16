import random


choices = ["rock", "paper", "scissors"]


def get_winner(user, computer):
    if user == computer:
        return "draw"

    if (
        (user == "rock" and computer == "scissors")
        or
        (user == "paper" and computer == "rock")
        or
        (user == "scissors" and computer == "paper")
    ):
        return "user"

    return "computer"


def play_game():
    user_score = 0
    computer_score = 0

    print("\n" + "=" * 45)
    print("        ✊ ROCK PAPER SCISSORS")
    print("=" * 45)

    while True:
        print("\nChoose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        choice = input("\nYour choice: ").strip()

        if choice == "4":
            break

        if choice not in ["1", "2", "3"]:
            print("❌ Invalid choice.")
            continue

        user = choices[int(choice) - 1]
        computer = random.choice(choices)

        print(f"\n👤 You: {user}")
        print(f"🤖 Computer: {computer}")

        winner = get_winner(user, computer)

        if winner == "draw":
            print("🤝 Draw!")

        elif winner == "user":
            print("🎉 You win!")
            user_score += 1

        else:
            print("🤖 Computer wins!")
            computer_score += 1

        print(
            f"\nScore → You: {user_score} | "
            f"Computer: {computer_score}"
        )


if __name__ == "__main__":
    play_game()