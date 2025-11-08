program_is_running = True

while program_is_running:

    user_input = input("Choose a file operation , type either ( Open , Delete , Rename , Exit) : ")

    match user_input.capitalize():
        case "Open":
            print("File opened")
        case "Delete":
            print("File deleted")
        case "Rename":
            print("File renamed")
        case "Exit":
            print("Exiting ... ")
            program_is_running = False
        case _:
            print("Operation not available")

