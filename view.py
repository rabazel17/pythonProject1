import text_fields


def show_menu() -> None:
    print(text_fields.main_menu)



def choice_menu() -> int:
    menu_length = len(text_fields.main_menu.split('\n')) - 1
    while True:
        number = input('Выберите пункт меню: ')
        if number.isdigit() and 0 < int(number) <= menu_length:
            return int(number)
    print(f'Введите число от 1-{menu_length}')

def show_contacts(phone_book: list[dict]):
        if not phone_book:
            print('Телефонная книга пуста или не открыта')
            return False
        else:
            for index, contact in enumerate(phone_book, 1):
                print(f"{index}. {contact.get('name'):<15}"
                  f"{contact.get('phone'):<15}"
                  f"{contact.get('comment'):<15}")


