name = input('class name:')
grade = input('class grade:')
allwordlist = []

for word in grade:
    wordlist = list(word)
    allwordlist.extend(wordlist)

if len(allwordlist) == 1:
    if allwordlist[0] == 'A':
        gpa = 4.0
        print(name + ' grade point: ' + str(float(gpa)), end='')
    elif allwordlist[0] == 'B':
        gpa = 3.0
        print(name + ' grade point: ' + str(float(gpa)), end='')
    elif allwordlist[0] == 'C':
        gpa = 2.0
        print(name + ' grade point: ' + str(float(gpa)), end='')
    else:
        gpa = 0.0
        print(name + ' grade point: ' + str(float(gpa)), end='')
else:
    if allwordlist[0] == 'A':
        gpa = 4.0
        if allwordlist[1] == '+':
            print(name + ' grade point: ' + str(float(gpa + 0.3)), end='')
        else:
            print(name + ' grade point: ' + str(float(gpa - 0.3)), end='')
    elif allwordlist[0] == 'B':
        gpa = 3.0
        if allwordlist[1] == '+':
            print(name + ' grade point: ' + str(float(gpa + 0.3)), end='')
        else:
            print(name + ' grade point: ' + str(float(gpa - 0.3)), end='')
    else:
        gpa = 2.0
        if allwordlist[1] == '+':
            print(name + ' grade point: ' + str(float(gpa + 0.3)), end='')
        else:
            print(name + ' grade point: ' + str(float(gpa - 0.3)), end='')
