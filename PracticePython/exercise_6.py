"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads
the same forwards and backwards.)

Script is checking if provided input is ascii compatible and if this string is a palindrome. As a output proper
message is printed out.

:return str
"""

data_input = input("Provide a string of chars\n")
if data_input.isascii():
    if data_input == data_input[::-1]:
        print("{data_input} is a pure palindrome\n{data_input_palindrome}".format(
            data_input=data_input, data_input_palindrome=data_input[::-1]))
    elif data_input.upper() == data_input.upper()[::-1]:
        print("{data_input} is a palindrome if CamelCase is ignored\n{data_input_palindrome}".format(
            data_input=data_input, data_input_palindrome=data_input.upper()[::-1]))
    else:
        print("{data_input} is not a palindrome".format(data_input=data_input))
else:
    raise TypeError("Use only Ascii chars: {data_input}".format(data_input=data_input))
