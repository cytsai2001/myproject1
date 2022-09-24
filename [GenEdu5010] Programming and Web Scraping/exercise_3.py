# lst = ['5','5','6','6']
# print(','.join(lst))
# # lst = list of str, all the elements are str.
# import this
# print(this)
given_integer = int(input())
cumulation = 0
for i in range(1, given_integer, 1):
    if given_integer % i == 0:
        cumulation += 1
# if given_integer % 2 == 0:
#     cumulation += 1
if cumulation >= 2:
    print(False)
else:
    print(True)
