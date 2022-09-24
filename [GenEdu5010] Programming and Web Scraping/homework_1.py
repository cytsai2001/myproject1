import string

raw_string = input()
raw_string_list = list(raw_string)
raw_string_list_copy = raw_string_list.copy()
english_lower_letter = list(string.ascii_lowercase)
english_upper_letter = list(string.ascii_uppercase)

if len(raw_string_list) != 0:
    student_score_list = []
    special_assignment = []

    score = 0
    i = raw_string_list[0]
    while len(raw_string_list) != 0:
        if i in english_lower_letter or i in english_upper_letter:
            score += raw_string_list.count(f'{i}'.lower()) * 1
            score += raw_string_list.count(f'{i}'.upper()) * 2
            student_score_list.append([f'{i}'.lower(), score])
            try:
                while True:
                    raw_string_list.remove(f'{i}'.lower())
            except ValueError:
                pass
            try:
                while True:
                    raw_string_list.remove(f'{i}'.upper())
            except ValueError:
                pass

        else:
            index_of_assignment = raw_string_list_copy.index(i)
            special_assignment.append([f'{i}', index_of_assignment])
            raw_string_list_copy.remove(i)
            raw_string_list_copy.insert(index_of_assignment, '')
            raw_string_list.remove(f'{i}')

        if len(raw_string_list) == 0:
            break
        i = raw_string_list[0]
        score = 0

    sorted_student_score_list = sorted(student_score_list, key=lambda student_id: student_id[0])

    # Print a 'list' of special assignment,
    # surpassing the issue of can only print out ['\\', index] instead of ['\', index].
    # print('[', sep='', end='')
    # for i in range(len(special_assignment)):
    #     if i < len(special_assignment) - 1:
    #         print('(' + '\'' + f'{special_assignment[i][0]}' + '\'' + ', ' + f'{special_assignment[i][1]}' + ')',
    #               sep='', end=', ')
    #     elif i == len(special_assignment) - 1:
    #         print('(' + '\'' + f'{special_assignment[i][0]}' + '\'' + ', ' + f'{special_assignment[i][1]}' + ')',
    #               sep='', end='')
    # print(']', sep='', end='\n')

    if len(sorted_student_score_list) != 0 and len(special_assignment) != 0:
        print(sorted_student_score_list, end='\n')
        print('[', sep='', end='')
        for i in range(len(special_assignment)):
            if i < len(special_assignment) - 1:
                print('(' + '\'' + f'{special_assignment[i][0]}' + '\'' + ', ' + f'{special_assignment[i][1]}' + ')',
                      sep='', end=', ')
            elif i == len(special_assignment) - 1:
                print('(' + '\'' + f'{special_assignment[i][0]}' + '\'' + ', ' + f'{special_assignment[i][1]}' + ')',
                      sep='', end='')
        print(']', sep='', end='\n')
    if len(sorted_student_score_list) == 0 and len(special_assignment) != 0:
        print('[', sep='', end='')
        for i in range(len(special_assignment)):
            if i < len(special_assignment) - 1:
                print('(' + '\'' + f'{special_assignment[i][0]}' + '\'' + ', ' + f'{special_assignment[i][1]}' + ')',
                      sep='', end=', ')
            elif i == len(special_assignment) - 1:
                print('(' + '\'' + f'{special_assignment[i][0]}' + '\'' + ', ' + f'{special_assignment[i][1]}' + ')',
                      sep='', end='')
        print(']', sep='', end='\n')
    if len(sorted_student_score_list) != 0 and len(special_assignment) == 0:
        print(sorted_student_score_list, end='')
