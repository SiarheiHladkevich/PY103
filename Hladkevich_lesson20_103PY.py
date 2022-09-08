class CardDeck:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x < len(self.lst):
            y = self.x
            self.x += 1
            return self.lst[y]
        else:
            raise StopIteration


def make_deck():
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    items = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        for item in items:
            deck.append(f'{item} of {suit}')
    return deck


carddeck = CardDeck(make_deck())
cards = iter(carddeck)
# for card in cards:
    # print(card)
print(cards.__next__())
print(cards.__next__())
print(cards.__next__())
print(cards.__next__())
print(cards.__next__())
