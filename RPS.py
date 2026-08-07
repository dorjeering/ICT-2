import random

# Function to determine winner
def check_winner(user, computer):
    if user == computer:
        return "It's a Tie!"

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You Win!"

    else:
        return "Computer Wins!"

print("===================================")
print("      ROCK PAPER SCISSORS")
print("===================================")

name = input("Enter Your Name: ")

choices = ["rock", "paper", "scissors"]  # List

while True:  # Loop

    user_choice = input("\nChoose Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:  # Conditional
        print("Invalid Choice! Try Again.")
        continue

    computer_choice = random.choice(choices)

    print("Your Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    result = check_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("===================================")
print("Thank You For Playing,", name)
print("===================================")