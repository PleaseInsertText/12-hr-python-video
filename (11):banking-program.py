import decimal
import time
from decimal import Decimal

def show_balance():
    global balance
    print(f"Your balance is: ${balance:.2f}\n\n\n")

def deposit():
    global balance
    amount = input("Enter an amount to be deposited: $")
    try:
        amount = Decimal(amount)
        rounded_amount = amount.quantize(Decimal("0.01"))

        if amount < 0:
            print("Amounts less than zero are not valid.")
            return

        elif amount != rounded_amount:
            print("Please enter only up to 2 decimal places.")
            return

        else:
            balance += amount

    except decimal.InvalidOperation:
        print("Invalid amount.\n\n\n")
        time.sleep(1)

def withdraw():
    global balance
    withdrawal = input("How much would you like to withdraw?: $")

    try:
        withdrawal = Decimal(withdrawal)
        rounded_withdrawal = withdrawal.quantize(Decimal("0.01"))

        if withdrawal < 0:
            print("Amounts less than zero are not valid.")
            return
        elif withdrawal != rounded_withdrawal:
            print("Please enter only up to 2 decimal places.")
            return
        elif balance - withdrawal < 0:
            print(f"\nInsufficient funds, the maximum "
                  f"amount you can withdraw is "
                  f"${balance:.2f}\n\n\n")
            time.sleep(1)
            return
        else:
            balance -= withdrawal

    except decimal.InvalidOperation:
        print("Invalid amount.\n\n\n")
        time.sleep(1)
        return

def main():
    is_running = True
    while is_running:

        print("----- BANKING PROGRAM -----")
        print()
        print("1: Show Balance            ")
        print("2: Deposit                 ")
        print("3: Withdraw                ")
        print("4: Exit                    ")
        print()

        choice = input("Enter your choice as a number: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Enter a valid option.\n\n\n")
        else:
            if choice == 1:
                show_balance()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                is_running = False
            else:
                print("Invalid choice")
                time.sleep(1)
                print("\n"*10)


balance = Decimal("0.00")
main()
