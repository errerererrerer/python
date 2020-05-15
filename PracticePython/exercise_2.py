"""
Exercise 2:
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides
   evenly into num, tell that to the user. If not, print a different appropriate message.

Script checking if given input is a digit and base on that deciding if first is a multiplication of 4, even or odd
number. Also checking if first and second dumber are divided equally and returning rounded division to 2 significant
digits. In case if provided data is containing unsupported char program will terminate and raise an TypeError.

 :param number1 int
 :param number2 int
 :return str
"""

NUMBER1 = input("Please provide a int number.\n")
NUMBER2 = input("Please provide a second int number.\n")

if NUMBER1.isdecimal() and NUMBER2.isdecimal():
    NUMBER1 = int(NUMBER1)
    NUMBER2 = int(NUMBER2)
    NUM = NUMBER1 / NUMBER2
    if NUMBER1 % 4 == 0:
        print("Chars are a mupliple of 4: {number}".format(number=NUMBER1))
    elif NUMBER1 % 2 == 0:
        print("Chars are an even number: {number}".format(number=NUMBER1))
    else:
        print("Chars are an odd number: {number}".format(number=NUMBER1))
    if NUMBER1 % NUMBER2 == 0:
        print("Chars1 and Chars2 are divided evenly: {division}".format(division=round(NUM, 2)))
    else:
        print("Chars1 and Chars2 are not divided evenly: {division}".format(division=round(NUM, 2)))
else:
    raise TypeError("Provided input is not a digit")
