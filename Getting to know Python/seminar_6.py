""" Задача № 1
Даны два массива чисел. Требуется вывести те элементы первого
массива (в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит  число N -
количество элементов в первом массиве, затем N чисел -
элементы массива. Затем число M - количество элементов во
втором массиве. Затем элементы второго массива
"""

import random as r # берем модуль рандом для наполнения списков
from string import printable  # все печатаемые элементы

print(
    list1 := [
        r.choice(list(printable))
        for _ in range(int(input("Введите количество элементов 1 списка: ")))
    ]
)
print(
    list2 := [
        r.choice(list(printable))
        for _ in range(int(input("Введите количество элементов 2 списка: ")))
    ]
)


# 1 вариант
for i in list1:
    if i not in list2:
        print(i, end=" ")


# Задача 2
""" Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел."""


import random # берем модуль рандом для наполнения списка

print(
    list1 := [
        random.randint(1, 9)
        for _ in range(int(input("Введите количество элементов: ")))
    ]
)

# 1 вариант
counter = 0
array_big_numbers = []
for i in range(1, len(list1) - 1):
    if list1[i - 1] < list1[i] > list1[i + 1]:
        counter += 1
        array_big_numbers.append(list1[i])
print("Количество элементов:", counter, "Список этих элементов:", array_big_numbers)

# 2 вариант
kol_el = int(input("Введите количество элементов: "))
count = 0
spisok = [random.randint(0, 10) for _ in range(kol_el)]

count = [i for i in range(1, kol_el - 1) if spisok[i - 1] < spisok[i] > spisok[i + 1]]
print(spisok)
print(len(count))


#  Задача 2
""" Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
"""

import random

print(
    list_1 := [
        random.randint(0, 10)
        for _ in range(int(input("Введите количество элементов: ")))
    ]
)
counter = 0

#  1 вариант (вроде работает, но это не точно)
for i in list_1:
    list_1.remove(i)
    if i in list_1:
        counter += 1
        list_1.remove(i)
print(counter)

# 2 вариант
counter = 0
for i in set(list_1):
    counter += list_1.count(i) // 2
print(counter)

# 3 вариант
print(sum([list_1.count(item) // 2 for item in set(list_1)]))

# Задача 3
"""Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
"""
# 1 вариант
import datetime  # для сравнения скорости работы кода
start = datetime.datetime.now()

LIMIT = 10000

# сумма делителей числа
def sum_dev(number):
    result = 0
    for dev in range(1, number // 2 + 1):
        if not number % dev:
            result += dev
    return result


for num in range(1, LIMIT):
    second_num = sum_dev(num)
    if num == sum_dev(second_num) and num > second_num:
        print(num, second_num)
finish = datetime.datetime.now()
print("time code = ", finish - start) # для сравнения скорости работы кода

# 2 вариант (самый оптимальный)
start = datetime.datetime.now()


def sums(pars):
    my_res = 1
    for test_numbers in range(2, int(pars**0.5) + 1):
        if pars % test_numbers == 0:
            my_res += test_numbers + pars // test_numbers
    return my_res


for numbers in range(1, LIMIT):
    first_sum = sums(numbers)
    sum_second = sums(first_sum)
    if sum_second == numbers and first_sum > sum_second:
        print(numbers, first_sum)
finish = datetime.datetime.now()
print("time code = ", finish - start)

# 3 вариант
start = datetime.datetime.now()

for n in range(1, LIMIT + 1):
    summ = sum([i for i in range(1, n) if n % i == 0])
    first_sum = summ
    summ = sum([i for i in range(1, first_sum) if first_sum % i == 0])

    if n < first_sum and summ == n < LIMIT:
        print(n, first_sum)
finish = datetime.datetime.now()
print("time code = ", finish - start)
