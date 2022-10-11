from random import choice


def dice():
    return choice(range(1, 6, 1))


def gprint():
    print('This is printed from dice module.')
