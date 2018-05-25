from functools import wraps
import time


def pause(sleep):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(int(sleep))
            #func()
            return print('Фунция выполняется с задержкой {} секунды!'.format(sleep))
        return wrapper
    return decorator

@pause(2)
def func():
    print('Фунция выполняется с задержкой 2 секунды!')

if __name__ == '__main__':
    func()


d = [1, 2, 3, 5]
print(type(d))
if type(d) is tuple:
    print('ok')
else: print('no')


def hh(*args):
    c = args
    print(c)

hh('ett', 'er')

from collections import namedtuple

def func1():
    return 'Python', 'is', 'programming language'

cor = ('a', 'b', 'c')
#Point = namedtuple('Point', ('a', 'b', 'c'))
#r = Point(func1())

#Point = namedtuple('Point', cor, ['ee','rr','tt'])

#c = func1()
#for x in func1(): print(x)
#print(func1())



def func3():
    return 'Python', 'is', 'programming language'

print(', '.join(str(i) for i in func3()))


def fibonacci(t):        # генератор (а не функция, т.к. оператор return заменён на yield)
    #k = max
    a, b = 1, 1
    while t:
        yield a            # return a, + запоминаем место рестарта для следующего вызова
        a, b = b, a + b
        t -= 1

for n in fibonacci(10):   # используем генератор fibonacci() как итератор
    print (n)