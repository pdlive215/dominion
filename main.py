class Treasure:
    def __init__(self, name):
        self.name = name
        self.cost = cost
        self.payload = payload

copper = Treasure(name="Copper", cost=0, payload=1)
silver = Treasure(name="Silver", cost=3, payload=2)
gold = Treasure(name="Gold", cost=6, payload=3)


class Victory:
    def __init__(self, name):
        self.name = name
        self.cost = cost
        self.points = points

estate = Victory(name="Estate", cost=2, points=1)
duchy = Victory(name="Duchy", cost=5, points=3)
province = Victory(name="Province", cost=8, points=6)


class Kingdom:
    def __init__(self, cost, payload=0, action=0, buys=0)
        self.name = name
        self.cost = cost
        self.payload = payload
        self.action = action
        self.buys = buys

# sifter
cellar = Kingdom(name="Cellar", cost=2, action=1)

# trasher
chapel = Kingdom(name="Chapel", cost=2)

# reaction (immunity to attack)
moat = Kingdom(name="Moat", cost=2)

# discard pile inspector
harbinger = Kingdom(name="Harbinger", cost=3)

# add 1 payload if silver in play
merchant = Kingdom(name="Merchant", cost=3, action=1)

# inspect next card, play action or discard
vassal = Kingdom(name="Vassal", cost=3, payload=2)

village = Kingdom(name="Village", cost=3, action=2)

# gain card costing up to 4
workshop = Kingdom(name="Workshop", cost=3)


class Player:
    def __init__(self, name, deck, pile, hand):
        self.name = name
        self.deck = deck
        self.pile = pile
        self.hand = hand

        self.payload = payload
        self.action = action
        self.buys = buys



class Board:
    def __init__(self, players):
        self.players = players