num = input('Type an integer: ')
allnumlist = []
ascchecklist = []
descchecklist = []
equalchecklist = []

for x in num:
    numlist = list(x)
    allnumlist.extend(numlist)

for x in range(0, len(allnumlist) - 1):
    if allnumlist[x + 1] > allnumlist[x]:
        ascchecklist.extend([allnumlist[x]])
    elif allnumlist[x + 1] < allnumlist[x]:
        descchecklist.extend([allnumlist[x]])
    elif allnumlist[x + 1] == allnumlist[x]:
        equalchecklist.extend([allnumlist[x]])
    else:
        break

if len(descchecklist) == len(allnumlist) - 1:
    print(num + ': strict desc', end='')
elif len(ascchecklist) == len(allnumlist) - 1:
    print(num + ': strict asc', end='')
elif len(descchecklist) + len(equalchecklist) == len(allnumlist) - 1 and len(descchecklist) != 0:
    print(num + ': desc', end='')
elif len(ascchecklist) + len(equalchecklist) == len(allnumlist) - 1 and len(ascchecklist) != 0:
    print(num + ': asc', end='')
else:
    print(num + ': not sorted', end='')

