"""
Реализовать возможность переустановки значения цены товара
в родительском классе. Проверить, распечатать информацию о товаре.
"""


class ItemDiscount:
    def __init__(self, title, price):
        self.__title = title
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, title, price):
        super().__init__(title, price)
        self.__title = title
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_parent_data(self):
        return f'Товар: {self.__title}, цена: {self.__price}'


product = ItemDiscountReport('Lenovo', 73000)
print(product.get_parent_data())

product.set_price('65000')
print(product.get_parent_data())
