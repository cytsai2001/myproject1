# list_of_input = input().split(' ')
# list_of_dictionary = []
# for i in list_of_input:
#     list_of_dictionary.append(i.split(','))
# dictionary = {i[0]: i[1] for i in list_of_dictionary}
#
# input_letter = input()
# if input_letter in dictionary.keys():
#     print(dictionary.get(input_letter))
# else:
#     print('單字不存在')


# list_of_input = input().split(' ')
# list_of_dictionary = [i.split(',') for i in list_of_input]
# dictionary_of_idle = {i[0]: [i[1], i[2]] for i in list_of_dictionary}
#
# input_idle = input()
# print(dictionary_of_idle.get(input_idle))


# n = int(input())
# sentence = []
# for i in range(n):
#     sentence.append(input().split())
#
# d = {}
#
# for i in sentence:
#     for word in i:
#         if word not in d:
#             d.update({word: 1})
#         else:
#             d[f'{word}'] += 1
#
# print(d)

# num_input = int(input())
#
#
# def ugly_or_not(integer):
#     if integer / 2 == integer // 2:
#         integer /= 2
#         ugly_or_not(integer)
#     else:
#         if integer / 3 == integer // 3:
#             integer /= 3
#             ugly_or_not(integer)
#         else:
#             if integer / 5 == integer // 5:
#                 integer /= 5
#                 ugly_or_not(integer)
#             else:
#                 if integer == 1:
#                     print(True)
#                 else:
#                     print(False)
#
#
# ugly_or_not(num_input)


num_input = int(input())


def counting(integer):
    for i in range(1, integer + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                print('拍手拍頭')
            else:
                print('拍手')
        elif i % 5 == 0:
            print('拍頭')
        else:
            print(i)


counting(num_input)
