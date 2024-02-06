"""Крестики нолики"""
# Пока компьютер можно обыграть, и нет проверку на ничью.
game_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Игровое поле

player_1 = "x"
player_2 = "o"
steps = []  # список ходов
win = 0

# Какие поля должны быть заполнены для победы
win_conditinons = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [7, 5, 3],
    [1, 4, 7],
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

# Заполняем победные поля элементами
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
    try:  # Проверка ввода
        step = int(step)
    except:
        print("\nНеверный ввод!")  
    if step not in range(1, 10):  # Проверка ввода
        print("\nВведите число от 1 до 9\n")
        game(player, list)
    elif step in steps:  # Проверка ввода
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
    if isinstance(step, int):  # type(step) == int
        steps.append(step)  # обновляем список ходов
    win_cond(step, player)  # обновляем победные списки

# ходы компьютера (тут можно еще переделать)
def comp_step(comp=player_2, player=player_1):
    for i in range(len(win_conditinons)):
        for j in range(len(win_conditinons[i])):
            if win_conditinons[i].count(player) == 2:
                for win_conditinons[i][j] in win_conditinons[i]:
                    if isinstance(win_conditinons[i][j], int):  # type(win_conditinons[i][j]) == int:
                        steps.append(win_conditinons[i][j])
                        step_c = win_conditinons[i][j]
                        for n in range(3):
                            for m in range(3):
                                if game_field[n][m] == win_conditinons[i][j]:
                                    game_field[n][m] = comp
                                    win_cond(step_c, comp)
                                    return

    for i in range(len(win_conditinons)):
        for j in range(len(win_conditinons[i])):
            if win_conditinons[i][j] == player:
                a = win_conditinons[i][(j + 1) % len(win_conditinons[i])]
                b = win_conditinons[i][(j - 1) % len(win_conditinons[i])]
                if isinstance(a, int):  # type(a) == int:
                    steps.append(a)
                    step_c = a
                    for n in range(3):
                        for m in range(3):
                            if game_field[n][m] == a:
                                game_field[n][m] = comp
                                win_cond(step_c, comp)
                                return
                elif isinstance(b, int):  # type(b) == int:
                    steps.append(b)
                    step_c = b
                    for n in range(3):
                        for m in range(3):
                            if game_field[n][m] == b:
                                game_field[n][m] = comp
                                win_cond(step_c, comp)
                                return


# Запускаем игру

partner = input(
    "Против кого будем играть? Введи 1 если против игрока или 2 если против компьютера: "
)
if partner == "2":
    comp = True
    print("\nИграем против компьютера!\n")
else:
    comp = False
    print("\nИграем против игрока!\n")

while win == False:
    game(player_1, game_field)
    wins(player_1)
    if win:
        break
    if comp:
        comp_step()  # играем с компьютером
    else:
        game(player_2, game_field)  # играем с человеком
    wins(player_2)
