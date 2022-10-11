input_list = input().split(' ')

integer_list = []
for i in input_list:
    j = int(i)
    integer_list.append(j)

integer_list.remove(integer_list[0])

print(max(integer_list), sum(integer_list), sep=', ', end='')
