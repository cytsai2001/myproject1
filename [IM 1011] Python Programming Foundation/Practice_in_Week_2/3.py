x = input('Please type an integer between 0 to 100.')
if f'{int(float(x))}' != x:
    print(int(float(x)))
else:
    x = int(float(x))
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print('Whoops')

