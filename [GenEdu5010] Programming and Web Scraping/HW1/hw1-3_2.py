position = list(input())
english_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
number_list = ['1', '2', '3', '4', '5', '6', '7', '8']
available_position = []


def vertical_line(position_of_queen, available_position_list):
    available_position_list += [f'{position_of_queen[0]}{i}' for i in number_list if i != position[1]]
    return available_position_list


def horizontal_line(position_of_queen, available_position_list):
    available_position_list += [f'{i}{position_of_queen[1]}' for i in english_letter if i != position[0]]
    return available_position_list


def first_quadrant(position_of_queen, available_position_list):
    available_position_list += [f'{english_letter[english_letter.index(position_of_queen[0]) + i]}{number_list[number_list.index(position_of_queen[1]) + i]}' for i in range(8)
                                if english_letter.index(position_of_queen[0]) + i <= 7 and number_list.index(position_of_queen[1]) + i <= 7]
    if available_position_list.count(f'{position[0]}{position[1]}') > 0:
        available_position_list.remove(f'{position[0]}{position[1]}')
    return available_position_list


def second_quadrant(position_of_queen, available_position_list):
    available_position_list += [f'{english_letter[english_letter.index(position_of_queen[0]) - i]}{number_list[number_list.index(position_of_queen[1]) + i]}' for i in range(8)
                                if (english_letter.index(position_of_queen[0]) - i >= 0) and (number_list.index(position_of_queen[1]) + i <= 7)]
    if available_position_list.count(f'{position[0]}{position[1]}') > 0:
        available_position_list.remove(f'{position[0]}{position[1]}')
    return available_position_list


def third_quadrant(position_of_queen, available_position_list):
    available_position_list += [f'{english_letter[english_letter.index(position_of_queen[0]) - i]}{number_list[number_list.index(position_of_queen[1]) - i]}' for i in range(8)
                                if english_letter.index(position_of_queen[0]) - i >= 0 and number_list.index(position_of_queen[1]) - i >= 0]
    if available_position_list.count(f'{position[0]}{position[1]}') > 0:
        available_position_list.remove(f'{position[0]}{position[1]}')
    return available_position_list


def forth_quadrant(position_of_queen, available_position_list):
    available_position_list += [f'{english_letter[english_letter.index(position_of_queen[0]) + i]}{number_list[number_list.index(position_of_queen[1]) - i]}' for i in range(8)
                                if (number_list.index(position_of_queen[1]) - i >= 0) and (english_letter.index(position_of_queen[0]) + i <= 7)]
    if available_position_list.count(f'{position[0]}{position[1]}') > 0:
        available_position_list.remove(f'{position[0]}{position[1]}')
    return available_position_list


vertical_line(position, available_position)
horizontal_line(position, available_position)
first_quadrant(position, available_position)
second_quadrant(position, available_position)
third_quadrant(position, available_position)
forth_quadrant(position, available_position)

no_repeated_available_list = list(set(available_position))
sorted_available = sorted(no_repeated_available_list, reverse=False)

print(sorted_available, sep='', end='')
