# Задача 1. Пересечение двух неупорядоченных наборов целых чисел
"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества."""
import random

var1 = input("Введите 2 числа через пробел: ")
var2 = ""
var3 = ""
# формируем строки из чисел (эта часть для сдачи ДЗ не нужна)
for _ in range(int(var1.split()[0])):
    var2 = var2 + (str(random.randint(0, 9))) + " "
for _ in range(int(var1.split()[1])):
    var3 = var3 + (str(random.randint(0, 9))) + " "

# 1 вариант
res = set()
for i in var2.split():
    if i in var3.split():
        res.add(i)
print(*sorted(res))

# 2 вариант
print(*sorted(set(var2.split()).intersection(var3.split())))

# Задача 2. Черника
"""Урожайность черничных кустов представлена в виде списка arr, 
где arr[i] - это урожайность (количество ягод) i-го куста.

В фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Каждый собирающий модуль может собрать ягоды с одного куста и с двух
соседних кустов. Собирающий модуль находится перед определенным кустом, и он
может выбирать, с какого куста начать сбор ягод.

Ваша задача - написать программу, которая определит максимальное число ягод,
которое может собрать один собирающий модуль за один заход, 
находясь перед некоторым кустом грядки.
"""
# часть с созданем списка для сдачи ДЗ не нужна
import random

bushes = int(input("Введите число кустов от 1 до 1000: "))
arr = []
for _ in range(bushes):
    arr.append(random.randint(1, 9))
print(arr)  # выводит грядку с количеством ягод на каждом кусте
# в ГБ следующая проверка не нужна т.к. в тестах нет меньше 4 кустов
if len(arr) < 4:  # проверка на количество кустов на грядке
    max_blueberry = sum(arr)

# 1 вариант
max_blueberry = 0  # счетчик сбора ягод
for i in range(len(arr) - 2):
    if arr[i] + arr[i - 1] + arr[i + 1] > arr[i] + arr[i + 1] + arr[i + 2]:
        # высчитываем количество ягод за 1 проход
        blueberry = arr[i] + arr[i - 1] + arr[i + 1]
        if blueberry > max_blueberry:
            max_blueberry = blueberry  # узнаем максимально количество ягод за 1 проход
# сравниваем с проходом где 1й куст будет последним в проходе
# почему-то тестер ГБ принимает решение без этой проверки
if max_blueberry < (arr[-2] + arr[-1] + arr[0]):
    print(arr[-2] + arr[-1] + arr[0])
else:
    print(max_blueberry)

# 2 вариант с помощью срезов и функции sum()
max_blueberry = arr[-2] + arr[-1] + arr[0]
for i in range(len(arr) - 1):
    if i == 0:
        blueberry = arr[-1] + arr[0] + arr[1]
    elif sum(arr[i - 1 : i + 2]) > sum(arr[i : i + 3]):
        blueberry = sum(arr[i - 1 : i + 2])
    if blueberry > max_blueberry:
        max_blueberry = blueberry
print(max_blueberry)

# 3 вариант через вычисление max(list())
max_blueberry = list()
for i in range(len(arr)):
    max_blueberry.append(arr[i - 2] + arr[i - 1] + arr[i])
print(max(max_blueberry))

# 4 вариант черех pop() insert()
for in list_1:
    list_1.insert(0, list_1.pop(-1))
    plus = list_1[0] + list_1[1] + list_1[2]
    result = max(result, plus)
print(result)

# 5 вариант через проход списка в цикле
max_blueberry = []
for i in range(len(arr)):
    max_blueberry.append(arr[(i - 1) % len(arr)] + arr[i % len(arr)] + arr[(i + 1) % len(arr)]) 
print(max(max_blueberry))
