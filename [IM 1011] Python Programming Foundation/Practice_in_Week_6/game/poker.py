from random import choice


def poker():
    color = ['C', 'T', 'H', '']
    number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    random_card = choice(color) + choice(number)
    return random_card


def gprint():
    print('This is printed from poker module.')
