from threading import main_thread
from black import main


main_condition = True

while main_condition:
    input_value = input("Do you want to proceed? [y/n]: ")
    if(input_value == 'n'):
        main_condition = False
        print("Shuting down the program...")
    elif (input_value != 'y'):
        print("You've type a invalid answer...")
    else:
        print("Coninuing...")
