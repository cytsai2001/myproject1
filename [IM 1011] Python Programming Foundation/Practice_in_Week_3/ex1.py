# You have a fashion store.
# The price of clothing, pants, and hat are $300, $550, and $200, respectively.
# Please build a computing system,
# which can automatically compute the total price when a customer tells you how many clothing,
# pants, and hat he/she wants to buy.

amount_of_clothing = int(input('amount_of_clothing'))
amount_of_pants = int(input('amount_of_pants'))
amount_of_hat = int(input('amount_of_hat'))
price_of_clothing = 300
price_of_pants = 550
price_of_hat = 200
total_price = amount_of_clothing*price_of_clothing + amount_of_pants*price_of_pants + amount_of_hat*price_of_hat
print(f'${total_price}')
