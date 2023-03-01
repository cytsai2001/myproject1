# Q1
# input_list = [int(i) for i in input().split()]
# if len(input_list) % 2 == 1:
#     print(float(input_list[len(input_list) // 2]))
# else:
#     print(float(input_list[len(input_list) // 2 - 1] + input_list[len(input_list) // 2]) / 2)

# Q2
# input_list = [f'{i}' for i in input()]
#
#
# def operate(inputlist, outputlist):
#     for i in inputlist:
#         if i != '+' and i != '-' and i != '*':
#             outputlist.append(i)
#         elif i == '+':
#             if len(outputlist) != 0:
#                 outputlist.append(outputlist[-1])
#         elif i == '-':
#             if len(outputlist) != 0:
#                 outputlist.pop(-1)
#         elif i == '*':
#             if len(outputlist) != 0:
#                 outputlist += outputlist
#     return outputlist
#
#
# output_list = []
# output_result = operate(input_list, output_list)
# for i in output_result:
#     print(i, end='')

# Q3
#
# def hour_minute_sec_to_sec(time_string):
#     time_list = time_string.split(':')
#     time_sec = 0
#     time_sec += int(time_list[0]) * 3600
#     time_sec += int(time_list[1]) * 60
#     time_sec += int(time_list[2])
#     return time_sec
#
#
# def sec_to_hour_minute_sec(sec):
#     hour = sec // 3600
#     minute = (sec - 3600 * hour) // 60
#     second = (sec - 3600 * hour - 60 * minute)
#     if hour < 10:
#         hour_string = f'0{hour}'
#     else:
#         hour_string = f'{hour}'
#     if minute < 10:
#         minute_string = f'0{minute}'
#     else:
#         minute_string = f'{minute}'
#     if second < 10:
#         second_string = f'0{second}'
#     else:
#         second_string = f'{second}'
#     return f'{hour_string}:{minute_string}:{second_string}'
#
#
# month = input()
# if month == '4' or month == '6' or month == '9' or month == '11':
#     day = 30
# elif month == '2':
#     day = 28
# else:
#     day = 31
#
# dict_of_game = {}
# for i in range(day):
#     input_line = input().split(',')
#     if input_line[0] in dict_of_game.keys():
#         dict_of_game[input_line[0]] += hour_minute_sec_to_sec(input_line[1])
#     else:
#         dict_of_game[input_line[0]] = hour_minute_sec_to_sec(input_line[1])
#
# print(len(dict_of_game))
# print(sec_to_hour_minute_sec(sum(list(dict_of_game.values()))))

# Q4
# import datetime
#
# date_1 = [int(i) for i in input().split()]
# date_2 = [int(i) for i in input().split()]
# date_1_formatted = datetime.date(year=date_1[0], month=date_1[1], day=date_1[2])
# date_2_formatted = datetime.date(year=date_2[0], month=date_2[1], day=date_2[2])
# print(abs((date_1_formatted - date_2_formatted).days))

# Q5
import datetime
date_1 = [int(i) for i in input().split()]
delta_day = int(input())
date_1_formatted = datetime.date(year=date_1[0], month=date_1[1], day=date_1[2])
date_2_formatted = datetime.timedelta(days=delta_day)
print((date_1_formatted + date_2_formatted).isoformat())
