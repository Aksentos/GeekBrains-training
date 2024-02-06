"""Крестики нолики"""
# Пока игра расчитана на 2 игроков без ИИ.
game_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Игровое поле

player_1 = "x"
player_2 = "o"
steps = []  # список ходов
win = 0

# Какие поля должны быть заполнены для победы
win_conditinons = [
    [1, 2, 3],
    [3, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [7, 5, 3],
    [1, 3, 7],
    [2, 5, 8],
    [3, 6, 9],
]

# Проверка на победу
def wins(player):
    global win
    for item in win_conditinons:
        if item.count(player) == 3: # если в списке все элементы "х" или "о"
            print(f"\nВыиграл {player}\n")
            win = True
            return win
    return win

# Заполняем победные списки элементами
def win_cond(num, player):
    for i in range(len(win_conditinons)):
        for j in range(len(win_conditinons[i])):
            if num == win_conditinons[i][j]:
                win_conditinons[i][j] = player

# Вывод текущего игрового поля
def field(lsit):
    print("*" * 13)
    for i in lsit:
        print(f"* {i}", end=" *\n")
    print("*" * 13)

# ход игры
def game(player, list):
    field(list)  # Вывод текущего игрового поля
    step = input(f"Куда ставим {player}?: ")  # спрашиваем в какую ячейку ставим знак
    try:  # проверка ввода
        step = int(step) 
    except:
        print("\nНеверный ввод\n")
        game(player, list)
    if step not in range(1, 10):  # проверка ввода
        print("\nНеверный ввод, выберите другое место\n")
        game(player, list)
    elif step in steps:  # проверка ввода
        print("\nЭто поле уже занято, выберите другое место\n")
        game(player, list)
    elif step == 1:
        game_field[0][0] = player
    elif step == 2:
        game_field[0][1] = player
    elif step == 3:
        game_field[0][2] = player
    elif step == 4:
        game_field[1][0] = player
    elif step == 5:
        game_field[1][1] = player
    elif step == 6:
        game_field[1][2] = player
    elif step == 7:
        game_field[2][0] = player
    elif step == 8:
        game_field[2][1] = player
    elif step == 9:
        game_field[2][2] = player

    steps.append(step)  # обновляем список ходов
    win_cond(step, player)  # обновляем победные списки
    

# Запускаем игру
while win == False:
    game(player_1, game_field)
    wins(player_1)  # проверка на победу
    if win == True:
        break
    game(player_2, game_field)
    wins(player_2)  # проверка на победу
