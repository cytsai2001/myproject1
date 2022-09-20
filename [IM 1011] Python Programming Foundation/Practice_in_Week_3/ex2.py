# 1 foot = 12 inches.
# Please build a system, which can ask a user what he/she wants to do,
# converting foot to inches or inches to foot.
# The following is an example.
# Convert foot to inches, press 1; Convert inches to foot, press 2; exit, press other key.
# 2
# How many inches do you want to convert?
# 26
# The answer is 2.1666666666

foot_to_inch = 12
a_what_do_u_want_to_do = input('Convert foot to inches, press 1; Convert inches to foot, press 2; exit, press other key.')
if a_what_do_u_want_to_do == '1':
    b_foot = float(input('How many foots do you want to convert?'))
    b_inch = b_foot * foot_to_inch
    print(f'{b_foot} foots is {b_inch} inches.')
elif a_what_do_u_want_to_do == '2':
    b_inch = float(input('How many inches do you want to convert?'))
    b_foot = b_inch / foot_to_inch
    print(f'{b_inch} inches is {b_foot} foots.')


