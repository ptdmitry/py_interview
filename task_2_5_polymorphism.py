"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
"""


class ItemDiscount:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class ItemDiscountReport1(ItemDiscount):
    def get_info(self):
        return f'Товар {self.title}'


class ItemDiscountReport2(ItemDiscount):
    def get_info(self):
        return f'Цена товара {self.price}'


product_1 = ItemDiscountReport1('Lenovo', 73000)
print(product_1.get_info())

product_2 = ItemDiscountReport2('Lenovo', 73000)
print(product_2.get_info())
