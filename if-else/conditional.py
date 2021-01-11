def is_positive(num):
    if num > 0:
        print(True)
    else:
        print(False)


is_positive(1)


def is_even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)


is_even(2)


def is_positive_and_even(num):
    if num > 0 and num % 2 == 0:
        print(True)
    else:
        print(False)


is_positive_and_even(4)


def is_positive_or_even(num):
    if num > 0 or num % 2 == 0:
        print(True)
    else:
        print(False)


is_positive_or_even(4)