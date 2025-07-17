import random
import time

recharges = 3
balance = 100

def recharge():
    global recharges

    print("Welcome to the number guessing game!\n")
    number = random.randint(1, 15)
    guesses = 0
    is_running = True

    while is_running:
        guess = int(input("Guess the number between 1 and 15: "))
        guesses += 1

        if guesses > 5:
            print("Sorry, you reached the max of 5 guesses. "
                  "You have to restart the number guessing game.")
            time.sleep(2)
            return  # Just exit back to balance_check loop

        if guess == number:
            print("\nYou guessed correctly!")
            recharges += 1
            is_running = False
        elif guess > 15 or guess < 1:
            print("\nError - Out of range. Try again.")
        else:
            print(f"Try again, {guess} was not correct.")

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "🌟"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "🍒": return bet * 2
            case "🍉": return bet * 3
            case "🍋": return bet * 4
            case "🔔": return bet * 5
            case "🌟": return bet * 6
    return 0

def main():
    global balance
    global recharges

    print("***********************")
    print("Welcome to Python Slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 🌟")
    print("***********************")

    while True:  # Infinite game loop
        while balance > 0:
            print(f"Your current balance is ${balance}")
            bet = input("Enter your bet amount (integers only): $")

            if not bet.isdigit():
                print("Please enter a valid number")
                continue

            bet = int(bet)

            if bet > balance:
                print("Insufficient funds")
                continue

            if bet <= 0:
                print("Bet must be greater than 0")
                continue

            balance -= bet

            row = spin_row()
            print("\nSpinning... \n")
            print_row(row)

            payout = get_payout(row, bet)

            if payout > 0:
                print(f"You won ${payout}!\n\n\n")
                balance += payout
            else:
                print(f"You lost :( \nYour balance is ${balance}\n\n\n")

        # Balance is 0, handle recharges
        while balance == 0:
            print(f"You're out of balance. Charges remaining: {recharges}")
            spend_charge = input("Would you like to spend 1 charge to top up your balance by 100? (Y/N) ")

            match spend_charge.upper():
                case "Y":
                    if recharges > 0:
                        recharges -= 1
                        balance += 100
                        print("Recharge successful!\n")
                        break  # Go back to betting loop
                    else:
                        minigame_choice = input("No charges left. \nDo you want to play a minigame to earn more? (Y/N) ")
                        match minigame_choice.upper():
                            case "Y":
                                recharge()
                            case "N":
                                print("Ok, waiting...")
                                time.sleep(2)
                            case _:
                                print("Invalid input.")
                case "N":
                    print("Ok, waiting...")
                    time.sleep(2)
                case _:
                    print("Invalid input.")

if __name__ == "__main__":
    main()
