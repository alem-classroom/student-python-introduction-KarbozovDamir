import random

def is_positive(num):
    if num > 0:
        print(True)
    else:
        print(False)


is_positive(1) # return true if num is positive, otherwise return false

def is_even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)


is_even(2) # return true if num is even, otherwise return false


def is_positive_and_even(num):
    if num > 0 and num % 2 ==0:
        print(True)
    else:
        print(False)


is_ positive_or_even(4) # return true if num is positive and even, otherwise return false


def is_positive_or_even(num):
    if num > 0 or num % 2 == 0:
        print(True)
    else:
        print(False)


is_positive_or_even(4)
    # return true if num is positive or even, otherwise return false
