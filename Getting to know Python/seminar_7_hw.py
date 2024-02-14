"""Задача № 1. print_operation_table
Напишите функцию print_operation_table(operation, num_rows, num_columns),
которая принимает в качестве аргумента функцию, вычисляющую элемент по
номеру строки и столбца. По умолчанию номер столбца и строки = 9.
Аргументы num_rows и num_columns указывают число строк и столбцов
таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
"ОШИБКА! Размерности таблицы должны быть больше 2!".
Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.
Между элементами должен быть 1 пробел, в конце строки пробел не нужен."""

# вариант 1 (мой)
def print_operation_table(operation, num_rows=9, num_columns=9):
    # проверка на количество строк и столбцов (у гб ошибка, по идее должно быть не меньше 2)
    if num_columns < 2 or num_rows < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
        for i in range(1, num_rows + 1):  # проходимся по строкам
            row = []
            for j in range(1, num_columns + 1):  # проходимся по столбцам
                # производим операцию с числами и добавляем резуьтат в список
                row.append(operation(i, j))
            print(*row)  # выводим получившийся список распаковкой


print_operation_table(lambda x, y: x * y, 3, 3)

# вариант 2 (от alter-mind)
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print('\n'.join([' '.join([str(operation(row, column)) for column in range(1, num_columns + 1)])
                         for row in range(1, num_rows + 1)]))

# вариант 3 (от GB)
def print_operation_table(operation, num_rows=9, num_columns=9):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if j != num_columns :
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n')
        print(''.join([str(i) for i in result[:len(result) - 1]]))


"""Задача № 2. Винни Пух
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько 
легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (т.е. число 
гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в 
виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке 
и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести:
"Количество фраз должно быть больше одной!".
"""

stroka = "за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла"

# вариант 1 (мой)
def rithm(poem: str()):
    string = poem.lower().split(" ")  # получаем список фраз разделённых пробелом
    if len(string) < 2:  # проверка на количество фраз
        return "Количество фраз должно быть больше одной!"
    else:
        result = set()  # создаём множество в которое будем добавлять количество слогов
        for phrase in string:
            let_sum = 0  # счетчик слогов в фразе
            for letter in "ауоыиэяюёе":
                if letter in phrase:
                    let_sum += phrase.count(letter)  # считаем сколько слогов в фразе
            result.add(let_sum)  # добавляем количество слогов в множество
        return "Парам пам-пам" if len(result) == 1 else "Пам парам"  # возвращаем ответ

print(rithm(stroka))  # в решении обязательно нужно вызвать функцию!


# вариант 2 (от alter-mind)
def check_rhythm(string):
    def vowels_count(string):
        count = 0
        vowels = 'ёуеыаоэяию euioa'
        for letter in string:
            if letter in vowels:
                count += 1
        return count

    phrases = string.split()
    if len(phrases) < 2:
        return None
    else:
        check = True
        const_vowels = vowels_count(phrases[0].lower())
        for phrase in phrases[1:]:
            if const_vowels != vowels_count(phrase.lower()):
                check = False
        return check


rhythm = check_rhythm(stroka)
if rhythm is None:
    print('Количество фраз должно быть больше одной!')
elif rhythm:
    print('Парам пам-пам')
else:
    print('Пам парам')


# вариант 3 (от GB)
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
    print('Количество фраз должно быть больше одной!')
else:
    countVowels = []

    for i in phrases:
        countVowels.append(len([x for x in i if x.lower() in vowels]))

    if countVowels.count(countVowels[0]) == len(countVowels):
        print('Парам пам-пам')
    else:
        print('Пам парам')
