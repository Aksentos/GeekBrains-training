"""
✔Три друга взяли вещи в поход. Сформируйте словарь, где ключ
— имя друга, а значение — кортеж вещей. 
Ответьте на вопросы:
✔Какие вещи взяли все три друга 
✔Какие вещи уникальны, есть только у одного друга 
✔Какие вещи есть у всех друзей кроме одного и имя того, 
у кого данная вещь отсутствует 
✔Для решения используйте операции с множествами. Код 
должен расширяться на любое большее количество друзей.
"""

friends = {
    "Ivan": ("matches", "food", "games", "umbrella"),
    "Bob": ("food", "games", "tent"),
    "Jack": ("food", "tent",  "phone"),
    # "Tom": ("tent", "shovel"),
}

# task 1 Какие вещи взяли все три друга
things = set()
for i in friends.values():
    things.update(set(i))  # наполняем множество уникальных наименований
print('В поход взяли:', *things)

# task 2 Какие вещи уникальны, есть только у одного друга
diff_things = []  # список для уникальных вещей
things = []  # список для перебора всех вещей
for value in friends.values():
    for i in value:
        if i not in diff_things:
            diff_things.append(i)  # добавляем вещь в уникальный список
        if i in things:
            diff_things.remove(i)  # если такая вещь есть в общем списке, удаляем её
        if i not in things:
            things.append(i)  # наполняем список всех вещей
print('Вещи которые взял кто-то один:', *diff_things)  # выводим список уникальных вещей

# task 3 Какие вещи есть у всех друзей кроме одного и имя того,
# у кого данная вещь отсутствует
all_things = []  # список для всех вещей и сколько их взяли
things = set()  # множество уникальных наименований как в task 1
for i in friends.values():
    things.update(set(i))  # наполняем множество уникальных наименований

for value in friends.values():
    for i in value:
        all_things.append(i)  # наполняем список для всех вещей и сколько их взяли

for k, v in friends.items():
    for i in things:
        if (  # проверка, если вещь взяли все кроме одного
            all_things.count(i) == len(friends) - 1
        ):
            if i not in v:
                print(f"{k} не взял {i}")  # выводим кто не взял вещь
