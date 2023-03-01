def go_stairs(steps, broken):
    dic = {}
    for i in range(steps + 1):
        if i == 0:
            dic[0] = 1
        elif i == 1 and i not in broken:
            dic[1] = 1
        elif i == 2 and i not in broken and 1 not in broken:
            dic[2] = 2
        elif i == 2 and i not in broken and 1 in broken:
            dic[2] = 1
        elif i in broken:
            dic[i] = 0
        elif i > 1:
            if i not in dic:
                dic[i] = dic[i - 1] + dic[i - 2] + dic[i - 3]
    return dic[steps]
    # elif steps > 1:
    #     return go_stairs(steps - 1, broken) + go_stairs(steps - 2, broken) + go_stairs(steps - 3, broken)

a = [int(i) for i in input().split()]
n = a[0]
brokenstep = a[1:]
print(go_stairs(n, brokenstep))
