
ll = 'siohosidhio'

memory = {}

if not memory:

    key = 'ggg'

    memory['ggg'] = ll
#memory = {}

print(memory['ggg'])


import hashlib
from functools import wraps

memory = {}

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
        return passw


def memo(*args):
    if not args:
        return
    else:
        return args['hash']


def mem(nash_val):
    memory = {}
    key = 'hash'
    memory[key] = nash_val
    return memory

def login_passw():
    username = input()
    password = input()
    return username, password


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not memory:
            n = 3
            while n:
                username, password = login_passw()
                hash_pass = make_token(username, password)
                hash_pass_file = get_pass()
                if hash_pass_file == hash_pass:
                    memory['hash'] = hash_pass
                    res = func(*args, **kwargs)
                    return res
                else:
                    n -= 1
        else:
            if memory['hash'] == get_pass():
                res = func(*args, **kwargs)
                return res
        return None
    return wrapper


@login_required
def f1():
    print('Функция защищена паролем')


@login_required
def f2():
    print('Эта функция тоже защищена паролем')


if __name__ == '__main__':


    f1()
    f2()
    f1()
