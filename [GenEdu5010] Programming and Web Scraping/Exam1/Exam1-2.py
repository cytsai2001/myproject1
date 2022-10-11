x_total_num_of_cake = int(input())
m_chocolate_cake = int(input())
n_strawberry_cake = int(input())
strawberry_chocolate_cake = x_total_num_of_cake - m_chocolate_cake - n_strawberry_cake

# ingredient = [flour, egg, coco, strawberry]
chocolate_cake_ingredient = [90, 3, 0.5, 0]
strawberry_cake_ingredient = [50, 2, 0, 10]
strawberry_chocolate_cake_ingredient = [120, 4, 1.25, 6]

chocolate_cake_ingredient_total = [i * m_chocolate_cake for i in chocolate_cake_ingredient]
strawberry_cake_ingredient_total = [i * n_strawberry_cake for i in strawberry_cake_ingredient]
strawberry_chocolate_cake_ingredient_total = [i * strawberry_chocolate_cake for i in strawberry_chocolate_cake_ingredient]

total_ingredient_needed = []
for i in range(4):
    total = chocolate_cake_ingredient_total[i] + \
            strawberry_cake_ingredient_total[i] + \
            strawberry_chocolate_cake_ingredient_total[i]
    total_ingredient_needed.append(total)

flour_cost = 0
if total_ingredient_needed[0] % 220 == 0:
    flour_cost += (total_ingredient_needed[0] // 220) * 50
elif total_ingredient_needed[0] % 220 != 0:
    flour_cost += ((total_ingredient_needed[0] // 220) + 1) * 50

egg_cost = 0
egg_amount_in_box = 0
if total_ingredient_needed[1] % 8 == 0:
    egg_amount_in_box = total_ingredient_needed[1] // 8
    egg_cost += egg_amount_in_box * 76
elif total_ingredient_needed[1] % 8 != 0:
    egg_amount_in_box = (total_ingredient_needed[1] // 8) + 1
    egg_cost += egg_amount_in_box * 76

coco_cost = 0
if int(total_ingredient_needed[2]) == total_ingredient_needed[2]:
    coco_cost += int(total_ingredient_needed[2]) * 300
else:
    coco_cost += (int(total_ingredient_needed[2]) + 1) * 300

strawberry_cost = 0
if total_ingredient_needed[3] >= 10:
    strawberry_cost += (total_ingredient_needed[3] // 10) * 25
    strawberry_cost += (total_ingredient_needed[3] % 10) * 3
else:
    strawberry_cost += total_ingredient_needed[3] * 3

total_cost = flour_cost + egg_cost + coco_cost + strawberry_cost

print(total_cost, egg_amount_in_box, sep=',', end='')
