import random

print("--- ROCK PAPER SCISSORS GAME ---")
options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors (or type 'exit' to quit): ").lower()
    if user == "exit":
        print("Thanks for playing!")
        break

    if user not in options:
        print("Invalid choice.")
        continue

    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a draw!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
