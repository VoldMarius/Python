# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12
from module import creat_list
from random import randint
from array import array
import os
os.system('cls')

n = int(input('кол-во элементов первого множества: '))
m = int(input('кол-во элементов второго множества: '))
n_list = []
n_list = creat_list(n)
m_list = []
m_list = creat_list(m)
new = {}
print(*n_list)
print(*m_list)
n_list = set(n_list)
m_list = set(m_list)
new = list(set.intersection(n_list, m_list))
new.sort()
print(new)
