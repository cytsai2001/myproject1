list_of_number = input().split(' ')
input_list_int = []
for item in list_of_number:
    int_i = int(item)
    input_list_int.append(int_i)

count = 0
for i in range(len(input_list_int)):
    for j in range(len(input_list_int)):
        for k in range(len(input_list_int)):
            if (0 <= i) and (i < j) and (j < k) and (k <= (len(input_list_int) - 1)):
                if input_list_int[i] + input_list_int[j] == input_list_int[k]:
                    count += 1

print(count, end='')
