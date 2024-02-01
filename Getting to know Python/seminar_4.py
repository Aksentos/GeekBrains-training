# Задача 1
"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""

string = "a a a b c a a d c d d"
res = {} # создаем пустой словарь
k = string.split() # убираем пробелы в строке и создаем список элементов
for i in k: # проходим по списку
    if i in res: # если ключ есть в словаре
        print(f'{i}_{res[i]}', end=" ")
    else: # если ключа нет
        print(i, end=" ")
    res[i] = res.get(i, 0) + 1 # в словарь добваляем пару ключ (i) со значением 0 + 1, 
															 # если такой ключ есть увеличивем на 1

# от препода
data = 'a a a b c a a d c d d'
dict_counter = {}
for item in data.split():
    # 1 вариант добваляем пары ключ значение
    if item in dict_counter:
        dict_counter[item] += 1
    else:
        dict_counter[item] = 0
    # 2 вариант
    if item in dict_counter:
        char = f'{item}_{dict_counter[item]}'
    else:
        char = item

    print(char, end=' ')
    dict_counter[item] = dict_counter.get(item, 0) + 1


# Задача 2
"""Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13"""

string = (
    "She sells sea shells on the sea shore The shells"
    " that she sells are sea shells I'm sure.So if she"
    " sells sea shells on the sea shore I'm sure that"
    " the shells are sea shore shells"
)
for i in '.!?:':  
    string = string.replace(i, ' ') # удаляем знаки препинания

res = string.lower().split() # выравниваем все буквы и разбиваем в список
s = set() # создаем множество
for i in res:
    s.add(i) # добавляем элементы списка в множество
print(len(s)) # выводим длинну множества

# Задача 3
''' Необходимо найти и исправить ошибке в коде'''
# Ученик 1
n = 1
max_number = 0
while n != 0:
    n = int(input('Введите число: '))
    if max_number < n:
        max_number = n
print(max_number)

# Ученик 2
n = int(input('Введите число: '))
max_number = n
while n != 0:
    n = int(input('Введите число: '))
    if max_number < n:
        max_number = n
print(max_number)
