import string
input_int = int(input())


res = ''
dict_of_quotient = {}

n = 0
for i in string.ascii_uppercase:
    dict_of_quotient[n] = i
    n += 1
for j in string.ascii_lowercase:
    dict_of_quotient[n] = j
    n += 1

if input_int == 0:
    print('A')
else:
    while input_int != 0:
        res += dict_of_quotient.get(input_int % 52)
        input_int //= 52

    # res = res[::-1]
    # output
    print(res)
