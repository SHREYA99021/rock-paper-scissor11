"""Play a three-round Rock, Paper, Scissors match in the console.

Run normally for random computer choices:
    python rock_paper_scissors.py

Use --test to reproduce the specification's fixed choices (Scissors, Rock,
Paper) for the three rounds:
    python rock_paper_scissors.py --test
"""

import argparse
import random


CHOICES = ("rock", "paper", "scissors")
TEST_COMPUTER_CHOICES = ("scissors", "rock", "paper")
MATCH_ROUNDS = 3


def compare_choices(player_choice, computer_choice):
    """Return 'You win', 'Computer wins', or 'Draw' for a round."""
    if player_choice == computer_choice:
        return "Draw"

    winning_pairs = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
    if (player_choice, computer_choice) in winning_pairs:
        return "You win"
    return "Computer wins"


def get_player_choice(round_number):
    """Return a valid choice and whether an invalid entry was corrected."""
    corrected_invalid_entry = False
    while True:
        choice = input(
            f"Round {round_number} choice (rock, paper, or scissors): "
        ).strip().lower()
        if choice in CHOICES:
            return choice, corrected_invalid_entry
        print("Invalid choice. Enter rock, paper or scissors.")
        corrected_invalid_entry = True


def play_match(use_test_choices=False):
    """Play three rounds and print the round and match results."""
    wins = 0
    computer_wins = 0
    draws = 0
    round_results = []

    for round_number in range(1, MATCH_ROUNDS + 1):
        player_choice, corrected_invalid_entry = get_player_choice(round_number)
        if use_test_choices:
            computer_choice = TEST_COMPUTER_CHOICES[round_number - 1]
        else:
            computer_choice = random.choice(CHOICES)

        result = compare_choices(player_choice, computer_choice)
        round_line = f"Round {round_number}: {result}"
        if corrected_invalid_entry:
            round_line += " (no round lost)"
        round_results.append(round_line)

        if result == "You win":
            wins += 1
        elif result == "Computer wins":
            computer_wins += 1
        else:
            draws += 1

    print(" | ".join(round_results))
    print(f"You {wins} | Computer {computer_wins} | Draws {draws}")

    if wins > computer_wins:
        print("Result: You win the match!")
    elif computer_wins > wins:
        print("Result: Computer wins the match.")
    else:
        print("Result: Match drawn.")


def ask_play_again():
    """Return whether the player wants to start another match."""
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def main():
    parser = argparse.ArgumentParser(description="Play Rock, Paper, Scissors.")
    parser.add_argument(
        "--test",
        action="store_true",
        help="use the fixed computer choices Scissors, Rock, Paper",
    )
    args = parser.parse_args()

    while True:
        play_match(use_test_choices=args.test)
        if not ask_play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
