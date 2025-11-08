tester_is_on = True

Welcome_text = "WELCOME TO CODE TESTER "

print(Welcome_text)

actual_result = 0

num_array = []

unwanted_operations = ["*" , "-" , "/"]
while tester_is_on:

    my_input = input("Test for addition: ")
    if "+" in my_input and not any(op in my_input for op in unwanted_operations):
        num_array = my_input.split("+")
        try:
            expected_result = int(input("What is your expected result: "))
            for num in num_array:
                actual_result += int(num)

            if actual_result == expected_result:
                print(f"Test Successful!!!:\nYour operation : {my_input}\n"
                      f"Your expected result = {expected_result}\n"
                      f"The actual result = {actual_result}")
            else:
                print(f"Test failed!!!:\nYour operation : {my_input}\n"
                      f"Your expected result = {expected_result} \n"
                      f"The actual result = {actual_result}")

        except ValueError:
            print("Input numbers")
    else:
        print("Invalid input")





