N = int(input())
color_order_list = list(input())

color_in_plate = []
discarded_color = []
for i in color_order_list:
    if len(color_in_plate) < N:
        if i not in color_in_plate:
            color_in_plate.append(i)
        elif i in color_in_plate:
            color_in_plate.remove(i)
            color_in_plate.append(i)
    else:
        if i not in color_in_plate:
            discarded_color.append(color_in_plate.pop(0))
            color_in_plate.append(i)
        elif i in color_in_plate:
            color_in_plate.remove(i)
            color_in_plate.append(i)


print(len(discarded_color))
