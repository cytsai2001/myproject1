n = int(input())
dict_of_patient = {}
for i in range(n):
    patient_info = [str(i) for i in input().split()]
    dict_of_patient[patient_info[0]] = [int(patient_info[1]), int(patient_info[2]), int(patient_info[3])]

total_wait = 0
late = 0
doctor_spent = 0
current_id = 1
sorted_dict_list = sorted(dict_of_patient.items(), key=lambda id: id[1], reverse=False)
sorted_dict = dict(sorted_dict_list)

for i in sorted_dict.values():
    if i[1] == current_id:
        if doctor_spent > i[0]:
            total_wait += doctor_spent - i[0]
        else:
            doctor_spent = i[0]
        doctor_spent += i[2]
        current_id += 1
    elif i[1] > current_id:
        if doctor_spent > i[0]:
            total_wait += doctor_spent - i[0]
        else:
            doctor_spent = i[0]
        late += (i[1] - current_id)
        current_id = i[1]
        doctor_spent += i[2]
        current_id += 1
    else:
        count = 0
        for j in sorted_dict.values():
            if i[0] == j[0]:
                if i[1] > j[1]:
                    if doctor_spent > i[0]:
                        total_wait += doctor_spent - i[0]
                    else:
                        doctor_spent = i[0]
                    current_id = i[1]
                    doctor_spent += i[2]
                    current_id += 1
                    count += 1
                elif i[1] < j[1]:
                    if doctor_spent > j[0]:
                        total_wait += doctor_spent - j[0]
                    else:
                        doctor_spent = j[0]
                    current_id = j[1]
                    doctor_spent += j[2]
                    current_id += 1
                    count += 1
        if count == 0:
            if doctor_spent > i[0]:
                total_wait += doctor_spent - i[0]
            else:
                doctor_spent = i[0]
            current_id = i[1]
            doctor_spent += i[2]
            current_id += 1
            count += 1

print(round(total_wait/len(sorted_dict), 1))
print(late)
