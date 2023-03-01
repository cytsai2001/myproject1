import random

month = 'october'
day = 10

random.seed(day)
for j in range(20):
    print(random.randint(0, 100), end=' ')
