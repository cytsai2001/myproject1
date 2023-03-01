class card:
    def __init__(self, card_info: str):
        if card_info[:-1] == 'A':
            self.value = 1
        elif card_info[:-1] == 'T':
            self.value = 10
        elif card_info[:-1] == 'J':
            self.value = 11
        elif card_info[:-1] == 'Q':
            self.value = 12
        elif card_info[:-1] == 'K':
            self.value = 13
        else:
            self.value = int(card_info[:-1])
        if card_info[-1] == 'c':
            self.suit = 0
        elif card_info[-1] == 'd':
            self.suit = 1
        elif card_info[-1] == 's':
            self.suit = 2
        elif card_info[-1] == 'h':
            self.suit = 3

class holeCards: # 底牌
    def __init__(self, card_arr: list):
        self.cards = [card(i) for i in card_arr]

# self.cards = A list with length 2, all elements in list is an object, card.

class boardCards: # 公牌
    def __init__(self, card_arr: list):
        self.cards = [card(i) for i in card_arr]
        # self.cards = A list with length 5, all elements in list is an object, card.


## We will judge the your code by the following code segment.
## Input takes in 8 cards, one for checking <class: card>, two for checking <class: holeCards>, five for checking <class.hoardCards>
def print_card(c: card) -> None:
    print(f"{c.value} {c.suit}")
    return None

c = card(input())
print_card(c)

h = []
for i in range(2):
    h.append(input())
hc = holeCards(h)
for el in hc.cards:
    print_card(el)

b = []
for i in range(5):
    b.append(input())
bc = boardCards(b)
for el in bc.cards:
    print_card(el)


