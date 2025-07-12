import random

running = True

while running:

    options = ("rock", "paper", "scissors")
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice - (rock, paper, scissors): ") .strip() .lower()

        if player not in options:
            print("You have not entered a valid option.")
            result = None
            continue

        elif player == computer:
            result = "It's a tie!"

        elif player == "rock" and computer == "scissors":
            result = "You have won!"

        elif player == "scissors" and computer == "paper":
            result = "You have won!"

        elif player == "paper" and computer == "rock":
            result = "You have won!"

        else:
            result = "You have lost!"

        print(" -------- RESULTS -------- ")
        print(f"| Player: {player:<16}|")
        print(f"| Computer: {computer:<14}|")
        print("|                         |")
        print(f"| {result:<24}|")
        print(" ------------------------- ")

        play_again = input("Play again? (y/n (anything other than y is no)): ")
        print()
        if not play_again == "y":
            running = False

print("Thank you for playing!")


#< is used to align to left and > is for right, python auto aligns strings to left, but it is just better to include the symbol for consistency.
#For each case I have to define result to avoid errors.
