def char_puzzle(lst):
    list_of_letter = []
    for i in lst:
        list_of_letter += [f'{j}' for j in i]
    duplicate_removed = sorted([*set(list_of_letter)])
    answer = ''
    for i in duplicate_removed:
        answer += i
    return answer

print(char_puzzle(["ccclub",  "python",  "class", "in", "ntu"]))
