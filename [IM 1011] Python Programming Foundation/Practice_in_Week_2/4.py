score_1 = float(input())
score_2 = float(input())
score_3 = float(input())
highest_score = max(score_1, score_2, score_3)
lowest_score = min(score_1, score_2, score_3)
print(sorted((score_1, score_2, score_3), reverse=True))
print(f'the highest score is {highest_score}', f'the lowest score is {lowest_score}', sep='\n', end='')