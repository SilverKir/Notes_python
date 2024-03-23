main_menu=['Главное меню',
           'Открыть файл записной книжки',
           'Сохранить файл записной книжки',
           'Показать заметку',
           'Создать заметку',
           'Найти заметку',
           'Изменить заметку',
           'Удалить заметку',
           'Выход']

main_menu_choice="Выберете пункт меню: "

text_from="от"
text_to="до"

empty_note_book = "Записная книжка пуста или не открыта!"
load_successful= "Записная книжка успешно загружена"
save_successful= "Записная книжка успешно сохранена"

new_note = ["Введите заголовок заметки: ",
                "Введите заметку: "]

def new_note_added_successful(name: str) -> str:
    return f'Заметка {name} успешно добавлена'

input_search_word="Введите слово для поиска: "

def notes_not_found(word:str)-> str:
    return f"Контакты, содержащие слово {word} не найдены"

input_id_change_contact="Введите ID заметки, который хотите изменить: "

change_contact=["Введите новый заголовок или Enter, чтобы оставить без изменений: ",
              "Введите новую заметку или Enter, чтобы оставить без изменений: "]

def note_changed_successful(name: str) -> str:
    return f'Заметка {name} успешно изменена'

input_id_delete_contact="Введите ID заметки, которую хотите удалить: "

def note_deleted_successful(name: str) -> str:
    return f'Заметка {name} успешно удалена'

good_bay="До свидания!"
