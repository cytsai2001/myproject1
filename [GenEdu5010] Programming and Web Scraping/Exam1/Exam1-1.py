input_1 = input()
input_2 = input()
input_3 = input()

drink_day_1 = [input_1[0:1], input_1[1:]]
drink_day_2 = [input_2[0:1], input_2[1:]]
drink_day_3 = [input_3[0:1], input_3[1:]]

drink_list = [drink_day_1, drink_day_2, drink_day_3]
caffeine = [0, 0, 0]
sugar = [0, 0, 0]
count = 0

for i in drink_list:
    if i[0] == 'B':
        caffeine[count] += 50 * int(i[1])
        sugar[count] += 10 * int(i[1])
    if i[0] == 'M':
        caffeine[count] += 20 * int(i[1])
        sugar[count] += 30 * int(i[1])
    count += 1
if (sum(caffeine) > 700) or (sum(sugar) > 150) or (max(caffeine) > 300) or (max(sugar) > 60):
    print('不可', end='')
else:
    print('可', end='')


