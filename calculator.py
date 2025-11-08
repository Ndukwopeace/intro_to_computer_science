welcome_text= r"""                                                                                                    
 _ _ _     _                      _                  _         _     _                    ___   ___ 
| | | |___| |___ ___ _____ ___   | |_ ___    ___ ___| |___ _ _| |___| |_ ___ ___      _ _|_  | |   |
| | | | -_| |  _| . |     | -_|  |  _| . |  |  _| .'| |  _| | | | .'|  _| . |  _|    | | |  _|_| | |
|_____|___|_|___|___|_|_|_|___|  |_| |___|  |___|__,|_|___|___|_|__,|_| |___|_|       \_/|___|_|___|
                                                                                                    """
print(welcome_text)
valid_operations = ["+" , "-" , "/" , "*"]
result = 0

calculator_is_on = True
#Addition
def addition(num1 , num2):
    return num1 + num2

#Substraction
def substraction(num1 , num2):
    return num1 - num2

#Multiplication
def multiplication(num1 , num2):
    return num1 * num2

#Division
def division(num1 , num2):
    return num1 / num2

while calculator_is_on:
    # Ask user to choose operation either + , - , * or /
    user_input = input(f"Choose an operation : {valid_operations}")
    if user_input == "exit".lower():
        calculator_is_on = False
    elif user_input in valid_operations or user_input == "exit".lower():
        try:
            first_number = int(input("Input the first number: "))
            second_number = int(input("Input second number:"))
            if user_input == "+":
                result = addition(num1= first_number , num2=second_number)
                print(f"result: {first_number} + {second_number} = {result}")
            elif user_input == "-":
                result = substraction(num1= first_number , num2=second_number)
                print(f"result: {first_number} - {second_number} = {result}")
            elif user_input == "/":
                result = division(num1= first_number , num2=second_number)
                print(f"result: {first_number} / {second_number} = {result}")
            elif user_input == "*":
                result = multiplication(num1= first_number , num2=second_number)
                print(f"result: {first_number} * {second_number} = {result}")
        except ValueError :
        #If the input is not a number print an error
            print("The input must be a number")
        except ZeroDivisionError:
        #If it is division be zero
            print("Zero division error ; Cannot divide by zero")
    else:
        print("Invalid operation , try again")

