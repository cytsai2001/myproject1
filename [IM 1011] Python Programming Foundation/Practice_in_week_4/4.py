import random
answer = random.sample(range(1, 10), 4)  # the four digits would be saved in a list.

guess = input()
guess_list = list(guess)
guess_list_of_number = []
for i in guess_list:
    j = int(i)
    guess_list_of_number.append(j)

A_count = 0
B_count = 0

while guess_list_of_number != answer:
    for i in guess_list_of_number:
        if i in answer:
            if guess_list_of_number.index(i) == answer.index(i):
                A_count += 1
            else:
                B_count += 1

    print(f'{A_count}' + 'A' + f'{B_count}' + 'B')
    guess = input()
    guess_list = list(guess)
    guess_list_of_number = []
    for i in guess_list:
        j = int(i)
        guess_list_of_number.append(j)

    A_count = 0
    B_count = 0

if guess_list_of_number == answer:
    print('Success!', end='')
