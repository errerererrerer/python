"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads
the same forwards and backwards.)

Script is checking if provided input is ascii compatible and if this string is a palindrome. As a output proper
message is printed out.

:return str
"""

DATA_INPUT = input("Provide a string of chars\n")
if DATA_INPUT.isascii():
    if DATA_INPUT == DATA_INPUT[::-1]:
        print("{data_input} is a pure palindrome\n{data_input_palindrome}".format(
            data_input=DATA_INPUT, data_input_palindrome=DATA_INPUT[::-1]))
    elif DATA_INPUT.upper() == DATA_INPUT.upper()[::-1]:
        print("{data_input} is a palindrome if CamelCase is ignored\n{data_input_palindrome}".format(
            data_input=DATA_INPUT, data_input_palindrome=DATA_INPUT.upper()[::-1]))
    else:
        print("{data_input} is not a palindrome".format(data_input=DATA_INPUT))
else:
    raise TypeError("Use only Ascii chars: {data_input}".format(data_input=DATA_INPUT))
