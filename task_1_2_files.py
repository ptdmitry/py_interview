"""
Реализовать функцию print_directory_contens(path). Функция принимает имя
директории и выводит её содержимое, включая содержимое всех поддиректорий
(рекурсивно вызывая саму себя). Использовать os.walk нельзя, но можно
использовать os.listdir и os.path.isfile
"""

import os


def print_directory_contens(path):
    for i in os.listdir(path):
        new_path = path + f'/{i}'
        if not os.path.isfile(new_path):
            print_directory_contens(new_path)
        else:
            file = new_path.split('/')[-1]
            print(file)


if __name__ == '__main__':
    print_directory_contens('C:\\Python310\\Tools')
