given_integer = int(input())

if given_integer == 1:
    print(4, 2, 1, sep=' ', end='')

while given_integer > 1:
    if given_integer % 2 == 1:
        given_integer *= 3
        given_integer += 1
        print(int(given_integer), end=' ')
    else:
        given_integer //= 2
        print(int(given_integer), end=' ')
