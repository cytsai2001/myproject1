# Please use Loop and print to draw the following triangle.
# triangle:
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
for i in range(1, 7, 1):
    print(i*'*', sep='', end='\n')
for j in range(5, 0, -1):
    print(j*'*', sep='', end='\n')
    if j == 0:
        break

