import random

print("=== Number Guessing Game  ===")

# Random number generate (1 to 10)
secret_number = random.randint(1, 10)

# User input
guess = int(input("Guess a number between 1 to 10: "))

# Logic
if guess == secret_number:
    print(" Correct! You guessed it right!")
elif guess > secret_number:
    print(" Too High! The number was:", secret_number)
else:
    print(" Too Low! The number was:", secret_number)