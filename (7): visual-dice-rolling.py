import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘       (from line above)
# The "|" on some keyboards is not the same as "│" from that list.

dice_thingy = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

dice = []
total = 0
just_used_to_loop_xd = True #Can be any random variable for the while loop.
num_of_dice = 0

while just_used_to_loop_xd:
    num_of_dice = input("How many dice do you want to roll? ")
    if num_of_dice.isdigit():
        num_of_dice = int(num_of_dice)
        just_used_to_loop_xd = False
    else:
        print("\nPlease enter a valid number.")

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))


for line in range(5):
    for die in dice:
        print(dice_thingy.get(die)[line], end = "")
    print()


for die in dice:
    total += die
print(f"Total = {total}")