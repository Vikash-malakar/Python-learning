import random

print("=== Number Guessing Game ===")

secret_number = random.randint(1, 20)
attempt = 0

while True:
    guess = int(input("Enter your guess (1 to 20): "))
    attempt += 1

    if guess == secret_number:
        print("Correct Guess")
        print("Total Attempts:", attempt)
        break

    elif guess > secret_number:
        print("Too High")

    else:
        print("Too Low")