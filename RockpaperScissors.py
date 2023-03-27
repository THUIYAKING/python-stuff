import random

def play_game(rounds):
    # possible choices
    choices = ["rock", "paper", "scissors"]

    #  initial score
    user_score = 0
    computer_score = 0

    # Play the  number of rounds
    for i in range(rounds):
        print("Round", i+1)

        # user's choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        #  computer's choice
        computer_choice = random.choice(choices)

        # Print the choices
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        # Determine the winner and update the score
        if user_choice == computer_choice:
            print("It's a tie!")
        elif ((user_choice == "rock" and computer_choice == "scissors")
                or (user_choice == "paper" and computer_choice == "rock")
                or (user_choice == "scissors" and computer_choice == "paper")):
            print("You win the round!")
            user_score += 1
        else:
            print("Computer wins the round!")
            computer_score += 1

        # Check if a player has won the game and declare the winner
        if user_score >= rounds//2+1:
            print("Congratulations, you win the game!")
            return
        elif computer_score >= rounds//2+1:
            print("Sorry, You lost.")
            return

    # Print the final score and declare the winner
    print("Final score:")
    print("You:", user_score)
    print("Computer:", computer_score)
    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")

# Play a game with 5 rounds
play_game(5)

