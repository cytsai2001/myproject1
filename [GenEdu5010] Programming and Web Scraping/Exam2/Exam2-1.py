scarf_dict = {'1': '文學院\n白色', '2': '理學院\n金黃色', '3': '社科學院\n紫色', '4': '醫學院\n綠色',
              '5': '工學院\n橘色', '6': '生農學院\n淺黃色', '7': '管理學院\n灰色', '8': '公衛學院\n紅色',
              '9': '電資學院\n藍色', 'A': '法律學院\n紫色', 'B': '生命科學院\n天藍色'}

id = input()
college_code = id[3:4]

print(scarf_dict.get(college_code))
