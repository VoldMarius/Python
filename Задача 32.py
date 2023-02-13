# Задача 32: Определить индексы элементов массива (списка),значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
from module import creat_list
import os

os.system('cls')

num_list = creat_list(10)
minimum = int(input('Введите минимальный элемент интервала:  '))
maximum = int(input('Введите максимальный элемент интервала:  '))
new = []
for i in range(len(num_list)):
    if num_list[i] > minimum and num_list[i] < maximum:
        new.append(num_list[i])
print(num_list)
print(new)
