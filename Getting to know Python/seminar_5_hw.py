""" Задача № 1. Возведение в степень
Напишите функцию f, которая на вход принимает два числа 
a и b, и возводит число a в целую степень b с помощью рекурсии.
Функция не должна ничего выводить, только возвращать значение."""


def f(a, b):
    if b == 0:
        return 1
    return f(a, b - 1) * a


print(f(2, 3))  # 8

""" Задача № 2. Рекурсивная сумма
Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
двух целых неотрицательных чисел. Из всех арифметических операций 
допускаются только +1 и -1. Также нельзя использовать циклы.
Функция не должна ничего выводить, только возвращать значение.
"""


def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return sum(a - 1, b + 1)


print(sum(2, 2))  # 4
print(sum(2, 0))  # 2
