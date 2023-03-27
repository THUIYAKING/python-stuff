import random

print("Guess the number game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

number = random.randint(1, 100)
guesses = 0

while True:
    guess = input("Enter your guess: ")
    guesses += 1
    
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
