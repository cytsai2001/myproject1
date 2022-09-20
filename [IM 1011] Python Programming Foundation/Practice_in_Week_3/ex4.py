# A logical operation is a special symbol or word that connects two or more phrases of information.
# It is most often used to test whether a certain relationship between the phrases is true or false.
# Example:
# 3 AND 5 is 1. 3 OR 5 is 1. 3 XOR 5 is 0.
# Output is given as 1. Hence, the possible
# operators would be AND, OR.
# sample input:
# 3 5 1
# sample output:
# AND
# OR
#
# sample iutput:
# 2 0 1
# sample output:
# OR
# XOR
#
# sample iutput:
# 0 0 1
# sample output:
# IMPOSSIBLE

a = [input('input_1, number'), input('input_2, number'), input('output, 0 or 1')]
if a[2] == '0':
    if (a[0] == '0') and (a[1] == '0'):
        print('AND, OR, XOR')
    elif (a[0] != '0') and (a[1] == '0'):
        print('AND')
    elif (a[0] == '0') and (a[1] != '0'):
        print('AND')
    else:
        print('XOR')
if a[2] == '1':
    if (a[0] == '0') and (a[1] == '0'):
        print('Impossible')
    elif (a[0] != '0') and (a[1] == '0'):
        print('OR, XOR')
    elif (a[0] == '0') and (a[1] != '0'):
        print('OR, XOR')
    else:
        print('AND, OR')

