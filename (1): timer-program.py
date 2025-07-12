import time

duration = int(input("Enter the time in seconds: "))
x = duration #For compatibility between for and while loops.
line = ("---------------------------------------------------------"
        "----------------------------------------")
#This line thingy is just to save space
input(
    f"{line} \nThe time will be displayed in the format - "
    f"days:hours:minutes:seconds \nYou do not have to answer "
    f"this, just click enter once you are ready for the timer "
    f"to start. \n{line}")

for x in range(duration, 0, -1): #You can replace this line with: "while duration > 0:"
                                 #The original is "for x in range(duration, 0, -1):"

    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    days = int(x/86400)

    #x+=-1                     #<-------- Only used if the loop is a while loop.

    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)

print()
print("-------------------")
print("--- TIME IS UP! ---")
print("-------------------")
