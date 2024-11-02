import random

def play_game():
    # Options for the game
    options = ["rock", "paper", "scissors"]
    
    # Get the player's choice
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    # Validate the player's choice
    if player_choice not in options:
        print("Invalid choice, please choose rock, paper, or scissors.")
        return

    # Generate the computer's choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
play_game()
