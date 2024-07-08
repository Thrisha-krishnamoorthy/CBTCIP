def get_feedback(secret, guess):
    correct_positions = sum(s == g for s, g in zip(secret, guess))
    correct_numbers = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - correct_positions
    return correct_positions, correct_numbers

def player_guess(secret):
    attempts = 0
    while True:
        guess = input("Enter your guess: ")
        attempts += 1
        if guess == secret:
            print(f"Congratulations! You guessed the number {secret} in {attempts} tries.")
            return attempts
        correct_positions, correct_numbers = get_feedback(secret, guess)
        print(f"Correct digits in correct positions: {correct_positions}")
        print(f"Correct digits in incorrect positions: {correct_numbers}")

def play_mastermind():
    print("Welcome to Mastermind! game")
    
    
    print("Player 1, enter a multi-digit number for Player 2 to guess:")
    player1_number = input().strip()
    
    print("\nPlayer 2, try to guess the number set by Player 1:")
    player2_attempts = player_guess(player1_number)
    
    
    print("\nPlayer 2, set a multi-digit number for Player 1 to guess:")
    player2_number = input().strip()
    
    print("\nPlayer 1, try to guess the number set by Player 2:")
    player1_attempts = player_guess(player2_number)
    
    
    if player1_attempts < player2_attempts:
        print(f"\nPlayer 1 wins the game and is crowned Mastermind with {player1_attempts} tries!")
    else:
        print(f"\nPlayer 2 wins the game and is crowned Mastermind with {player2_attempts} tries!")

play_mastermind()
