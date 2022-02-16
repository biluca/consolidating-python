your_name = input("What is your Name? ")


def validate_your_name(name):
    try:
        if len(name) > 8:
            raise ValueError
        else:
            print("You're good to go")
    except:
        print("Your name is too big to remember")


validate_your_name(your_name)
