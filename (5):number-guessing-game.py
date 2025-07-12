import random

print("Welcome to the number guessing game!\n")
lowest = int(input("What would you like the lowest number to be? (ENTER A WHOLE NUMBER): "))
highest = int(input("What is the largest number? (ENTER A WHOLE NUMBER): "))
number = random.randint(lowest, highest)
increment = input("If you guess the wrong number, "
                  "would you like to get a hint? (y/n): ") .lower() .strip()
guesses = 0
is_running = True

if increment.startswith("y"):
    while is_running:
        guess = int(input(f"Guess the number between {lowest} and {highest}: "))
        guesses += 1
        if guess == number:
            print("\nYou guessed correctly!")
            is_running = False
        elif guess > highest or guess < lowest:
            print("\nError - You went outside of the range of numbers, try again.")
        else:
            print(f"Try again, {guess} was not the correct answer.")

            range_size = highest - lowest
            step = max(1, range_size // 10)

            if guess < number:
                lowest = max(lowest, min(guess + step, number))
            else:
                highest = min(highest, max(guess - step, number))


else:
    while is_running:
        guess = int(input(f"Guess the number between {lowest} and {highest}: "))
        guesses += 1
        if guess == number:
            print("\nYou guessed correctly!")
            is_running = False
        elif guess > highest or guess < lowest:
            print("\nError - You went outside of the range of numbers, try again.")
        else:
            print(f"Try again, {guess} was not the correct answer.")