# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

import os
os.system('cls')


def erection_degree(x, y):
    rez = 0
    if y == 0:
        return 1
    else:
        rez = x * erection_degree(x, y - 1)
    return rez


a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
print(erection_degree(a, b))
