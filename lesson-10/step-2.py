# Декораторы

from datetime import datetime
from functools import reduce, wraps, lru_cache
import pickle
import time


# todo: 'Простой декоратор. Как применить и где использовать'

def benchmark(func): # функция декоратор всегда принимает 1 аргумент, ту функцию, которую оборачивает
    @wraps(func)
    def wrapper(*args, **kwargs):   #  # функция оберткаб  *args, **kwargs аргументы оборачиваемой функции factorial
        started = time.time()
        resault = func(*args, **kwargs)
        worked = time.time() - started
        print('Функция "{}" выполнилась за  {:f} микросекунд'.format(
            func.__name__, worked * 1e6
        ))
        return resault

    return wrapper #возвращает возвращает

# аналог lru_cache
def cache(func):
    memory = {}   # хранение в кеше

    @wraps(func)
    def wrapper(*args, **kwargs):                               # функция обертка
        key = pickle.dumps((args, sorted(kwargs.items())))      # pickle - переводит любые данные в строку,
                                                                # items -возвращает кортеж, список
        if key not in memory:
            memory[key] = func(*args, **kwargs)

        return memory[key]
        #return  func(*args, **kwargs)  # функция обертка возвращает результат функии, которую обернули

    return wrapper  #cache функию возвращает




@cache
@benchmark
#@cache
def factorial(n):
    return reduce(lambda f, i: f * i, range(1, n + 1)) # reduce -


print(factorial(5))
print(factorial(5))


# todo: Декоратор с параметрами
"""
=====схема======
def decorator_parameters(param1,...paramN)
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            do something
            return func(*args, **kwargs)
        return wrapper
    return decorator
"""

def log(filename):  #декоратор пишет логи работы функции
    template = '''
[{now:%Y-%m-%d %H:%M:%S}]  function: *{func}* called with
    -> positional argument: {args}
    -> keyword argument: {kwargs}
Returns: {resault}
'''
    def decorator(func):
        def wrapper(*args, **kwargs):  # функция обертка из нее возращаем результат работы оригинальной функции
            resault = func(*args, **kwargs)

            with open(filename, 'a') as f:
                f.write(template.format(now=datetime.now(),
                                        func='.'.join((func.__module__, func.__name__)),
                                        args=args,
                                        kwargs=kwargs,
                                        resault=resault))


            return resault
        return wrapper
    return decorator


@log('log.txt')
def tst_func(a, b):
    return a + b



tst_func(2, 2)
tst_func(8, 10)
tst_func(5, 8)











