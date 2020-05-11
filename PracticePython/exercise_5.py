"""
Exercise 5:
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without
duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

Scripts comparing two lists static and two randomize list in range of <0, 100> and looking for unique elements in
both lists.

:return [int]
"""
from random import randrange

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

uniques = list(dict.fromkeys([single_element for single_element in a if single_element in b]))
print(uniques)

# Extra 1 & 2

random = [sample for sample in range(randrange(0, 100))]
next_random= [randrange(1, 100) for _ in range(0, 100)]

uniques = list(dict.fromkeys([single_element for single_element in random if single_element in next_random]))
print(uniques)