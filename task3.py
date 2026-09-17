import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("\n" + "=" * 40)
    print("          🎲 DICE ROLLING SIMULATOR")
    print("=" * 40)

    while True:
        choice = input(
            "\nPress Enter to roll or q to quit: "
        ).strip().lower()

        if choice == "q":
            print("\n👋 Goodbye!")
            break

        dice1 = roll_dice()
        dice2 = roll_dice()

        print(f"\n🎲 Dice 1: {dice1}")
        print(f"🎲 Dice 2: {dice2}")
        print(f"🎯 Total : {dice1 + dice2}")


if __name__ == "__main__":
    main()