from audioop import mul


this_is_dictionary = {
    "days": 12,
    "conversion_unit": "m"
}

HOURS_MULTIPLIER = 60
MINUTES_MULTIPLIER = 3600
SECONDS_MULTIPLIER = 216000


def get_multiplier(conversion_unit):
    if conversion_unit == 'h':
        return HOURS_MULTIPLIER
    if conversion_unit == 'm':
        return MINUTES_MULTIPLIER
    if conversion_unit == 's':
        return SECONDS_MULTIPLIER

    raise ValueError("Unknown Converion Unit")


def convert_days(input_data):
    multiplier = get_multiplier(input_data["conversion_unit"])
    return input_data["days"] * multiplier


result = convert_days(this_is_dictionary)
print("Result:", result)
