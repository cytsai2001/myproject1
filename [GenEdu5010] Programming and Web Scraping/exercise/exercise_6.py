# ex6-1
# class_of_movie = {'Fantasy': 10, 'Drama': 9, 'Action': 8, 'Thriller': 7, 'Comedy': 6,
#                   'Crime': 5, 'History': 4, 'Romance': 3, 'Adventure': 2, 'Biography': 1}
#
# movie_1 = input()
# IMDb_1 = float(input().split(':')[1])
# genre_1 = input().split()
# score_1 = IMDb_1
# movie_2 = input()
# IMDb_2 = float(input().split(':')[1])
# genre_2 = input().split()
# score_2 = IMDb_2
#
# for i in genre_1:
#     score_1 += class_of_movie.get(i)
#
# for j in genre_2:
#     score_2 += class_of_movie.get(j)
#
# if score_1 == score_2:
#     print(movie_1, movie_2, sep='\n')
# elif score_1 > score_2:
#     print(movie_1)
# else:
#     print(movie_2)

# ex6-2
# n_of_student = int(input())
# dict_of_student = {}
# for i in range(n_of_student):
#     student = input().split()
#     dict_of_student[student[0]] = float(student[1])
# student_to_be_search = input().split()
#
# sum_of_score = float()
# for i in student_to_be_search:
#     sum_of_score += dict_of_student.get(i)
# average_score = sum_of_score / len(student_to_be_search)
# print(average_score)

# ex6-3
# dict_of_correlation = {}
# for i in range(20):
#     correlation = input().split()
#     dict_of_correlation[correlation[0]] = correlation[1]
# start_letter = input()
# print(start_letter, sep='', end=' ')
# next_letter = dict_of_correlation.get(start_letter)
# print(next_letter, sep='', end=' ')
# while next_letter != start_letter:
#     next_letter = dict_of_correlation.get(next_letter)
#     if next_letter == start_letter:
#         break
#     else:
#         print(next_letter, sep='', end=' ')

# ex6-4
n = int(input())
j = 1
for i in range(n):
    count = 0
    while count <= i:
        if count < i:
            print(j, sep='', end='')
            if j == 9:
                j = 0
            else:
                j += 1
            count += 1
        elif count == i:
            print(j, sep='', end='\n')
            if j == 9:
                j = 0
            else:
                j += 1
            count += 1

# ex6-5
# n = int(input())
# dict_of_resident = {}
# for i in range(n):
#     resident = input().split()
#     dict_of_resident[resident[0]] = [resident[1], int(resident[2]), int(resident[3])]
#
# for i in dict_of_resident.values():
#     if i[0] == 'A':
#         i[0] = 2
#     elif i[0] == 'B':
#         i[0] = 1
#     elif i[0] == 'C':
#         i[0] = 0
#     if i[1] >= 10:
#         i[1] = 10
#     elif 5 < i[1] < 10:
#         i[1] = 5
#     elif i[1] < 5:
#         i[1] = 0
#     if i[2] % 2 == 1:
#         i[2] = 1
#     elif i[2] % 2 == 0:
#         i[2] = 0
#
#
# def sorting_key(list_input):
#     return list_input[0], list_input[1], list_input[2]
#
#
# sorted_dict = sorted(dict_of_resident.items(), key=lambda x: x[1], reverse=True)
#
# for i in sorted_dict:
#     print(i[0])

