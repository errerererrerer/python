"""
Exercise 3:
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in
   it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller
   than that number given by the user.

Main script searching inside of hardcoded list containing ints for elements less or more then 5 and then print them out.
Output is in form of a single int or [ints] fulfilling base requirement. Input data is used for creating list of items
that are less then typed int.

:param data_input int
:return int, [int]
"""

test_data = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Main
for data in test_data:
    if data > 5:
        print(data)

# Extras 1 & 2
collection = [data for data in test_data if data < 5]
print(collection)

# Extras 3
data_input = input("Please provide at least 1 char containing digits\n")
if data_input.isdecimal():
    collection = [data for data in test_data if data < int(data_input)]
    print(collection)
else:
    raise TypeError("Provided input is not a digit")
