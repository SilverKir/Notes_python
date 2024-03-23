import datetime

import text

def main_menu()-> int:
        for n, item in enumerate(text.main_menu):
            if n==0:
                print(item)
            else:
                print(f"\t {n}. {item}")
        while True:
            choice=input(text.main_menu_choice)
            if choice.isdigit() and 0 < int(choice) <len(text.main_menu):
                return int(choice)
            print(f"{text.main_menu_choice.replace(':','')} {text.text_from} 1 {text.text_to} {len(text.main_menu)-1}:")

def save_menu() -> int:
    for n, item in enumerate(text.save_menu):
        if n == 0:
            print(item)
        else:
            print(f"\t {n}. {item}")
    choice = input(text.main_menu_choice)
    if choice.isdigit() and 0 < int(choice) < len(text.save_menu):
        return int(choice)

def show_notes(note_book: dict[int,list[str]], error_message: str):
    max_size=list(map (lambda x: len(max(x,key=len)), list(zip(*note_book.values()))))
    if note_book:
        print('\n' + '=' * (sum(max_size)+9))
        for n, contact in note_book.items():
            print (f"{n:>3}. {contact[0]:<{max_size[0]}} {contact[1]:<{max_size[1]}} {contact[2]:<{max_size[2]}}")
        print('=' * (sum(max_size)+7) + '\n')
    else:
        print_message(error_message)

def print_message(massage:str):
    print('\n'+'='*len(massage))
    print(massage)
    print('='*len(massage)+'\n')

def add_note(massage: list[str], note: list[str] = None):
    note=note if note else ['', '','']
    for n, mes in enumerate(massage):
        field=input(mes)
        note[n]=field if field else note[n]
    note[n+1]=str(datetime.datetime.now())
    return note

def input_data (message: str)->str:
    return input(message)





