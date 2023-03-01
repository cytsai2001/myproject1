[total_column, total_row] = [int(i) for i in input().split()]
list_of_maze = []
for i in range(total_row):
    list_of_maze.append(list(input()))


def get_coordinate(wanted_str):
    wanted_coordinate = []
    for i in list_of_maze:
        for j in range(len(i)):
            if wanted_str == i[j]:
                wanted_coordinate.append([list_of_maze.index(i), j])
    return wanted_coordinate


def near_or_not(list_of_coor1, list_of_coor2):
    if list_of_coor1[0] == list_of_coor2[0]:
        if abs(list_of_coor1[1] - list_of_coor2[1]) == 1:
            return True
        else:
            return False
    elif abs(list_of_coor1[0] - list_of_coor2[0]) == 1:
        if list_of_coor1[1] == list_of_coor2[1]:
            return True
        else:
            return False
    else:
        return False


start_coordinate = get_coordinate('S')
end_coordinate = get_coordinate('G')
wall_coordinate = get_coordinate('#')


start_near_list = [near_or_not(start_coordinate[0], i) for i in wall_coordinate]
now_coordinate = start_coordinate[0]
count = 0
# while now_coordinate != end_coordinate[0]:
#     # 開頭，右邊有沒有牆壁
#     if count == 0:
#         if now_coordinate[1] == 0 or [now_coordinate[0], now_coordinate[1] - 1] in wall_coordinate:
#             # 有的話，看前面有沒有牆壁
#             if now_coordinate[0] ,ml

