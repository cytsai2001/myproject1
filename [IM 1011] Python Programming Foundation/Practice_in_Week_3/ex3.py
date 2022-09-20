# A programming test has 14 questions.
# In order to increase the pass rate, the scoring method is as follows:
# if you answer 1 to 8 questions correctly, each question will be scored as 8 points;
# if you answer more than 9 questions correctly, the first 8 questions will still be scored as 8 points,
# and the rest will be scored as 6 points.
# Please write a program according to the above description,
# let the user input the number of correct answers,
# and then output the score after calculation by the program.

number_of_correct_answers = int(input())
if (number_of_correct_answers >= 1) and (number_of_correct_answers<= 8):
    point_of_each_question = 8
    score = number_of_correct_answers * point_of_each_question
    print(score)
elif number_of_correct_answers >= 9:
    number_of_correct_answers_more_than_eight = number_of_correct_answers - 8
    point_within_eight_question = 8
    point_of_excess_question = 6
    score = 8 * point_within_eight_question + number_of_correct_answers_more_than_eight * point_of_excess_question
    print(score)
elif number_of_correct_answers > 14:
    print('The correct answer number is out of the number of questions, plz input again.')
