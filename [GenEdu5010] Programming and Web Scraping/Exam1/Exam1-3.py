student_list = [f'{i}' for i in input().split()]

student_score_list = []

score = 0
last_five_code = []
product = 1
for student in student_list:
    if student[3:4] == '9':
        score = 0
        student_score_list.append([score, student])
    else:
        if student[0:3] == 'b06':
            score += 3
        elif student[0:3] == 'b07':
            score += 1
        if int(student[6:]) % 3 == 0 or int(student[6:]) % 5 == 0 or int(student[6:]) % 7 == 0:
            score += 2
        if int(student[6:]) % 2 == 0:
            score += 1
        last_five_code = [int(i) for i in student[4:] if i != '0']
        for i in range(len(last_five_code)):
            product *= last_five_code[i]
        if product // 10000 >= 1:
            score += 4
        else:
            if product // 1000 >= 1:
                score += 3
            else:
                if product // 100 >= 1:
                    score += 2
                else:
                    if product // 10 >= 1:
                        score += 1
        student_score_list.append([score, student])
    product = 1
    score = 0


sorted_student_list = sorted(student_score_list, key=lambda id: id[0], reverse=True)

print(sorted_student_list[0][0], sorted_student_list[0][1], sep=',', end='')
