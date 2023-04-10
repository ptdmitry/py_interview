"""
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет
сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


# Инкапсуляция без доступа к параметрам:


class ItemDiscount:
    def __init__(self, title, price):
        self.__title = title
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self.__title}, цена: {self.__price}'


product = ItemDiscountReport('Samsung', 74000)
print(product.get_parent_data())  # AttributeError: 'ItemDiscountReport' object has no attribute
# '_ItemDiscountReport__title'. Did you mean: '_ItemDiscount__title'?

# Инкапсуляция с доступом к параметрам:


class ItemDiscount:
    def __init__(self, title, price):
        self.__title = title
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self._ItemDiscount__title}, цена: {self._ItemDiscount__price}'


product = ItemDiscountReport('Samsung', 74000)
print(product.get_parent_data())
