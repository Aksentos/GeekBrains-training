import view
import model
import text


def find_contacts(message):
    search_word = view.input_data(message)
    result = model.find_contact(search_word)
    view.show_contacts(result, text.find_contact_no_result(search_word))
    return True if result else False


def start_app():
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1:
                model.open_phone_book()
                view.show_message(text.phone_book_opened_successfully)
            case 2:
                model.save_phone_book()
                view.show_message(text.phone_book_saved_successfully)
            case 3:
                view.show_contacts(model.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = view.input_data(text.input_new_contact)
                model.add_new_contact(new_contact)
                view.show_message(text.added_new_contact(new_contact[0]))
            case 5:
                find_contacts(text.input_serach_word)
            case 6:
                if find_contacts(text.input_serach_word_for_edit):
                    u_id = int(view.input_data(text.input_id_for_edit))
                    edited_contact = view.input_data(text.edit_contact)
                    name = model.edit_contact(u_id, edited_contact)
                    view.show_message(text.edit_contact_successfully(name))
            case 7:
                if find_contacts(text.input_serach_word_for_delete):
                    u_id = int(view.input_data(text.input_id_for_delete))
                    name = model.delete_contact(u_id)
                    view.show_message(text.delete_contact_success(name))
                # добавить подтверждение/проверку удаления
            case 8:
                # добавить сравнение если книга была изменена
                break
