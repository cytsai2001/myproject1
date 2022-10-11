given_coordinate = input().split(' ')

sniper_x_coordinate_list = []
sniper_y_coordinate_list = []
for i in range(0, 6, 2):
    sniper_x_coordinate_list.append(int(given_coordinate[i]))
for i in range(1, 6, 2):
    sniper_y_coordinate_list.append(int(given_coordinate[i]))
sniper_coordinate_list = [[sniper_x_coordinate_list[0], sniper_y_coordinate_list[0]],
                          [sniper_x_coordinate_list[1], sniper_y_coordinate_list[1]],
                          [sniper_x_coordinate_list[2], sniper_y_coordinate_list[2]]]

coordinate_list = []
for i in range(0, 6):
    for j in range(0, 6):
        coordinate_list.append([i, j])

safe_x_list = []
safe_y_list = []
safe_diagonal_list = []
dangerous_diagonal_list = []
for i in range(0, 6):
    if i not in sniper_x_coordinate_list:
        safe_x_list.append(int(i))

for i in range(0, 6):
    if i not in sniper_y_coordinate_list:
        safe_y_list.append(int(i))

for [i, j] in coordinate_list:
    for [x, y] in sniper_coordinate_list:
        if abs(i - x) == abs(j - y):
            if [i, j] not in dangerous_diagonal_list:
                dangerous_diagonal_list.append([i, j])
            else:
                continue
    if [i, j] not in dangerous_diagonal_list:
        safe_diagonal_list.append([i, j])

safe_diagonal_list_copy = safe_diagonal_list.copy()

for [i, j] in safe_diagonal_list_copy:
    if i in safe_x_list:
        continue
    else:
        if [i, j] in safe_diagonal_list:
            index = safe_diagonal_list_copy.index([i, j])
            safe_diagonal_list.remove([i, j])
            safe_diagonal_list.insert(index, ['', ''])
        else:
            continue

for [i, j] in safe_diagonal_list_copy:
    if j in safe_y_list:
        continue
    else:
        if [i, j] in safe_diagonal_list:
            index = safe_diagonal_list_copy.index([i, j])
            safe_diagonal_list.remove([i, j])
            safe_diagonal_list.insert(index, ['', ''])
        else:
            continue

while ['', ''] in safe_diagonal_list:
    safe_diagonal_list.remove(['', ''])

for i in safe_diagonal_list:
    print(i)
