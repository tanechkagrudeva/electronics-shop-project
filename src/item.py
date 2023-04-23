import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        """атрибут `name` сделать приватным"""
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        return f'''{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})'''

    def __str__(self):
        return f"""{self.__name}"""

    def __add__(self, other):
         if isinstance(other, Item):
             return self.quantity + other.quantity


    """добававляем геттер и сеттер для `name`, используя @property"""
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print("Длина наименования товара превышает 10 символов")



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.value = self.price * self.quantity
        return self.value

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
    @classmethod
    def instantiate_from_csv(cls, filename):
        Item.all.clear()
        with open(filename, encoding='windows-1251') as r_file:
            file_reader = csv.DictReader(r_file)
            for row in file_reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(num):
        return int(float(num))



