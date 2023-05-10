"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def get_type_of_number(num) -> str:
    try:
        number = float(num)
        if int(number) == number:
            return f'Number {num} is integer'
        else:
            flag = True
            nums = str(num).split('.')
            if nums[0] == nums[1]:
                return f'Number {num} is floating\n{flag}'
            flag = False
            return f'Number {num} is floating\n{flag}'
    except:
        return f'Not number enetered'


print(get_type_of_number(input('Enter the number: ')))
