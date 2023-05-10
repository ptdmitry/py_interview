"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением.
В функции необходимо реализовать поиск имени файла (с расширением),
а затем «выделение» имени файла (без расширения).
Расширений может быть несколько (например testfile.tar.gz).
"""

path_1 = 'C:/Users/ptdmitry/PycharmProjects/interview/lesson_3/task_3_1_path_name.py'
path_2 = 'C:/Users/ptdmitry/PycharmProjects/interview/lesson_3/testfile.tar.gz'


def get_file_name(path: str) -> str:
    file_name_full = path.split('/')[-1]
    file_name = file_name_full.split('.')[0]
    return f'{file_name_full}\n{file_name}'


print(get_file_name(path_1))
print(get_file_name(path_2))
