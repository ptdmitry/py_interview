"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться
в качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора
дочернего класса (метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена
и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно,
не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    def __init__(self, title, price):
        self.__title = title
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, title, price, discount=0):
        super().__init__(title, price)
        self.__title = title
        self.__price = price
        self.__discount = discount

    def __str__(self):
        prodict_with_discount = self.__price - self.__price * self.__discount / 100
        return f'Цена товара {self.__title} с учётом скидки {self.__discount}%: {prodict_with_discount}'


product = ItemDiscountReport('Lenovo', 73000, 1)
print(product)
