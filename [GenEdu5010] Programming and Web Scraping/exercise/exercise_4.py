dream_list = []
i = input()
while i != 'end':
    dream_list.append(i.split(','))
    i = input()

sorted_dream_list = sorted(dream_list, key=lambda items: int(items[1]), reverse=False)

if len(sorted_dream_list) >= 3:
    for i in range(2):
        print(sorted_dream_list[i][0] + ' ' + sorted_dream_list[i][1], end='\n')
    print(sorted_dream_list[2][0] + ' ' + sorted_dream_list[2][1], end='')
elif len(sorted_dream_list) == 2:
    print(sorted_dream_list[0][0] + ' ' + sorted_dream_list[0][1], end='\n')
    print(sorted_dream_list[1][0] + ' ' + sorted_dream_list[1][1], end='')
elif len(sorted_dream_list) == 1:
    print(sorted_dream_list[0][0] + ' ' + sorted_dream_list[0][1], end='')
