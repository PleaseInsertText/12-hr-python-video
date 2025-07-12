def is_weekend(day):
    day = day.capitalize()
    match day:
        case "Saturday":
            return "It's the weekend! :)"
        case "Sunday":
            return ("Its the weekend!\n"
                    "but...\n"
                    "Sunday evenings are just depressing );")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday":
            return "It's a weekday :("
        case "Friday":
            return "Its a weekday but still a good day."
        case _:
            return "That is not a valid day :/"

print(is_weekend("friday"))