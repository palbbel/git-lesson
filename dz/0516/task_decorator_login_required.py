import hashlib
from functools import wraps, lru_cache
import pickle


def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()


def file(username, password):
    with open('token.txt', 'w') as f:
        f.write(make_token(username, password))


def get_pass():
    with open('token.txt') as f:
        passw = f.read()
        passw = passw.replace('/n', '')


def login_passw():
    username = input()
    password = input()
    return username, password

def cache(func):
    memory = {}   # хранение в кеше

    @wraps(func)
    def wrapper(*args, **kwargs):                               # функция обертка
        key = 'hash'#pickle.dumps((args, sorted(kwargs.items())))      # pickle - переводит любые данные в строку,
                                                                # items -возвращает кортеж, список
        if key not in memory:
            memory[key] = func(*args, **kwargs)

        return memory[key]
        #return  func(*args, **kwargs)  # функция обертка возвращает результат функии, которую обернули

    return wrapper  #cache функию возвращает

#@cache
#def memo(*args):
#    return
    '''
    if not args:
        return None
    else:
    memory = {}
    key = hash
    memory[key] = hash_pass
    return memory[key]
    '''

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #if not memo():
        n = 3
        while n:
            username, password = login_passw()
            hash_pass = make_token(username, password)
            hash_pass_file = get_pass()
            if hash_pass_file == hash_pass:
                res = func(*args, **kwargs)
                #m = memo(hash_pass)
                return username, password #res
            else:
                n -= 1

        return None
    return wrapper

#@lru_cache(maxsize=30)
@login_required
def f1():
    print('Функция защищена паролем')

@login_required
def f2():
    print('Эта функция тоже защищена паролем')


if __name__ == '__main__':
    username = input()
    password = input()

    f1()
    f2()
    f1()
