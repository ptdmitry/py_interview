"""
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений (выбирается случайно)
заменить на значения типа 345example (в обратном порядке, число и строка).
(То есть вы переделываете функцию записи в файл так, чтобы она иногда меняла запись на 345example).
Реализовать функцию поиска определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать функцию замену всех найденных подстрок
на новое значение и вывод измененных строк. (это ДВЕ ОТДЕЛЬНЫЕ функции которые ВЫВОДЯТ значения,
не записывают и не модифицируют файлы).
"""

import os
import re
from string import ascii_lowercase
from random import randint
from functools import reduce


def get_random_str():
    return reduce(lambda string, char: string + char,
                  [ascii_lowercase[randint(1, len(ascii_lowercase) - 1)] for _ in range(5)])


def create_file(name: str):
    if os.path.exists(name):
        print(f'Файл с именем {name} уже существует')
        exit()
    with open(name, 'w', encoding='utf=8') as f:
        numbers = [randint(1, 100) for _ in range(3)]
        strings = [get_random_str() for _ in range(3)]
        f.writelines([f'{txt}{num}\n' for txt, num in zip(strings, numbers)])
        return f


def get_text_file(file):
    with open(file.name, 'r', encoding='utf-8') as file_in:
        with open('new_test.txt', 'w', encoding='utf-8') as file_out:
            for line in file_in:
                num = re.search(r'\d+', line)
                string = re.search(r'\w[a-z]+', line)
                line = num.group(0) + string.group(0)
                file_out.write(f'{line}\n')
    with open('new_test.txt', 'r', encoding='utf-8') as f:
        for el in f:
            print(el)


new_file = create_file('test.txt')
get_text_file(new_file)
