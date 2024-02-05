"""
Написать игру крестики нолики для игры с пк
"""

import tkinter as tk


window = tk.Tk()  # открывает окно приложения
window.title("Крестики vs. нолики")


# кнопка закрывает окно приложения
def button_quit(frame):
    quit = tk.Button(
        master=frame,
        text="quit",
        relief=tk.RAISED,
        borderwidth=3,
        command=window.destroy,
    )
    return quit


# кнопка Х,О
def button_x(frame):
    btn = tk.Button(
        master=frame,
        text=" ",
        width=10,
        height=5,
        bg="blue",
        fg="yellow",
        # смена кнопки (пока не работает)
    )
    return btn


# смена кнопки (пока не работает)
def change_button(self):
    if self["text"] == " ":
        self["text"] = "X"
    elif self["text"] == "X":
        self["text"] = "O"
    elif self["text"] == "O":
        self["text"] = " "


# кнопка сброса (функции еще нет)
def button_reset(frame):
    reset = tk.Button(master=frame, text="reset", relief=tk.RAISED, borderwidth=3)
    return reset


# заполнение игрового поля кнопками
for i in range(4):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=75)
    for j in range(3):
        frame_field = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame_field.grid(row=i, column=j, padx=3, pady=3)
        if i < 3:
            btn = button_x(frame_field)  # добавляем кнопки для Х О
            btn.configure(command=change_button(self=btn)) ## НЕ РАБОТАЕТ!!!!
            btn.pack()
        if i == 3:
            if j == 2:
                button_quit(frame_field).pack()  # добавляем кнопку выхода из приложения
            elif j == 1:
                button_reset(frame_field).pack()  # добавляем кнопку сброса игры
            else:
                pass  # добавляем еще какую-нибудь кнопку слева снизу


window.mainloop()  # указывает Python, что нужно запустить цикл событий Tkinter
