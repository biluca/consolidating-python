# Functions

# Functions are used to encaspsulate a piece of logic
# in order to make it reusable avoiding code repetition

def day_to_miliseconds(total_days):
    hours_per_day = 24
    minutes_per_hour = 60
    seconds_per_minute = 60
    miliseconds_per_second = 100

    total_minutes_on_days = total_days * hours_per_day * \
        minutes_per_hour * seconds_per_minute * miliseconds_per_second
    return total_minutes_on_days


day_to_miliseconds_value = day_to_miliseconds(59)
print(day_to_miliseconds_value)


def day_to_hours(total_days=10):  # Right here I'm passing a default value for the Parameter
    hours_per_day = 24

    total_hours_on_days = total_days * hours_per_day
    return total_hours_on_days


day_to_hours_value = day_to_hours()
print(day_to_hours_value)


def counting_numbers(number_a, number_b, number_c):
    return f"Hey, I'm printing {number_a}, {number_b}, {number_c} numbers"


print(counting_numbers(1, 2, 5))
