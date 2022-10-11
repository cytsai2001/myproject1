## moving average

number_of_period = int(input())
amount_of_numbers = int(input())
number = input().split()
number_list = []
for i in number:
    j = int(i)
    number_list.append(j)

moving_average_list = []
for i in range(number_of_period-1, len(number_list)):
    moving_average = (number_list[i-2] + number_list[i-1] + number_list[i])/3
    moving_average_list.append(moving_average)

print('moving average in float: ')
for i in moving_average_list:
    if moving_average_list.index(i) != len(moving_average_list) - 1:
        print(i, end=', ')
    elif moving_average_list.index(i) == len(moving_average_list) - 1:
        print(i, end='\n')

print('moving average in integer: ')
for i in moving_average_list:
    j = int(i)
    if moving_average_list.index(i) != len(moving_average_list) - 1:
        print(j, end=', ')
    elif moving_average_list.index(i) == len(moving_average_list) - 1:
        print(j, end='')
