import random
number = random.randint(1, 100)
num_guesses = 0
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    num_guesses += 1
    if guess == number:
        print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
        break
    if guess < number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")
