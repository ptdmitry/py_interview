"""
Создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену.
Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке вида
(“{название товара} {цена товара}”). Создать экземпляры родительского класса и дочернего.
Распечатать информацию о товаре.
"""


class ItemDiscount:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self.title}, цена: {self.price}'


product = ItemDiscountReport('Lenovo', 73000)
print(product.get_parent_data())
