#!/usr/local/bin/python3

# Given an integer input, and a list of values
# find all the combinations in order to represent the input
# with different set of values
# E.g.
# input = 5
# result = 4 (5, 2+2+1, 2+1+1+1, 1+1+1+1+1)

import sys

Xp = int(sys.stdin.readline())
coins = list([1, 2, 5, 10, 50, 100, 200])

def combination(input, list):
    print(input, list)
    if not len(list) or input - list[0] < 0:
        return 0;
    if input - list[0] == 0:
        return 1

    return combination(input-list[0], list) + combination(input, list[1:len(list)])


print("Combinations: ")
print(combination(Xp, coins))