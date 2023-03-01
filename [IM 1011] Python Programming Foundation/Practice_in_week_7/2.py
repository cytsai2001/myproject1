import random


to_be_written_file = open('q2.txt', 'w', encoding='utf-8')
month = 'october'
day = 10

random.seed(day)
for j in range(20):
    if j == 19:
        print(random.randint(0, 100), end='', file=to_be_written_file)
    else:
        print(random.randint(0, 100), end=' ', file=to_be_written_file)
to_be_written_file.close()

read_the_text = open('q2.txt', 'r', encoding='utf-8')
read_data_list = [int(i) for i in read_the_text.readline().split(' ')]
read_the_text.close()


def mean(list_of_input):
    sum_of_items = 0
    for i in list_of_input:
        sum_of_items += i
    return sum_of_items / len(list_of_input)


# ddof means Delta Degrees of Freedom, same as numpy.std
def std_dev(list_of_input, mean_of_data, ddof=1):
    sum_of_square = 0
    for i in list_of_input:
        sum_of_square += (i ** 2)
    standard_deviation = ((sum_of_square - ((mean_of_data ** 2) * len(list_of_input))) / (len(list_of_input) - ddof)) ** (1/2)
    return standard_deviation


mean = mean(read_data_list)
sd = std_dev(read_data_list, mean)
print(f'mean = {mean}, sd = {sd}')

greater_or_not = ''
if sd > day:
    greater_or_not = 'True'
else:
    greater_or_not = 'False'
write_the_data = open('q2.txt', 'a', encoding='utf-8')
print(f'\nmean = {mean}, sd = {sd}', file=write_the_data)
write_the_data.writelines(greater_or_not)
write_the_data.close()
