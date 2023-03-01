scores_text_file = open('scores.txt', 'r', encoding='utf-8')
lines = []
for line in scores_text_file.readlines():
    lines.append([int(i) for i in line.split()])
scores_text_file.close()

total_score_dict = {}
for line in lines:
    total_score_dict[line[0]] = line[1] + line[2] + line[3]

print(f'No. {max(total_score_dict, key=total_score_dict.get)} has the highest total score {max(total_score_dict.values())}.')
