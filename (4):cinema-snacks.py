def cinema_snacks():

    import time

    from decimal import  Decimal
    #^Imports the only needed section (Decimal)
    #This is so the dont need to add 'decimal.' infront of 'Decimal(...)'

    menu = {"small popcorn": Decimal(3),
            "medium popcorn": Decimal(4.5),
            "large popcorn":Decimal(6),
            "fizzy drink": Decimal(0.5),
            "chocolate chip cookie": Decimal(1),
            "white chocolate chip cookie": Decimal(1),
            "slush": Decimal(2),
            "skittles": Decimal(0.7)}

    cart = []
    total = 0

    print("Welcome to the cinema, here is a selection of food and drink to enjoy with your movie!\n")
    print(" -------------------- MENU --------------------")
    for food, price in menu.items():
        print(f"| {food:30}: ${price:.2f}        |")
    print(" ----------------------------------------------")
    print("\nIf you want multiple of the same item, please enter it again.\n")
    while True:
        item = input("Which item would you like to buy? (Q to quit): ") .strip() .lower()
        if item.upper() == "Q":
            print("\nYou have ended the order.\n")
            break
        elif menu.get(item) is None:
            print("Sorry, we do not have that item or you have made a typo.")
            input("Click enter to start again: ")
            print("\n\n\n\n\n\n\n")
            cinema_snacks()
            break
        else:
            cart.append(item)

    print("------------------ YOUR ORDER ------------------")
    for items in cart:
        total += menu.get(items)
        print(f"- {items}")
    print(f"\nYour total is: ${total:.2f}")
    #There may be inaccuracies as decimal
    #as decimals may have problems being represented
    #in binary
    print("------------------------------------------------")
    input("PRESS ENTER TO PAY: ")
    print("\n~~~ PROCESSING ~~~")
    time.sleep(2)
    print("\nPAYMENT ACCEPTED! \nHere is your food, enjoy the movie!")

cinema_snacks()
