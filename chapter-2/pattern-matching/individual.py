program_is_running = True

while program_is_running:

    user_input = input("input a weekday e.g monday: ")

    match user_input.capitalize():
        case "Monday":
            print("Start project")
        case "Tuesday":
            print("Hold meeting")
        case "Wednesday":
            print("Group work")
        case "Thursday":
            print("Clean up")
        case "Friday":
            print("Submit report")
        case "Saturday":
            print("Chill")
        case "Sunday":
            print("Glory be to God")
        case _:
            print("Day not available")

