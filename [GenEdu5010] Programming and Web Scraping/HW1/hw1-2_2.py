import string

raw_string = input()
raw_string_list = list(raw_string)
raw_string_list_copy = raw_string_list.copy()
english_lower_letter = list(string.ascii_lowercase)
english_upper_letter = list(string.ascii_uppercase)

student_score_dict = {f'{i}': 0 for i in english_lower_letter}
student_score_list_unorganized = []
special_assignment = []
list_of_recorded_student = []

count = 0
for i in raw_string_list:
    if i in english_lower_letter:
        student_score_dict.update({f'{i}': int(student_score_dict.get(f'{i}')) + 1})
    elif i in english_upper_letter:
        student_score_dict.update({f'{i}'.lower(): int(student_score_dict.get(f'{i}'.lower())) + 2})
    elif i == '\\':
        student_score_dict.update((key, value * 2) for key, value in student_score_dict.items())
    elif i == '/':
        student_score_dict.update((key, value + 1) for key, value in student_score_dict.items() if value > 0)
    elif i == '@':
        student_last_recorded = ''
        score_last_recorded = 0
        for j in range(count):
            if raw_string_list[j] in english_lower_letter or raw_string_list[j] in english_upper_letter:
                student_last_recorded = f'{raw_string_list[j]}'.lower()
                if raw_string_list[j] in english_lower_letter:
                    score_last_recorded = 1
                elif raw_string_list[j] in english_upper_letter:
                    score_last_recorded = 2

        student_score_dict.update({student_last_recorded: int(student_score_dict.get(student_last_recorded)) + score_last_recorded})
    elif i == '?':
        student_last_recorded = ''
        score_last_recorded = 0
        for j in range(count):
            if raw_string_list[j] in english_lower_letter or raw_string_list[j] in english_upper_letter:
                student_last_recorded = f'{raw_string_list[j]}'.lower()
        student_score_dict.update({student_last_recorded: int(student_score_dict.get(student_last_recorded)) - 1})

    count += 1

final_student_score_dict = {key: value for key, value in student_score_dict.items() if value > 0}


score_list = []
if len(final_student_score_dict) != 0:
    for key, value in final_student_score_dict.items():
        score_list.append([key, value])
    print(score_list)

else:
    print('None')
