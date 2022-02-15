# GLOBAL Variables
total_days_in_year = 365
year_animal = "Tiger"


def scope_check_globals():
    # This function uses Global Variabels on its Logic
    print(f"This year, is the year of the {year_animal}")
    print(f"This year, we'll have {total_days_in_year} days in total")


scope_check_globals()


def scope_check_function():
    # This function only uses Local Variables on its Logic
    total_persons = 77
    square_meters = 100
    people_density = square_meters/total_persons

    print(people_density)


scope_check_function()


def scope_check_globals_function(year_animal):
    # This function uses Global & Local Variables on it Logics
    # Notice that the variable <year_animal> its duplicate here
    # In this case, the local variable will be used over the global one

    # This function uses Global Variabels on its Logic
    print(f"This year, is the year of the {year_animal}")
    print(f"This year, we'll have {total_days_in_year} days in total")


scope_check_globals_function("Dragon")
