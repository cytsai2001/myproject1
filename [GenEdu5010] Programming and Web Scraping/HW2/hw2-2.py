import json
dict_from_json = json.loads(input())
dict_of_all_info = {}
for i in dict_from_json.items():
    dict_of_all_info[i[0]] = [i[1].get('Gender').upper(), int(i[1].get('Age')), int(i[1].get('Group')), i[1].get('Dep').upper(), 0]


dict_of_judge = {}
for i in range(4):
    judge_i = input().split()
    dict_of_judge[int(judge_i[0])] = [judge_i[1].upper(), int(judge_i[2])]

while True:
    try:
        grade_info_input = input()
        grade_info = grade_info_input.split()
        if int(grade_info[0]) in dict_of_judge:
            if grade_info[1].split(':')[0][0] == 'G':
                try:
                    for i in dict_of_all_info.items():
                        if int(grade_info[1].split(':')[0][1:]) == i[1][2]:
                            grade_add = int(grade_info[1].split(':')[1])
                            if dict_of_judge.get(int(grade_info[0]))[0] == i[1][3]:
                                if dict_of_judge.get(int(grade_info[0]))[1] == i[1][1]:
                                    if grade_add <= 6:
                                        grade_add += 3
                                    else:
                                        grade_add *= 1.5
                                else:
                                    grade_add += 2
                            elif dict_of_judge.get(int(grade_info[0]))[1] == i[1][1]:
                                if dict_of_judge.get(int(grade_info[0]))[0] == i[1][3]:
                                    if grade_add <= 6:
                                        grade_add += 3
                                    else:
                                        grade_add *= 1.5
                                else:
                                    grade_add += 1
                            dict_of_all_info[i[0]][4] += grade_add
                except ValueError:
                    if grade_info[1].split(':')[0] in dict_of_all_info.keys():
                        for i in dict_of_all_info.items():
                            if grade_info[1].split(':')[0] == i[0]:
                                grade_add = int(grade_info[1].split(':')[1])
                                if dict_of_judge.get(int(grade_info[0]))[0] == i[1][3]:
                                    if dict_of_judge.get(int(grade_info[0]))[1] == i[1][1]:
                                        if grade_add <= 6:
                                            grade_add += 3
                                        else:
                                            grade_add *= 1.5
                                    else:
                                        grade_add += 2
                                elif dict_of_judge.get(int(grade_info[0]))[1] == i[1][1]:
                                    if dict_of_judge.get(int(grade_info[0]))[0] == i[1][3]:
                                        if grade_add <= 6:
                                            grade_add += 3
                                        else:
                                            grade_add *= 1.5
                                    else:
                                        grade_add += 1
                                dict_of_all_info[i[0]][4] += grade_add
                    else:
                        print(f'ValueError {grade_info[1]}')
            elif grade_info[1].split(':')[0] in dict_of_all_info.keys():
                for i in dict_of_all_info.items():
                    if grade_info[1].split(':')[0] == i[0]:
                        grade_add = int(grade_info[1].split(':')[1])
                        if dict_of_judge.get(int(grade_info[0]))[0] == i[1][3]:
                            if dict_of_judge.get(int(grade_info[0]))[1] == i[1][1]:
                                if grade_add <= 6:
                                    grade_add += 3
                                else:
                                    grade_add *= 1.5
                            else:
                                grade_add += 2
                        elif dict_of_judge.get(int(grade_info[0]))[1] == i[1][1]:
                            if dict_of_judge.get(int(grade_info[0]))[0] == i[1][3]:
                                if grade_add <= 6:
                                    grade_add += 3
                                else:
                                    grade_add *= 1.5
                            else:
                                grade_add += 1
                        dict_of_all_info[i[0]][4] += grade_add
            else:
                print(f'ValueError {grade_info[1]}')
    except:
        break
dict_of_F = {}
dict_of_M = {}
for i in dict_of_all_info.items():
    if i[1][0] == 'F':
        dict_of_F[i[0]] = i[1]
    elif i[1][0] == 'M':
        dict_of_M[i[0]] = i[1]

score_list_F = []
for i in dict_of_F.items():
    score_list_F.append(i[1][4])
if len(score_list_F) != 0:
    max_score_F = max(score_list_F)
    if max_score_F == 0:
        print(None)
    else:
        list_of_best_F = []
        for i in dict_of_F.items():
            if i[1][4] == max_score_F:
                list_of_best_F.append(i[0])
        list_of_best_F.sort()
        if len(list_of_best_F) == 1:
            for i in list_of_best_F:
                print(i)
        elif len(list_of_best_F) > 1:
            for i in range(len(list_of_best_F) - 1):
                print(f'{list_of_best_F[i]}-', end='')
            print(list_of_best_F[-1])
        else:
            print(None)
else:
    print(None)

score_list_M = []
for i in dict_of_M.items():
    score_list_M.append(i[1][4])
if len(score_list_M) != 0:
    max_score_M = max(score_list_M)
    if max_score_M == 0:
        print(None)
    else:
        list_of_best_M = []
        for i in dict_of_M.items():
            if i[1][4] == max_score_M:
                list_of_best_M.append(i[0])
        list_of_best_M.sort()
        if len(list_of_best_M) == 1:
            for i in list_of_best_M:
                print(i)
        elif len(list_of_best_M) > 1:
            for i in range(len(list_of_best_M) - 1):
                print(f'{list_of_best_M[i]}-', end='')
            print(list_of_best_M[-1])
        else:
            print(None)
else:
    print(None)

dict_of_group = {}
for i in dict_of_all_info.items():
    if i[1][2] not in dict_of_group:
        dict_of_group[i[1][2]] = i[1][4]
    else:
        dict_of_group[i[1][2]] += i[1][4]
if len(dict_of_group) != 0:
    max_score_group = max(dict_of_group.values())
    if max_score_group == 0:
        print(None)
    else:
        for i in sorted(dict_of_group.items()):
            if i[1] == max_score_group:
                best_group_member = []
                print(f'Group {i[0]}: ', end='')
                for j in dict_of_all_info.items():
                    if j[1][2] == i[0]:
                        best_group_member.append(j[0])
                best_group_member.sort()
                for k in range(len(best_group_member) - 1):
                    print(f'{best_group_member[k]}-', end='')
                print(f'{best_group_member[-1]}')
else:
    print(None)
