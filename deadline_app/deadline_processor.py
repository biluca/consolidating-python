from datetime import datetime

DEFAULT_SEPARATOR = ":"
DEFAULT_DATE_FORMAT = "%d/%m/%Y"

print(f"The require format is: {DEFAULT_DATE_FORMAT} ")
print(f"Multiple values are separated by {DEFAULT_SEPARATOR} ")
user_input = input("Enter your Goal with a Deadline:")

user_input = user_input.split(DEFAULT_SEPARATOR)

goal = user_input[0]
deadline = user_input[1]

print(f"Your Goal is:", goal)
print(f"Your Deadline is:", deadline)

current_date = datetime.today()
deadline_date = datetime.strptime(deadline, DEFAULT_DATE_FORMAT)

countdown_date = deadline_date - current_date
if(countdown_date.days > 0):
    print(f"Dear User you have {countdown_date.days} days to reach your goal!")
else:
    print("Bazinga! Your time is Up!")
