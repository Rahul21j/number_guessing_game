import random

number = random.randint(1, 10)
guessLimit = 3
i = 1

while i <= guessLimit:
    user = int(input("Guess the number: "))
    if user == number:
        print(f"The number you guessed was correct: {number}")
        break
    else:
        if i == guessLimit:
            print(f"You are out of guesses. The number was: {number}")
        else:
            pass
    i += 1
