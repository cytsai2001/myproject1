start_team = input()
score_list = [int(i) for i in list(input())]

serve_person = ''


def change_the_team(team_started, point_list):
    change_time = 0
    if team_started == 'ab':
        if point_list[0] == 1:
            change_time += 1
    elif team_started == 'cd':
        if point_list[0] == 0:
            change_time += 1
    for i in range(len(point_list)-1):
        if point_list[i] != point_list[i+1]:
            change_time += 1
    return change_time


change_times = change_the_team(start_team, score_list)

if start_team == 'ab':
    serve_person = 'a'
    if score_list[-1] == 0:
        if change_times % 2 == 0:
            serve_person = 'b'
        else:
            serve_person = 'a'
    else:
        if change_times % 2 == 0:
            serve_person = 'd'
        else:
            serve_person = 'c'
else:
    serve_person = 'd'
    if score_list[-1] == 1:
        if change_times % 2 == 0:
            serve_person = 'c'
        else:
            serve_person = 'd'
    else:
        if change_times % 2 == 0:
            serve_person = 'a'
        else:
            serve_person = 'b'

print(serve_person)
