from src.item import Item
class Mixsin:
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            return self.language == "RU"
        return self.language == "EN"
class Keyboard(Item, Mixsin):
    def __init__(self, name: str, price: float, quantity: int, language) -> None:
        super().__init__(name, price, quantity)
        self.language = language




