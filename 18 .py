# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
n = int(input('Введите число N: '))
x = int(input('Введите число X: '))
count = 0
numm_list = []
for i in range(1,n+1):
    numm_list.append(i)
print(numm_list)
if x >= n:
    print (n)
else:
    for i in range(n):
        if numm_list[i] == x :
           print (numm_list[i])