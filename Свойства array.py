import os
os.system('cls')
from array import array

a = array('i', [1, 4, 7, 65, 4])
b = array('i', [25, 96, 78])
print(a)
# Вывод элемента
print(a[0])
print(a[-2])
# Слайс массива
print(a[2:])
print(a[1:-2])
#  разворот массива
a.reverse()
print(a)
print(a[::-1])
# Умножение массива(увеличение кол-ва элементов)
print(a * 2)
# Сложение массивов
print(a + b)
# Добавление элемента
a.append(5)
print(a)
# Подсчет заданных элементов
print(a.count(4))
# Конвертация массива в лист
b = a.tolist()
print(b)
print(type(b))
# Поиск индекса заданного элемента
print(a.index(65))
# Изменение элемента по индексу
a.insert(2,558)
print(a)
# Удоление и получение значение индексируемого элемента
print(a.pop(5))
print(a)
# Удоление элемента (первого если несколько таких по порядку)
print(a.remove(558))
print(a)
# Удоление по индексу
del a[3]
print(a)
# Создание структуры И изменение заданных элементов по условию цикла
a = array('i',list(range(13)))
print(a)

for value in a:
   if value % 2 == 0:
         a[a.index(value)] =89
print(a)    
