from functools import wraps
import time

#sl = 4

def pause(sleep):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(int(sleep))
            return print('Фунция выполняется с задержкой {} секунды!'.format(sleep))
        return wrapper
    return decorator

@pause(3)
def func():
    print('Фунция выполняется с задержкой 2 секунды!')

if __name__ == '__main__':
    func()