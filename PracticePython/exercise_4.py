"""
Exercise 4:
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you
don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26
because 26 / 13 has no remainder.)

Script checking what divisors input int have and print them out in a list.

:param data_input int
:return [int]
"""

data_input = input("Provide a int chars.\n")

if data_input.isdecimal():
    data_input = int(data_input)
    dividers = [divider for divider in range(1, data_input + 1) if data_input % divider == 0]
    print(dividers)
else:
    raise TypeError("Provided input is not a digit")
