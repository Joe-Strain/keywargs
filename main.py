#!/usr/bin/env python3
"""
Short script to multiply any number of INTEGERS from the command line and return the total

Usage: python main.py a b c...
where a, b, c... are all integers

"""


import sys


def multiply(**kwargs):
    # set total to 1 outside the loops
    total = 1
    # iterate through the dictionary "kwargs"
    for key, value in kwargs.items():
        # iterate over the dictionary values
        for j in value:
            # only expects integer values from command line, use float otherwise
            total *= int(j)
    print(total)


# call multiply with kwargs set to a list from index 1 onwards
# index 0 is the file's name
if __name__ == '__main__':
    multiply(kwargs=sys.argv[1:])
