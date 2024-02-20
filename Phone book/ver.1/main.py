"""
Что умеет справочник:
V 1. Открыть справочник* (происходит при обращении к файлу)
V 2. Сохраниить  справончик* (происходит при выполнении функций)
V 3. Показть все контакты
V 4. Создать контакт
V 5. Найти контакт
V 6. Изменить контакт 
V 7. Удалить контакт
V 8. Выход
"""


# Создать контакт
def add_contact():
    book = open("phone_book.txt", "a+", encoding="utf-8")
    fio = input("Введите имя: ")
    number = input("Введите номер: ")
    comment = input("Введите комментарий: ")
    book.write(f"{fio},{number},{comment}\n")
    book.close()
    print(f"Новый контакт {fio},{number},{comment} добавлен")


# Показть все контакты
def all_contacts():
    with open("phone_book.txt", "r+", encoding="utf-8") as book:
        return book.readlines()


# обработка несуществующего контакта для поиска
def not_contact():
    print("Такого контакта нет, хотите его созадть?")
    add = input("Введите 1 если Да, 2 - если Нет →  ").lower()
    if add == "1":
        add_contact()


# Сортировка книги по алфавиту
def sort_book():
    contact_list = [contact for contact in all_contacts()]
    contact_list.sort()
    file = open("phone_book.txt", "w", encoding="utf-8")
    for contacts in contact_list:
        file.write(str(contacts))
    file.close()


# Найти контакт
def find_contact():
    book = all_contacts()

    flag = False
    if (
        what := input(
            "Что будем искать?\nУкажите номер из списка: 1-фио, 2-номер, 3-комментарий → "
        )
    ) == "1":
        fio = input("Введите имя: ")
        for line, contact in enumerate(book):
            if fio in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    elif what == "2":
        number = input("Введите номер: ")
        for line, contact in enumerate(book):
            if number in contact.lower().split(",")[1]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    elif what == "3":
        comment = input("Введите комментарий: ")
        for line, contact in enumerate(book):
            if comment in contact.lower().split(",")[2]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    else:
        print("Нужно выбрать 1, 2 или 3")
        find_contact()


# Изменить контакт
def change_name():
    book = all_contacts()
    flag = False
    if (
        what := input(
            "Что будем менять?\nУкажите номер из списка: 1-фио, 2-номер, 3-комментарий? → "
        )
    ) == "1":
        fio = input("Кого будем менять: ").lower()
        for line, contact in enumerate(book):
            if fio in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")

                flag = True
        if flag:
            name_id = int(input("введите № id кого меняем?: "))
            new_name = input("Введите новое имя для контакта: ")
            change_contact = book[name_id]
            book[
                name_id
            ] = f'{new_name},{change_contact.split(",")[1]},{change_contact.split(",")[2]}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()

    elif what == "2":
        number = input("Введите номер: ").lower()
        for line, contact in enumerate(book):
            if number in contact.lower().split(",")[1]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if flag:
            name_id = int(input("введите № id кого меняем?: "))
            number = input("Введите новый номер телефона: ")
            change_contact = book[name_id]
            book[
                name_id
            ] = f'{change_contact.split(",")[0]},{number},{change_contact.split(",")[2]}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()

    elif what == "3":
        comment = input("Введите комментарий: ").lower()
        for line, contact in enumerate(book):
            if comment in contact.lower().split(",")[2]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if flag:
            name_id = int(input("введите № id кого меняем?: "))
            comment = input("Введите новый комментарий для контакта: ")
            change_contact = book[name_id]
            book[
                name_id
            ] = f'{change_contact.split(",")[0]},{change_contact.split(",")[2]},{comment}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()
    else:
        print("Нужно выбрать 1, 2 или 3")
        change_name()
    content()


# Удалить контакт
def delete_contact():
    book = all_contacts()
    flag = False
    fio = input("Кого будем удалять?: ").lower()
    for line, contact in enumerate(book):
        if fio in contact.lower().split(",")[0]:
            print("id =", line, *contact.split(","), end="")
            flag = True
    if flag:
        name_id = int(input("введите № id кого удаляем → "))
        print(f"{book.pop(name_id)} удален!")
        file = open("phone_book.txt", "w", encoding="utf-8")
        for contacts in book:
            file.write(str(contacts))
        file.close()
    else:
        not_contact()


# Работа справочника
def content():
    with open("phone_book.txt", "a+", encoding="utf-8") as f:
        f.close()
    while True:
        menu = {
            1: "1 → Показать все контакты",
            2: "2 → Создать новый контакт",
            3: "3 → Найти контакт",
            4: "4 → Изменить контакт",
            5: "5 → Удалить контакт",
            6: "6 → Выйти из программы",
            7: ("*" * 26),
        }

        print("\n", "*" * 7, "Содержание", "*" * 7)
        print(*menu.values(), sep="\n")
        point = input("\nВведите № пункта → ")
        if point == "1":  # Показать все контакты
            print("\nСписок всех контактов:")
            print(*all_contacts(), sep="")  # выводим отсортированный по алфавиту справочник
            
        elif point == "2":  # Создать новый контакт
            add_contact()
            
        elif point == "3":  # Найти контакт
            find_contact()
            
        elif point == "4":  # Изменить контакт
            change_name()
            
        elif point == "5":  # Удалить контакт
            delete_contact()
            
        elif point == "6":  # Выйти из программы
            sort_book()  # Сортируем книгу по алфавиту перед закрытием
            break
        else:
            print("Ошибка ввода, выберите один из пунктов")
            


# Запуск программы
if __name__ == "__main__":
    content()
