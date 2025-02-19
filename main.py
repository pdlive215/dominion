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
    def __init__(self, cost, cards=0, action=0, buys=0, payload=0, points=0)
        self.name = name
        self.cost = cost
        self.cards = cards
        self.action = action
        self.buys = buys
        self.payload = payload
        self.points = points

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

# gain silver on top of deck; opponent places victory card on deck
bureaucrat = Kingdom(name="Bureaucrat", cost=4)

# increment points by size of deck / 10 (round down)
gardens = Kingdom(name="Gardens", cost=4)

# opponent discards down to three cards
militia = Kingdom(name="Militia", cost=4, payload=2)

# trash copper to gain payload of 3
moneylender = Kingdom(name="Moneylender", cost=4)

# discard a card for each empty supply pile
poacher = Kingdom(name="Poacher", cost=4, cards=1, action=1, payload=1)

# trash a card, gain another card costing +2
remodel = Kingdom(name="Remodel", cost=4)

smithy = Kingdom(name="Smithy", cost=4, cards=3)

# play an action from hand twice
throne_room = Kingdom(name="Throne_Room", cost=4)


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