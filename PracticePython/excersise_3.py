"""
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

# Extras 1
collection = []
for data in test_data:
    if data < 5:
        collection.append(data)
print(collection)

# Extras 2
collection = []
for data in test_data:
    if data < 5: collection.append(data)  # PEP8: E701 Error! Never write things like this
print(collection)

# Extras 3
data_input = input("Please provide at least 1 char containing digits")
collection = []
if data_input.isdecimal():
    for data in test_data:
        if data < data_input:
            collection.append(data)
    print(collection)
else:
    raise TypeError("Provided input is not a digit")