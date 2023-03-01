import string
N = int(input())
k = int(input())
j = 1
index_of_lower = 0
index_of_upper = 0
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
for i in range(N):
    count = 0
    while count - k + 1 <= i:
        if count - k + 1 < i:
            if i % 3 == 2:
                print(j, sep='', end='')
                if j == 9:
                    j = 0
                else:
                    j += 1
                count += 1
            elif i % 3 == 1:
                print(lower[index_of_lower], sep='', end='')
                if index_of_lower == 25:
                    index_of_lower = 0
                else:
                    index_of_lower += 1
                count += 1
            elif i % 3 == 0:
                print(upper[index_of_upper], sep='', end='')
                if index_of_upper == 25:
                    index_of_upper = 0
                else:
                    index_of_upper += 1
                count += 1
        elif count - k + 1 == i:
            if i % 3 == 2:
                print(j, sep='', end='\n')
                if j == 9:
                    j = 0
                else:
                    j += 1
                count += 1
            elif i % 3 == 1:
                print(lower[index_of_lower], sep='', end='\n')
                if index_of_lower == 25:
                    index_of_lower = 0
                else:
                    index_of_lower += 1
                count += 1
            elif i % 3 == 0:
                print(upper[index_of_upper], sep='', end='\n')
                if index_of_upper == 25:
                    index_of_upper = 0
                else:
                    index_of_upper += 1
                count += 1
# n = int(input())
# j = 1
# for i in range(n):
#     count = 0
#     while count <= i:
#         if count < i:
#             print(j, sep='', end='')
#             if j == 9:
#                 j = 0
#             else:
#                 j += 1
#             count += 1
#         elif count == i:
#             print(j, sep='', end='\n')
#             if j == 9:
#                 j = 0
#             else:
#                 j += 1
#             count += 1
