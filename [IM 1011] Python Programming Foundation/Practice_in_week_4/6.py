first_input = input('default: 4 9').split()
amount_of_item_and_capacity = []
for i in first_input:
    j = int(i)
    amount_of_item_and_capacity.append(j)

second_input = input().split()
weight_of_items = []
for i in second_input:
    j = int(i)
    weight_of_items.append(j)

third_input = input().split()
value_of_items = []
for i in third_input:
    j = int(i)
    value_of_items.append(j)

forth_input = input().split()
if_the_item_is_selected = []
for i in forth_input:
    j = int(i)
    if_the_item_is_selected.append(j)

index_of_selected = []
for i in if_the_item_is_selected:
    if i == 1:
        index = if_the_item_is_selected.index(i)
        index_of_selected.append(index)
        if_the_item_is_selected.remove(i)
        if_the_item_is_selected.insert(0, index)


summation_of_weight = 0
for i in index_of_selected:
    summation_of_weight += weight_of_items[i]

if summation_of_weight > amount_of_item_and_capacity[1]:
    print(0, end='')
else:
    summation_of_value = 0
    for i in index_of_selected:
        summation_of_value += value_of_items[i]
    print(f'{summation_of_weight}', f'{summation_of_value}', sep=' ', end=' ')

