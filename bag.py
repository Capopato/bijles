class Bag:
    def __init__(self, colour: str, weight):
        self.colour = colour
        self.weight = weight

    def __repr__(self):
        return f'{self.colour}, {self.weight}'


print(Bag)
print(Bag('Red', 15))