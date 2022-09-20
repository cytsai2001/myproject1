# Please let the user input a positive number to be the height (highest point)
# and use Loop and print to draw the corresponding triangle.
# example 1:
# input = 6
#
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
# example 2:
# input = 3
#
# *
# **
# ***
# **

a = int(input('Please input the wanted height of triangle (int)'))

for i in range(1, a+1, 1):
    print(i*'*', sep='', end='\n')
for j in range(a-1, 0, -1):
    print(j*'*', sep='', end='\n')
    if j == 0:
        break
