import random

print("Number Guessing Game")

secret_number = random.randint(1, 20)

attempts = 0

while True:
    guess = int(input("Guess a number between 1 to 20: "))
    attempts += 1

    if guess == secret_number:
        print("Correct Guess")
        print("Total Attempts:", attempts)
        break

    elif guess > secret_number:
        print("Too High")

    else:
        print("Too Low")