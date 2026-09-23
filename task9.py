players = {}


def add_player():
    name = input("\nPlayer name: ").strip()

    if not name:
        print("❌ Name required.")
        return

    players[name] = players.get(name, 0)

    try:
        score = int(input("Enter score: "))
    except ValueError:
        print("❌ Invalid score.")
        return

    players[name] += score

    print("✅ Score added!")


def show_scores():
    if not players:
        print("\n❌ No players found.")
        return

    print("\n🏆 SCOREBOARD")
    print("-" * 30)

    ranking = sorted(
        players.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for position, (name, score) in enumerate(ranking, 1):
        print(f"{position}. {name:<15} {score}")


def main():
    while True:
        print("\n1. Add Score")
        print("2. Show Scores")
        print("3. Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            show_scores()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()