# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
from array import array
from random import randint
import os
os.system('cls')

n = int(input('Введите число монеток на столе:  '))
coins = []
for i in range(n):
    coins.append(randint(0, 1))
print(f'На столе {n} монет -> {coins}')


def CountEqual(list_numbers):
    count = 0
    count1 = 0
    for i in range(len(list_numbers)):
        if list_numbers[i] == 0:
            count += 1
        else:
            count1 += 1
    if count < count1:
        return count
    return count1


print(CountEqual(coins))
