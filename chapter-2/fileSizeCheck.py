
file_size_checker_is_on = True


while file_size_checker_is_on:

    try:
        file_size = input("Input the size of the file or exit: ")
        if file_size.lower() == 'exit':
            print("exiting")
            file_size_checker_is_on = False
        elif int(file_size) <=0 :
            print("Invalid size")
        elif int(file_size) in range(1 , 101):
            print("File is small")
        elif int(file_size) in range(101 , 301):
            print("File is medium sized")
        else:
            print("File is too large")

    except ValueError:
        print("Input a number")