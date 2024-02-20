phone_book = {}
path = 'GeekBrains-training/Phone book/ver.2/phone_book.txt'
SEPARATOR = ';'

def open_phone_book():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as book:
        data = book.readlines()
        data.sort()  # сортируем книгу по алфавиту при окрытии
    
    for u_id, contact in enumerate(data, 1):
        phone_book[u_id] = contact.strip().split(SEPARATOR)
    print(phone_book)
