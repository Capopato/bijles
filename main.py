from bag import Bag
from engine import Engine

# Maak een method in de Car class genaamd change_key(self) die de key_turned eigenschap switched. Dus False wordt True en True wordt False.
#
# Maak een nieuwe class aan genaamd Bag die 2 eigenschappen heeft: color en weight. Maak ook weer een repr hiervoor.
# Deze hebben we nodig voor het volgende:
#
# In de Car constructor (dus de _init_), maak daar die lijst aan, genaamd luggage die leeg begint.
# Hier hebben we het over gehad, deze heeft dus geen bijbehorende parameter.
#
# Maak een method in de Car class genaamd add_bag(self, bag: Bag) die dus een tas toevoegt aan die lijst.
#
# Lastig:
# Maak een method die de totale weight van de luggage berekent. Dus je moet de weight sommeren van alle Bags in de luggage lijst.
# Noem hem calc_luggage_weight(self) -> int:

class Car:
    def __init__(self, engine: Engine, gastank: int, key_turned: bool, wheels: int):
        self.engine = enginek
        self.gastank = gastank
        self.key_turned = key_turned
        self.wheels = wheels
        self.luggage = []

    def __repr__(self) -> str:  # the -> states the expected output
        return f"Car(Engine: {self.engine}, gastank: {self.gastank}, key: {self.key_turned}, wheels: {self.wheels})"
        # return f"Car(Engine: {self.engine}, gastank: {self.gastank}, key: {self.key_turned}, wheels: {self.wheels}, luggage: {self.luggage})"

    def calc_luggage_weight(self) -> int:
        print(self.luggage)  # Just to check to whole list
        total_weight = 0  # Set new total weight to 0
        for i in self.luggage:  # Iterate over self.luggage
            if isinstance(i, int):  # If int
                total_weight += i  # Add to total weight
            elif isinstance(i, float):  # If int
                total_weight += i  # Add to total weight

        return total_weight

    def add_bag(self, bag: Bag):  # Take values from class Bag
        self.luggage.append(bag.colour)  # Add colour to list
        self.luggage.append(bag.weight)  # Add weight to list

    def change_key(self) -> bool:  # Method to turk key
        if self.key_turned == True:  # If key is True
            self.key_turned = False  # Set key to False
            return self.key_turned  # Return change

        elif self.key_turned == False:  # If key is False
            self.key_turned = True  # Set key to True
            return self.key_turned  # Return change

    def can_move(self) -> bool:  # Method that depicts if car can move
        return self.key_turned and self.gastank > 0  # return True (car can move) If key is True and gastank > 0


e = Engine(100, 'Ferrari')
b1 = Bag('Blue', 25)
b2 = Bag('Red', 35)
b3 = Bag('Purple', 15)
b4 = Bag('Black', 22.5)
c = Car(e, 100, False, 4)

print(c)

c.add_bag(b1)
c.add_bag(b2)
c.add_bag(b3)
c.add_bag(b4)
print(c.calc_luggage_weight())


