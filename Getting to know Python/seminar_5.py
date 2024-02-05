"""Задача №1. Последовательностью Фибоначчи"""


def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))  # 55

"""дз 1"""
first = 5
second = 6


def summ(a, b):
    if a == 0:
        return b
    return summ(a - 1, b + 1)


print(summ(first, second))

"""Задача № 2. Хакер Василий
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные."""

grades = [1, 2, 2, 3, 5, 3, 4, 3, 2, 1]


def change_mark(list1):
    max_mark = max(list1)
    min_mark = min(list1)
    for i in range(len(list1)):
        if list1[i] == max_mark:
            list1[i] = min_mark
    return list1


print(change_mark(grades))

"""Задача № 3. Простое число
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)"""


def is_simple(number):
    if number in (1, 2):
        return True
    if number % 2 == 0:
        return False
    for d in range(3, int((number**0.5) + 1), 2):
        if (number % d) == 0:
            return False
    return True


print(is_simple(121)) # False
print(is_simple(4)) # False
print(is_simple(17)) # True

""" Задача № 4
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода)."""


count = int(input("Сколько символов будем вводить?: "))


def turn(number):
    if number == 0:
        return ""
    char = input("Введите символ: ")
    return turn(number - 1) + char


print(turn(count))
