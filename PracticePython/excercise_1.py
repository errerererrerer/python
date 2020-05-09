"""
Simple script asking about first and last name and then printing it in the same order.
"""

sir_name = input("Pass your sir name, please\n")
first_name = input("Pass your first name please\n")

if sir_name.isalpha():
    if first_name.isalpha():
        print("Sir name: {sir_name}\nFirst name: {first_name}".format(sir_name=sir_name, first_name=first_name))
    else:
        raise TypeError("First Name content an unsupported char for a name: {first_name}".format(first_name=first_name))
else:
    raise TypeError("Sir Name content an unsupported char for a name: {sir_name}".format(sir_name=sir_name))