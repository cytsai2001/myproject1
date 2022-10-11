order = input('How many orders do you finish?')

if int(order) <= 50:
    reward = int(order) * 50
    print(reward, end='')
else:
    reward = (int(order) - 50) * 100 + 2500
    print(reward, end='')

# If the driver delivers 30 orders, and x is 50 , y is 100, please calculate his/hers profit of the day.
#   1500 dollars.
# If another driver delivers 70 orders, x and y are the same, what is his/hers profit of the day?
#   4500 dollars.
