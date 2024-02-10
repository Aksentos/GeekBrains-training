""" Задача № 1. Элементы из заданного диапазона
Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума 
и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в 
виде чисел min_number, max_number.
ЭЛЕМЕНТЫ ДОЛЖНЫ ВЫВОДИТЬСЯ ПОСТРОЧНО!"""

import random

# создаем список из рандомных элементов
print(
    list_1 := [
        random.randint(-10, 10)
        for _ in range(int(input("Введите количество элементов: ")))
    ]
)
min_number = 0
max_number = 10
# все что выше вставлять в ГБ не нужно

# 1 вариант
list_index = [i for i in range(len(list_1)) if min_number < list_1[i] < max_number]
print(*list_index, sep="\n")  # выводим все элементы списка list_index построчно

# 2 вариант
for i in range(len(list_1)):
    if list_1[i] in range(min_number, max_number + 1):
        print(i)
# 3 вариант
for i,x in enumerate(list_1):
   if x in range(min_number,max_number+1):
         print(i)

""" Задача № 2. Арифметическая прогрессия
Заполните массив элементами арифметической прогрессии. Её первый 
элемент a1 , разность d и количество элементов n будет задано 
автоматически. Формула для получения n-го члена прогрессии: 
an = a1 + (n-1) * d. ЭЛЕМЕНТЫ ДОЛЖНЫ ВЫВОДИТЬСЯ ПОСТРОЧНО! """

a1, d, n = [int(input()) for _ in range(3)]  # это вставлять в ГБ не нужно

# 1 вариант
ar_progression = [a1 + d * i for i in range(n)]
print(*ar_progression, sep="\n")

# 2 вариант
progression = [a1 + (el - 1) * d for el in range(1, n + 1)]

for el in progression:
    print(el)
