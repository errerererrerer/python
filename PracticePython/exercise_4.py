"""
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
