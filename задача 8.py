# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
import os
os.system('cls')

n = int(input("Введите высоту шеколадки: "))
m = int(input("Введите ширину шеколадки: "))
k = int(input("Введите колличество долек на отлом: "))
if (n * m % k) % n or (n * m % k) % m:
    print('no')
else:
    print('yes')
