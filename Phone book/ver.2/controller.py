import view
import model
import text


def start_app():
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1:
                model.open_phone_book()
                view.show_message(text.phone_book_opened_successfully)
            case 2:
                view.show_message(text.phone_book_saved_successfully)
            case 3:
                model.open_phone_book()
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
