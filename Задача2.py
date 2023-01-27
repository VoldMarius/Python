# Задача 2:
#  Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
import os
os.system('cls')

n = int(input("Введите число: "))
sum = 0
while n > 1:

    sum = int(sum + n % 10)
    n = n / 10

print(sum)
