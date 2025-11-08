loop_is_on = True

while loop_is_on:
    #Ask user for an input
    user_input = input("Input a number : ")
    #check if number is less than zero
    try:
        if int(user_input) <= 0 :
            #if true stop the loop
            print(f"You inputted a negative number : {user_input}")
            loop_is_on = False
        else:
            #else print the number
            print(int(user_input))
    except ValueError:
        print("Input a number")