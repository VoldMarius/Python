# Задача 28: Напишите рекурсивную функцию sum(a, b),возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1.Также нельзя использовать циклы.
# 2 2
# 4
import os

os.system('cls')


def addition_numbers(x, y):
    rez = 0
    if y == 0:
        return x
    else:
        rez += addition_numbers(x + 1, y - 1)
        return rez


a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
print(addition_numbers(a, b))
