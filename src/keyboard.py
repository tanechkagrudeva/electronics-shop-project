from src.item import Item
class LanguageMixin:
    def __init__(self, language = "EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language == "EN" or language == "RU":
            self.__language = language
            raise AttributeError

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)







