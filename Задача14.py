# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
import os

os.system('cls')
from array import array

#    Solution   1
n = int(input('Введите число N:  '))
number = 2
res = 1
result = [1]
while res < n:
    res = res * number
    if res < n:
      result.append(res)
print(result)

# solution 2
n = int(input('Введите число N:  '))
number = 2
res = 1
result = [1]
while res < n:
    res = res * number
    result.append(res)
result.pop(-1)
print(result)