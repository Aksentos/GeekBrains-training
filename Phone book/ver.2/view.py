import text
BORDER = '='

def show_main_menu() -> int:
    print("\t" + text.main_menu[0])
    for k, v in text.main_menu.items():
        if k:
            print(f"{k:>3}. {v}")

    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.mistake_input)


def show_message(message: str):
    print('\n' + BORDER * len(message))
    print(message)
    print(BORDER * len(message) + '\n')

