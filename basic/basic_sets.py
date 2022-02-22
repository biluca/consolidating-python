# Set is another Built-in data type of Python
# Similar to lists, is used to store multiples item
# Has the unique feature that does not allow duplicate values

list_of_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
set_of_numbers = set(list_of_numbers)

print(set_of_numbers)

list_of_names = ["Joe", "Jolene", "Jasper", "Joe"]
set_of_names = set(list_of_names)

print(set_of_names)

# You can see on the Printed Outputs that the
# duplicated values are ignored when a list is
# converted into a set

set_of_letters = {'a', 'b', 'c'}

# Sets aren't ordered and/or indexed
# which means that you can't access individual elements
# but we can add & remove elements...

set_of_letters.add('x')
set_of_letters.add('y')
set_of_letters.remove('x')


for letter in set_of_letters:
    print(f"{letter}::{ord(letter)}")