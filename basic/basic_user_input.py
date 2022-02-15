# I'm Asking your name:
input("What is your name? ")


# I'm Asking your Age and Printing it
your_age = input("How older are you? ")
print(f"Nice! You are {your_age} years old.")

# Now I'm reading your option, until you choose to exit

option = -1
while option != '0':
    print("If you type 0, the program will stop.")
    option = input("Please, type a number: ")