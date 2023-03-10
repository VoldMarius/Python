# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
from random import randint
from array import array
import os

os.system('cls')

n = int(input('Введите число кустов N: '))
a = int(input('Введите число ягод на  кусте A: '))
garden_bed = []
for i in range(n):
    garden_bed.append(randint(1, a))
print(garden_bed)
bushes = []
for i in range(len(garden_bed)):
    bushes.append(sum(garden_bed[i - 3:i]))

print(f'максимальное число ягод за один заход {max((bushes))}')
