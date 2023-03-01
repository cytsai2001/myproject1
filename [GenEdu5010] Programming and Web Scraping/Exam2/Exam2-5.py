n, l, s, d = [int(i) for i in input().split()]
fare_dist = {}
for i in range(n):
    if i != 0:
        fare_dist[f'from city {i - 1}'] = [int(j) for j in input().split()]
    else:
        fare_dist['salary'] = [int(j) for j in input().split()]

if l == 0:
    if d > s:
        print(- fare_dist.get(f'from city {s}')[d - s - 1])
    elif d < s:
        print(- fare_dist.get(f'from city {d}')[s - d - 1])

elif l == 1:
    intermediate_dict = {}
    for intermediate in range(n):
        if (s < intermediate) and (intermediate < d):
            intermediate_dict[f'intermediate{intermediate}'] = fare_dist.get('salary')[intermediate] - fare_dist.get(f'from city {s}')[intermediate - s - 1] - fare_dist.get(f'from city {intermediate}')[d - intermediate - 1]
        elif (s > intermediate) and (intermediate < d):
            intermediate_dict[f'intermediate{intermediate}'] = fare_dist.get('salary')[intermediate] - fare_dist.get(f'from city {intermediate}')[s - intermediate - 1] - fare_dist.get(f'from city {intermediate}')[d - intermediate - 1]
        elif (s > intermediate) and (intermediate > d):
            intermediate_dict[f'intermediate{intermediate}'] = fare_dist.get('salary')[intermediate] - fare_dist.get(f'from city {intermediate}')[s - intermediate - 1] - fare_dist.get(f'from city {d}')[intermediate - d - 1]
        elif (s < intermediate) and (intermediate > d):
            intermediate_dict[f'intermediate{intermediate}'] = fare_dist.get('salary')[intermediate] - fare_dist.get(f'from city {s}')[intermediate - s - 1] - fare_dist.get(f'from city {d}')[intermediate - d - 1]
    print(max(list(intermediate_dict.values())))

elif l == 2:

