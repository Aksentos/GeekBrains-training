"""
1. Открыть справочник*
2. Сохраниить  справончик*
V 3. Показть все контакты
V 4. Создать контакт 
V 5. Найти контакт
? 6. Изменить контакт
7. Удалить контакт
8. Выход"""


# phone_book 
# 1,Шамиль Мамедов,+79999999999,ментор ГБ
# 2,Ivanov Bob,+79997776655,comment888
# 3,Ivan,888888,true
# 4,Kirill,78965413333,prepod
# 5,Lotus,9993333111,auto



# Создать контакт
def add_contact():
    book = open("phone_book.txt", "r+", encoding="utf-8")
    fio = input("Введите имя: ")
    number = input("Введите номер: ")
    comment = input("Введите комментарий: ")
    # phone_book[number] = [fio, comment]
    ids = len(book.readlines()) + 1
    book.write(f"{ids},{fio},{number},{comment}\n")
    book.close()


# Показть все контакты
def all_contacts():
    with open("phone_book.txt", "r+", encoding="utf-8") as book:
        return book.readlines()


# Найти контакт
def find_contact():
    book = all_contacts()
    if (
        what := input("Что будем искать?\n(Выбирите 1-фио, 2-номер, 3-комментарий)?: ")
    ) == "1":
        fio = input("Введите имя: ")
        for contact in book:
            if fio in contact.lower().split(",")[1]:
                print(contact)

    elif what == "2":
        number = input("Введите номер: ")
        for contact in book:
            if number in contact.lower().split(",")[2]:
                print(contact)
    elif what == "3":
        comment = input("Введите комментарий: ")
        for contact in book:
            if comment in contact.lower().split(",")[3]:
                print(contact)
    else:
        print("Повторите выбор!")
        find_contact()


# Изменить контакт
def change_name():
    book = all_contacts()

    if (
        what := input("Что будем менять?\n(Выбирите 1-фио, 2-номер, 3-комментарий)?: ")
    ) == "1":
        fio = input("Кого будем менять: ").lower()
        for contact in book:
            if fio in contact.lower().split(",")[1]:
                print(contact)
        change_name_id = input('введите № id кого меняем?: ')
        new_name = input('Введите новое имя для контакта: ')
        contact = contact.lower().split(",")[1]
                


    elif what == "2":
        number = input("Введите номер: ").lower()
        for contact in book:
            if number in contact.lower().split(",")[2]:
                print(contact)
    elif what == "3":
        comment = input("Введите комментарий: ").lower()
        for contact in book:
            if comment in contact.lower().split(",")[3]:
                print(contact)
    else:
        print("Повторите выбор!")
        change_name()



