import random

def get_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'scissors' and player2 == 'paper') or \
         (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        player1_choice = input("Player 1, enter your choice (rock, paper, scissors): ").lower()
        if player1_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue
        
        player2_choice = input("Player 2, enter your choice (rock, paper, scissors): ").lower()
        if player2_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        print(f"\nPlayer 1 chose: {player1_choice}")
        print(f"Player 2 chose: {player2_choice}")

        result = get_winner(player1_choice, player2_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

play_rock_paper_scissors()
