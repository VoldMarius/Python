# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a n  = a1  + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
import os

os.system('cls')

first_number = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))

arithmetic_progression = []
for i in range(n):
    arithmetic_progression.append(first_number + 2 + (i - 1) * d)
print(arithmetic_progression)
