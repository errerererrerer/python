"""
Exercise 1:
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells
them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the
   previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing
   the ENTER button)

Simple script asking about first and last name and then printing it in the same order.

 :param sir_name str
 :param first_name str
 :return str
"""

SIR_NAME = input("Pass your sir name, please\n")
FIRST_NAME = input("Pass your first name please\n")

if SIR_NAME.isalpha():
    if FIRST_NAME.isalpha():
        print("Sir name: {sir_name}\nFirst name: {first_name}".format(sir_name=SIR_NAME, first_name=FIRST_NAME))
    else:
        raise TypeError("First Name content an unsupported char for a name: {first_name}".format(first_name=FIRST_NAME))
else:
    raise TypeError("Sir Name content an unsupported char for a name: {sir_name}".format(sir_name=SIR_NAME))
