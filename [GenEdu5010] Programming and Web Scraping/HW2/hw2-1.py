competitor_dict = {}

# def sorting_key(lst):
#     for i in lst:
#         if i.split(':')[0] == 'Name':

while True:
    input_info = input()
    if input_info != 'competitorEND':
        competitor = input_info.split(',')
        this_competitor_info = {}
        for i in competitor:
            this_competitor_info[i.split(':')[0]] = i.split(':')[1]
        competitor_dict[this_competitor_info.get('Name')] = [this_competitor_info.get('Gender').upper(), this_competitor_info.get('Age'), this_competitor_info.get('Group'), this_competitor_info.get('Dep').upper()]
    else:
        break
while True:
    try:
        request = input()
        if request in competitor_dict.keys():
            print(f"[('Gender', '{competitor_dict.get(request)[0]}'), ('Age', {competitor_dict.get(request)[1]}), ('Group', {competitor_dict.get(request)[2]}), ('Dep', '{competitor_dict.get(request)[3]}')]")
        elif request.split()[0] == 'Age':
            try:
                count_age = 0
                list_of_output = []
                for i in competitor_dict.items():
                    if i[1][1] == request.split()[1]:
                        list_of_output.append(i[0])
                        count_age += 1
                if count_age == 0:
                    print(None)
                else:
                    print(sorted(list_of_output))
            except IndexError:
                print(None)
        elif request.split()[0] == 'Group':
            try:
                count_group = 0
                list_of_output = []
                for i in competitor_dict.items():
                    if i[1][2] == request.split()[1]:
                        list_of_output.append(i[0])
                        count_group += 1
                if count_group == 0:
                    print(None)
                else:
                    print(sorted(list_of_output))
            except IndexError:
                print(None)
        elif request.split()[0] == 'Dep':
            try:
                count_dep = 0
                list_of_output = []
                for i in competitor_dict.items():
                    if i[1][3] == request.split()[1].upper():
                        list_of_output.append(i[0])
                        count_dep += 1
                if count_dep == 0:
                    print(None)
                else:
                    print(sorted(list_of_output))
            except IndexError:
                print(None)
        elif request.split()[0] == 'Gender':
            try:
                count_gender = 0
                list_of_output = []
                for i in competitor_dict.items():
                    if i[1][0] == request.split()[1].upper():
                        list_of_output.append(i[0])
                        count_gender += 1
                if count_gender == 0:
                    print(None)
                else:
                    print(sorted(list_of_output))
            except IndexError:
                print(None)
        else:
            print(None)
    except:
        break
    # if request == 'STOP':
    #     break
