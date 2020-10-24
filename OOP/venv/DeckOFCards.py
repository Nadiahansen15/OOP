class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, x):
        return self.cards[x]

    def __add__(self, n):
        return self.cards.append(n)

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f'Cards: {self.cards}'

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del(self.cards[key])

d = Deck()
print(len(d))
print(d[1])
print(d+"hej")
print(repr(d))
print(str(d.cards))
del(d[1])
print(d)
d[2] = 1000
print(d)





