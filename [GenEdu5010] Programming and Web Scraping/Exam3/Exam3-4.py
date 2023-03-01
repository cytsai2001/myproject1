[n, m] = [int(i) for i in input().split()]
map_dict = {}
for i in range(m):
    map_dict[i] = list(input())

try:
    print('vertical hint')
    for i in range(m):
        count_pre = 0
        count = 0
        print_str = ''
        for j in range(len(map_dict[i])):
            if map_dict[i][j] == 'X':
                if j != 0:
                    if map_dict[i][j-1] == 'X':
                        count_pre += 1
                    elif map_dict[i][j-1] == 'O':
                        count_pre = 0
                count += 1
            elif map_dict[i][j] == 'O':
                if j != 0:
                    if map_dict[i][j-1] == 'X':
                        count_pre += 1
                        if print_str == '':
                            print_str += f'{count_pre}'
                        else:
                            print_str += f' {count_pre}'
                    elif map_dict[i][j-1] == 'O':
                        count_pre = 0
                count = 0
        if count != 0:
            if print_str != '':
                print_str += f' {count}'
            else:
                print_str += f'{count}'
            print(print_str)
        else:
            if print_str != '':
                print(print_str)
            else:
                print('\n', end='')

    print('horizontal hint')
    for i in range(n):
        count_pre = 0
        count = 0
        print_str = ''
        for j in range(m):
            if map_dict[j][i] == 'X':
                if j != 0:
                    if map_dict[j-1][i] == 'X':
                        count_pre += 1
                    elif map_dict[j-1][i] == 'O':
                        count_pre = 0
                count += 1
            elif map_dict[j][i] == 'O':
                if j != 0:
                    if map_dict[j-1][i] == 'X':
                        count_pre += 1
                        if print_str == '':
                            print_str += f'{count_pre}'
                        else:
                            print_str += f' {count_pre}'
                    elif map_dict[j-1][i] == 'O':
                        count_pre = 0
                count = 0
        if count != 0:
            if print_str != '':
                print_str += f' {count}'
            else:
                print_str += f'{count}'
            print(print_str)
        else:
            if print_str != '':
                print(print_str)
            else:
                print('\n', end='')
except:
    print('\n', end='')

