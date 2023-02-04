#Задача 16: Требуется вычислить, сколько раз встречается
#некоторое число Х в массиве А[1..N]. Пользователь в первой
#строке вводит натуральное число N - количество элементов
# в массиве. В последующих строках записаны N целых чисел А..
#Последняя строка содержит число Х
import os
os.system('cls')
from random import randint

n = int(input('Введите число N: '))
x = int(input('Введите число X: '))
count = 0
numm_list = []
for i in range(n):
    numm_list.append(randint(1, n))
print(numm_list)
for i in range(n):
    if numm_list[i] == x:
        count +=1
print(count)    