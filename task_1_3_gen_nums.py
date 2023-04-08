"""
Разработать целочисленный генератор случайных чисел. В функцию передавать
начальную и конечную границу диапазона генерации (выдавать значения из
диапазона включая концы). Заполнить этими данными словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”,
а значене сгенеренное случайное число. Вывести содержимое словаря.
(Усложненный вариант по желанию*):
Не использовать стандартный модуль python random.
"""

from random import randint


def gen_rand_nums(start: int, end: int) -> dict:
    rand_nums = {}
    for key, val in enumerate(range(start, end + 1), start=1):
        rand_nums[f'elem_{key}'] = randint(start, end)
    return rand_nums


if __name__ == '__main__':
    print(gen_rand_nums(10, 19))
