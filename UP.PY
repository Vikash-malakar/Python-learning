import random

print("Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ").lower()

print("Computer Chose:", computer)

if user == computer:
    print("Match Draw")

elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("You Win")

elif user in choices:
    print("Computer Wins")

else:
    print("Invalid Input")