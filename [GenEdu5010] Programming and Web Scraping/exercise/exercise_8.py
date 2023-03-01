# # Q1
# def take_res(list_or_residual, int_input, int_n):
#     residual = int_input % int_n
#     if residual not in list_of_res:
#         list_or_residual.append(residual)
#     else:
#         residual += 1
#         take_res(list_or_residual, residual, int_n)
#
#
# n = int(input())
# list_of_int = [int(i) for i in input().split(',')]
# list_of_res = []
# for i in list_of_int:
#     take_res(list_of_res, i, n)
#
# for i in range(len(list_of_res) - 1):
#     print(f'{list_of_res[i]},', end='')
# print(list_of_res[-1])

# Q2
n = int(input())
dict_of_member = {}
for i in range(n):
    this_member_data = [int(i) for i in input().split()]
    if 1 <= this_member_data[3] <= 12:
        this_member_data.append(1)
    else:
        this_member_data.append(0)
    bmi = this_member_data[1] / ((this_member_data[0]/100) ** 2)
    this_member_data.append(round(bmi, 2))
    diff_of_height_and_weight = abs(this_member_data[0] - this_member_data[1])
    this_member_data.append(diff_of_height_and_weight)
    dict_of_member[i] = this_member_data

n = len(dict_of_member)
for i in range(n):
    already_sorted = True
    for j in range(n - i - 1):
        if dict_of_member.get(j)[4] > dict_of_member.get(j + 1)[4]:
            dict_of_member[j], dict_of_member[j + 1] = dict_of_member[j + 1], dict_of_member[j]
