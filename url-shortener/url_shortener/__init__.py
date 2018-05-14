import sys

from url_shortener import storage


get_connection = lambda: storage.connec('shortener.sqlite')

def action_add():
    """Добавить URL-адрес"""
    url = input('\nВведите URL-адрес: ')

    with get_connection() as conn:
        storage.add_url(conn, url)



def action_find():
    """Найти оригинальный URL-адрес"""


def action_find_all():
    """Вывести все URL-адресa"""
    with get_connection() as conn:
        urls = storage.find_all(conn)

    template = '{url[short_url]} - {url[original_url]} - {url[created]}'
    for url in urls:
        #print(url)
        print(template.format(url=url))


def action_show_menu():
    """Показать меню"""
    print('''
1. Добавить URL-адрес
2. Найти оригинальный URL-адрес
3. Вывести все URL-адресa
m. Показать меню
q. Выйти

    ''')


def action_exit():
    """Выйти"""
    sys.exit(0)


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    actions = {
        '1': action_add,
        '2': action_find,
        '3': action_find_all,
        'm': action_show_menu,
        'q': action_exit,
    }

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)   # не дает ошибку при отсутствии ключа (возвращает None),
                                    # проверяет наличие
        if action:
            action()
        else:
            print('Неизвестная команда')

