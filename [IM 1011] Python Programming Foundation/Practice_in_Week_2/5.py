# HONG is a sandwich store. The price of a sandwich is $20. HONG recently promotes a series of promotions.
# Promotion 1: If you buy below 10 sandwiches, you cannot get any discount
#              10~19 sandwiches, you can get 10% off discount
#              over 20 sandwiches, you can get 15% off discount
# Promotion 2: If you buy sandwiches on 6th of every month, you can get an extra 6% off discount.
#
# Besides, if you need a plastic bag for sandwiches, you need to pay $1.
# Please design an ordering system to calculate the total price which the customer has to pay.
# (Note: You need to drop the decimal point of total price.)
#
# Input:
# Purchase date (Format: dd)
# The quantity of sandwiches you want to buy (Integer)
# Need a plastic bag? (Yes/No)
# Output: Total price
#
# Example:
# Input:
# Purchase date (Format: dd): 06
# The quantity of sandwiches you want to buy: 17
# Need a plastic bag? (Yes/No): Yes
# Output: 288
date = input('Purchase date (Format: dd): ')
quantity = int(input('The quantity of sandwiches you want to buy: '))
plastic_bag = input('Need a plastic bag? (Yes/No)')

original_price = 20 * quantity
if date == '06':
    price = original_price * 0.94
else:
    price = original_price

if quantity >= 20:
    price *= 0.85
elif (quantity >= 10) and (quantity < 20):
    price *= 0.90
else:
    price = price

if plastic_bag == 'Yes':
    price += 1
else:
    price = price

print(f'Total: {int(price)}')
