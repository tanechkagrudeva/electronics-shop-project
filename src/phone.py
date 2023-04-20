from src.item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim:int = number_of_sim

    def __repr__(self):
        return f'''{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})'''

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise Exception
    #     else:
    #         raise TypeError
    #
    # def control(self):
    #     if not isinstance(Phone, Item):
    #         raise ValueError('Складывать можно только `Phone` или `Item` с экземплярами не `Phone` или `Item` классов')

print(isinstance(Item,Phone))
print(isinstance(Phone,Item))
