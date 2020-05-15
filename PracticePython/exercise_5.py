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
from RANDOM import randrange

A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

UNIQUES = list(dict.fromkeys([single_element for single_element in A if single_element in B]))
print(UNIQUES)

# Extra 1 & 2

RANDOM = [sample for sample in range(randrange(0, 100))]
NEXT_RANDOM = [randrange(1, 100) for _ in range(0, 100)]

UNIQUES = list(dict.fromkeys([single_element for single_element in RANDOM if single_element in NEXT_RANDOM]))
print(UNIQUES)
