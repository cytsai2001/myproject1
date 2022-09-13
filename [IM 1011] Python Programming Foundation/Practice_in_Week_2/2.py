juice_price = 70
bread_price = 30
notebook_price = 150

allowance = int(float(input()))
if allowance >= juice_price + bread_price + notebook_price:
    print(allowance - juice_price - bread_price - notebook_price)
elif allowance >= juice_price + bread_price \
        and allowance < juice_price + bread_price + notebook_price:
    print(allowance - juice_price - bread_price)
elif allowance >= juice_price and allowance < juice_price + bread_price:
    print(allowance - juice_price)
else:
    print("You don't have enough money.")
