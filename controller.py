import text
import view
import model

def find_note(phonebook: model.NoteBook()):
    word = view.input_data(text.input_search_word)
    result = phonebook.find_note(word)
    view.show_notes(result, text.notes_not_found(word))

def save_note(phonebook: model.NoteBook()):
    choice = view.save_menu()
    if choice==1:
       phonebook.save_file()
       view.print_message(text.save_successful)

def start_app():
    pb = model.NoteBook()
    pb.open_file()
    view.print_message(text.load_successful)
    while True:
        choice = view.main_menu()
        match choice:
                case 1:
                    view.show_notes(pb.notebook, text.empty_note_book)
                case 2:
                    note= view.add_note(text.new_note)
                    pb.new_note(note)
                    view.print_message(text.new_note_added_successful(note[0]))
                case 3:
                    find_note(pb)
                case 4:
                    find_note(pb)
                    c_id=int(view.input_data(text.input_id_change_contact))
                    c_contact= view.add_note(text.change_contact, pb.notebook[c_id])
                    pb.change_note(c_id, c_contact)
                    view.print_message(text.note_changed_successful(c_contact[0]))
                case 5:
                    find_note(pb)
                    c_id = int(view.input_data(text.input_id_delete_contact))
                    name= pb.delete_note(c_id)[0]
                    view.print_message(text.note_deleted_successful(name))
                case 6:
                    pb.save_file()
                    view.print_message(text.save_successful)
                case 7:
                    save_note(pb)
                    view.print_message(text.good_bay)
                    break

