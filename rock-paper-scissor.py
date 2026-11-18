"""A beginner-friendly three-round Rock, Paper, Scissors game."""

import random


choices = ["rock", "paper", "scissors"]
test_choices = ["scissors", "rock", "paper"]

# Leave this False for random computer choices. Set it to True to use the
# fixed choices from the project examples: scissors, rock, then paper.
use_test_choices = False


def find_winner(player_choice, computer_choice):
    """Compare two choices and return the winner of the round."""
    if player_choice == computer_choice:
        return "Draw"

    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win"

    return "Computer wins"


def play_game():
    """Play three rounds and show the match result."""
    player_wins = 0
    computer_wins = 0
    draws = 0
    round_results = []

    for round_number in range(1, 4):
        invalid_choice_entered = False

        # Keep asking for this round until the player enters a valid choice.
        while True:
            player_choice = input(
                f"Round {round_number} choice (rock, paper, or scissors): "
            ).strip().lower()

            if player_choice in choices:
                break

            print("Invalid choice. Enter rock, paper or scissors.")
            invalid_choice_entered = True

        if use_test_choices:
            computer_choice = test_choices[round_number - 1]
        else:
            computer_choice = random.choice(choices)

        winner = find_winner(player_choice, computer_choice)
        round_result = f"Round {round_number}: {winner}"
        if invalid_choice_entered:
            round_result += " (no round lost)"
        round_results.append(round_result)

        if winner == "You win":
            player_wins += 1
        elif winner == "Computer wins":
            computer_wins += 1
        else:
            draws += 1

    print(" | ".join(round_results))
    print(f"You {player_wins} | Computer {computer_wins} | Draws {draws}")

    if player_wins > computer_wins:
        print("Result: You win the match!")
    elif computer_wins > player_wins:
        print("Result: Computer wins the match.")
    else:
        print("Result: Match drawn.")


while True:
    play_game()

    play_again = input("Play again? (y/n): ").strip().lower()
    while play_again not in ["y", "n", "yes", "no"]:
        play_again = input("Please enter y or n: ").strip().lower()

    if play_again == "n" or play_again == "no":
        print("Thanks for playing!")
        break
