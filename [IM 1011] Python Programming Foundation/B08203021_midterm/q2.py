def adjustment(score):
    return int(score * ((2028 / 100) ** (1/20)))


print('Original\tAdjusted')
for i in range(0, 101):
    if adjustment(i) < 100:
        print(f'{i}\t{adjustment(i)}')
    else:
        print(f'{i}\t{100}')
