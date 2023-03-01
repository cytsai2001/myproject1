def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


while True:
    try:
        n = int(input('please key in n'))
        k = int(input('please key in k'))
        if 0 < k < n:
            try:
                combination = factorial(n) // (factorial(k) * factorial(n - k))
                print(combination)
                break
            except RecursionError:
                print('please key in again w/ smaller numbers (recursion depth limitation encountered)')
        else:
            print('you must satisfy 0 < k < n')
    except ValueError:
        print('please key in integer')
