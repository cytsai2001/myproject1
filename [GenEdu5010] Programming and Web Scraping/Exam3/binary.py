# input
n = int(input())

# transform
res = ''
while n != 0:
    if n % 2 == 1:
        res += '1'
    else:
        res += '0'
    n //= 2

res = res[::-1]
# output
print(res)
