

import random


def get_winner(user, computer):

    if user == computer:
        return "tie"

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"

    else:
        return "computer"


def play_game():

    user_score = 0
    computer_score = 0
    ties = 0

    choices = ["rock", "paper", "scissors"]

    print("\n========== ROCK PAPER SCISSORS GAME ==========")

    while True:

        print("\nChoose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice = input("\nEnter your choice: ").lower().strip()

        if user_choice in ["1", "2", "3"]:
            user_choice = choices[int(user_choice) - 1]

        if user_choice not in choices:
            print("Invalid choice! Please select Rock, Paper or Scissors.")
            continue

        computer_choice = random.choice(choices)

        print("\nYour choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = get_winner(user_choice, computer_choice)

        if result == "tie":
            print("Result: It's a tie!")
            ties += 1

        elif result == "user":
            print("Result: You win!")
            user_score += 1

        else:
            print("Result: Computer wins!")
            computer_score += 1

        print("\n========== SCOREBOARD ==========")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        print("Ties:", ties)

        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()

        if play_again == "n":
            print("\n========== FINAL SCORE ==========")
            print("Your Score:", user_score)
            print("Computer Score:", computer_score)
            print("Ties:", ties)

            print("\nThanks for playing!")
            break

        elif play_again != "y":
            print("Invalid input! Exiting the game.")
            break


if __name__ == "__main__":
    play_game()

