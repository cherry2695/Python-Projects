import random

print("\n--- Welcome to the Rock-Paper-Scissors Game ---\n")

options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ").lower().strip()

    print(f"\nPlayer    : {player}")
    print(f"Computer  : {computer}\n")

    # Game logic
    if player == computer:
        print("Result    : It's a tie!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("Result    : Congratulations! You won the game.")
    else:
        print("Result    : You lost the game.")

    print("\n---------------------------------------------")

    play_again = input("Do you want to play again? (y/n): ").lower().strip()
    if play_again != 'y':
        playing = False

print("\nThanks for playing! See you next time.")