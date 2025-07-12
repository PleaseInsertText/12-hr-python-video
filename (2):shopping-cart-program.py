import time

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (or enter q to quit): ")
    if food.lower().strip() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
time.sleep(0.2)
print("\n------- YOUR CART -------")
time.sleep(0.5)
if len(foods) == 0:
    print("THERE ARE NO ITEMS IN HERE")


else:
    print()
    print("Items:")
    for food in foods:
        print(f"- {food}")
    print()
    for price in prices:
        total += price
    time.sleep(0.5)
    print(f"The total cost will be: ${round(total,2)}")

    input("\n~~~~ PRESS ENTER TO PAY ~~~~")
    print("\nPROCESSING...")
    time.sleep(1)
    print("\nHere are you items, thank you for shopping here!")
