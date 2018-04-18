# Каа объявить функцию
# Функция это блок кода, который можно вызывать многократно


def hello():
    print('Hello')

hello()  # вызов функции


say_hello = hello
say_hello()


# Зачем фунуции аргументы

def hello_username(name):
    print('Hello,', name)

hello_username('Павел')


def summa(a, b):
    print(a + b)

summa(1, 3)


# ередача значений аргументов по ссылке
def pars(src, output):
    src = src.strip('.')  # обрезает точки

    for i in src.split(): # split - разбиение по разделителю
        output.append(i)

src = 'Pythin is programming language.'
lst = []

print(src, lst)
pars(src, lst)
print(src, lst)


# Задание аргумента по умолчанию
def powww(x, p=2):
    print(x ** p)

powww(5)
powww(5, 3)


def hello_username_default(name='Вася'):
    print('Hello,', name)

hello_username_default()


def f(i, l=[]):
    l.append(i)
    print(i)


f(3)
f(1, [2])

def ff(i, l=None):
    l = l if i is not None else []  # так не делать
    l = l or [] # для аргументов изменяемго типа



# Как вернуть значение из функии
def minus(a, b):
    return a - b

r = minus(1, 2)
print(r)


"""
Проверять надо на ложь (if). Избавлятся от else
"""

def f2():
    return 1, 2, 3  # скобки говорят о возвращении кортежа (1, 2, 3)

a, b, c = f2()

# Переменное количество переменных в описании функции
def demo(*args):
    """
    args - это кортеж:
    """
    print(args, type(args))

demo(1, 2, 3, 4)
demo(10, 20, True)

def demo1(i, *args):
    """
    args - это кортеж:
    """
    print(args, type(args))

demo1(1, 2, 3, 4)
demo1(10, 20, True)


def demo2(i, j=0, *args):
    """
    args - это кортеж:
    """
    print(args, type(args))

demo2(1, 2, 3, 4)
demo2(10, 20, True)


def demo3(i, *args, **kwargs):
    """
    args - это кортеж:
    kwargs - это словарь
    """
    print(args, type(args))
    print(kwargs, type(kwargs))

demo3(1, 2, 3, j=4)
demo3(10, 20, k=True, e=456)

def demo4(i=1, j=1, *args):
    print(i, j, args)

demo4(2, 2, 3, 5)


def demo5(i, *args, j=1, **kwargs):  # во втором питоне будет ошибка
    print(i, j, args, kwargs)

demo5(2, 5, 5, j=4)
demo5(2, 5, 5, j=4, d={})


# Переменное количество переменных при вызове функции
def f4(i, j, k, a=None, b=None, c=None):
    print(i, j, k)
    print(a, b, c)

args = [1, 2, 3]
kwargs = {
    'a': 10,
    'b': 20,
    'c': 30
    }

f4(*args, **kwargs)



# Анонимная функция
sqrt = lambda x: x ** 0.5
# lambda: pass
# lambda x, y: pass
print(sqrt(9))

def f5(x, cb):
    return cb(x)

print(f5(25, sqrt))
print(f5(25, lambda x: x ** 0.5))

"""

"""


# Замыкание - в одной функции описываем другую функцию
def trim():
    # область видимости локальная фукции trim
    # Замкнутая облась - живет пока существует spaces_trim
    def f():
        # область видимости локальная фукции f
        pass
    return f

spaces_trim = trim()
print(spaces_trim)

# Функция каррирования ()частичная
def trim2(chars=None):
    # область видимости локальная фукции trim
    # Замкнутая облась - живет пока существует spaces_trim
    def f22(s):
        # область видимости локальная фукции f
        return s.strip(chars)
    return f22

spaces_trim2 = trim2()
slashes_trim2 = trim2('/\\')

print(spaces_trim2('    Hello        '))
print(slashes_trim2('////url//\\\\//'))



# Рекурсивная функция (функция вызывает саму себя)
# 5! = 1 * 2 * 3 * 4 * 5
def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)

print(factorial(5))



