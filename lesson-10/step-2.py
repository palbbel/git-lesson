# Декораторы

from datetime import datetime
from functools import reduce, wraps
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