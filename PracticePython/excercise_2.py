"""
Script checking if given input is a digit and base on that deciding if first is a multiplication of 4, even or odd
number. Also checking if first and second dumber are divided equally and returning rounded division to 2 significant
digits. In case if provided data is containing unsupported char program will terminate and raise an TypeError.

 :param number1 int
 :param number2 int
 :return str
"""

number1 = input("Please provide a int number.\n")
number2 = input("Please provide a second int number.\n")

if number1.isdecimal() and number2.isdecimal():
    number1 = int(number1)
    number2 = int(number2)
    num = number1 / number2
    if number1 % 4 == 0:
        print("Chars are a mupliple of 4: {number}".format(number=number1))
    elif number1 % 2 == 0:
        print("Chars are an even number: {number}".format(number=number1))
    else:
        print("Chars are an odd number: {number}".format(number=number1))
    if number1 % number2 == 0:
        print("Chars1 and Chars2 are divided evenly: {division}".format(division=round(num, 2)))
    else:
        print("Chars1 and Chars2 are not divided evenly: {division}".format(division=round(num, 2)))
else:
    raise TypeError("Provided input is not a digit")
