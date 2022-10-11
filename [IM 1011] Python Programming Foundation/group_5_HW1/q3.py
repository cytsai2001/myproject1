import math
import numpy as np

id = input('student ID: ')
score = input('raw score: ')
finalscore = math.sqrt(float(score))*10
print('student ID: ' + id, 'final score: ' + str(np.round(finalscore, 2)), sep='\n', end='')
