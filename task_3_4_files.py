"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение (например example345).
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого.
"""

import os
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
    with open(file.name, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)


new_file = create_file('test.txt')
get_text_file(new_file)
