# assume the user always key in proper numbers
x = int(input('please key in x'))
y = int(input('please key in y'))

for i in range(y - 1):
    if x % 2 == 1:
        x = x * 5 - 3
    else:
        x = x // 2 + 1

print(x)
