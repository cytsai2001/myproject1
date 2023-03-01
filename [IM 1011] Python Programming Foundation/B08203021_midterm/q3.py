import random


random.seed(2028)
random_int_list = [random.randint(0, 200) for i in range(100)]
sample_function_list = random.sample(range(201), k=100) # should be range(201)

in_two_list = []
count = 0
for i in random_int_list:
    if i in sample_function_list:
        count += 1
        index_of_i = random_int_list.index(i)
        random_int_list.remove(i)
        random_int_list.insert(index_of_i, '')
        if i not in in_two_list:
            in_two_list.append(i)

if len(in_two_list) == 0:
    print('all are different')
else:
    print(count)
