class CakeShop:
    def __init__(self, flour, egg, strawberry):
        self.flour = flour
        self.egg = egg
        self.strawberry = strawberry
        self.cost = 0
        self.gain = 0

    def purchase(self, type, quantity, price):
        self.cost += price
        if type == 'F':
            self.flour += quantity
        elif type == 'E':
            self.egg += quantity
        elif type == 'S':
            self.strawberry += quantity
        print(f"flour:{self.flour},egg:{self.egg},strawberry:{self.strawberry}")

    def sell(self, type, quantity):
        if type == 'S':
            if (self.flour >= (200 * quantity)) and (self.egg >= (2 * quantity)) and (self.strawberry >= (5 * quantity)):
                self.flour -= 200 * quantity
                self.egg -= 2 * quantity
                self.strawberry -= 5 * quantity
                self.gain += 500 * quantity
                print('Order Completed')
            else:
                print('Order Cancel')
        elif type == 'O':
            if (self.flour >= (300 * quantity)) and (self.egg >= (3 * quantity)):
                self.flour -= 300 * quantity
                self.egg -= 3 * quantity
                self.gain += 350 * quantity
                print('Order Completed')
            else:
                print('Order Cancel')

    def analysis(self):
        print_str = ''
        count = 0
        count_egg = 0
        if self.flour < 200 and self.egg >= 2 and self.strawberry >= 5:
            print('flour')
        elif self.flour < 200 and self.egg < 2 and self.strawberry >= 5:
            print('flour,egg')
        elif self.flour < 200 and self.egg < 2 and self.strawberry < 5:
            print('flour,egg,strawberry')
        elif self.flour < 200 and self.egg >= 2 and self.strawberry < 5:
            print('flour,strawberry')
        elif self.flour >= 200 and self.egg < 2 and self.strawberry < 5:
            print('egg,strawberry')
        elif self.flour >= 200 and self.egg < 2 and self.strawberry >= 5:
            print('egg')
        elif self.flour >= 200 and self.egg >= 2 and self.strawberry < 5:
            print('strawberry')
        elif self.flour >= 200 and self.egg >= 2 and self.strawberry >= 5:
            print(None)
        print(self.gain - self.cost)

shop = CakeShop(1275, 48, 32)
while 1:
    try:
        args = input().split()
        if args[0] == "purchase":
            shop.purchase(args[1], int(args[2]), int(args[3]))
        elif args[0] == "sell":
            shop.sell(args[1], int(args[2]))
            shop.purchase('E', 0, 0)
        elif args[0] == "analysis":
            shop.purchase('E', 0, 0)
            shop.analysis()
    except:
        break
