import sys
from collections import namedtuple, OrderedDict


from url_shortener import storage


get_connection = lambda: storage.connec('shortener.sqlite')



Action = namedtuple('Action', ('func', 'name'))
actions = OrderedDict()   # словарь, который сохраняет порядок


'''
def menu_action(cmd, name):
    def decorator(func):
        actions[cmd] = Action(func, name)
        return func
    return decorator
'''
def menu_action(cmd, name=None):
    def decorator(func):
        #nonlocal name
        #name = name or func.__doc__
        #actions[cmd] = Action(func, name)
        actions[cmd] = Action(func, name or func.__doc__)
        return func
    return decorator



#@menu_action('1', 'Добавить URL-адрес')
@menu_action('1')  # возьмет из комеентария
def action_add():
    """Добавить URL-адресик"""
    url = input('\nВведите URL-адрес: ')

    with get_connection() as conn:
        storage.add_url(conn, url)


@menu_action('2', 'Найти оригинальный URL-адрес')
def action_find():
    """Найти оригинальный URL-адрес"""


@menu_action('3', 'Вывести все URL-адреса')
def action_find_all():
    """Вывести все URL-адресa"""
    with get_connection() as conn:
        urls = storage.find_all(conn)

    template = '{url[short_url]} - {url[original_url]} - {url[created]}'
    for url in urls:
        #print(url)
        print(template.format(url=url))

@menu_action('m', 'Показать меню')
def action_show_menu():
    """Показать меню"""
    """ удалили
    print('''
1. Добавить URL-адрес
2. Найти оригинальный URL-адрес
3. Вывести все URL-адресa
m. Показать меню
q. Выйти

    ''')
    """
    menu = []

    for cmd, action in actions.items():
        menu.append('{}. {}'.format(cmd, action.name))

    print('\n'.join(menu))



@menu_action('q', 'Выйти')
def action_exit():
    """Выйти"""
    sys.exit(0)


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    ''' удалили
    actions = {
        '1': action_add,
        '2': action_find,
        '3': action_find_all,
        'm': action_show_menu,
        'q': action_exit,
    }
    '''

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)   # не дает ошибку при отсутствии ключа (возвращает None),
                                    # проверяет наличие
        if action:
            #action() # меняем
            action.func()
        else:
            print('Неизвестная команда')

