# I'm Asking your Age and Printing it
your_age = input("How older are you? ")
print(f"Nice! You are {your_age} years old.")

you_can_drink_age = 21

if (int(your_age) >= you_can_drink_age):
    print("Let's get a Drink?")
else:
    print("Let's get a Cup of Coffee?")

print()


# Rock, Paper & Scissors and you'll never win
your_choise = input("Rock, Paper, Scissors: ")

if (your_choise == 'rock'):
    print('I choose Paper! I win!')
elif (your_choise == 'paper'):
    print('I choose Scissors! I win!')
else:
    print('I choose Rock! I win!')