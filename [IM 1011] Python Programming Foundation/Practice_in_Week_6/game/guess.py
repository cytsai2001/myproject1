import random

status = ['scissors', 'stone', 'paper']


def figure_guess():
    return random.choice(status)


def guess_print():
    print('This is printed from guess_print.')
