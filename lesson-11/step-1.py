# Итераторы
# Генераторы
# Генераторы списков, словарей, множеств
# Генераторы выражений


# todo: Итераторы

s = 'Linus Torvalds'
lst = [1, 2, 3, 4, 5]
d = {
    'name': 'Linus Torvalds',
    'age': 47,
    'is_developer': True,
}


"""
__iter__() => return Iterator
__next__() => Iterator
"""
it = iter(s)       # __iter__()
print(type(it))
print(next(it))  # строки перебираются посимвольно  # __next__()
print(next(it))


it = iter(lst)
print(type(it))
print(next(it))


it = iter(d)
print(type(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it))



def for_emitator(seq):
    it = iter(seq)

    while 1:
        try:
            i = next(it)
            print(i)
        except StopIteration:
            break

for_emitator(s)
for_emitator(lst)
for_emitator(d)



with open(__file__) as f:
    print(type(f))
    for i in f:
        pass



# todo: Генераторы

def generator():
    print('Шаг №1')
    yield 1         # возвращает результат, ставит на паузу генератор
    print('Шаг №2')
    yield 2
    print('Шаг №3')


gen = generator()
print(type(gen))    # ничего не вывелось про Шаги
                    # генератор останавливается пока не будет вызван next
                    # return не нужен

print(next(gen))    # Шаг №1
                    # 1

print(next(gen))    # Шаг №2
                    # 2

#print(next(gen))    # StopIteration


def countdown(n):
    print("Генератор стартовал")

    while n:
        yield n
        n -= 1


for i in countdown(3):
    print('Значение счетчика: {}'.format(i))



# todo: Генераторы списков словарей множеств

"""
[expression for item1 in iterable1 if condition1
            for item2 in iterable2 if condition2
            ...
            for item3 in iterable3 if condition3]
"""

numbers = [1, 1, 2, 2, 3, 3]
squars = []

# Делали ранее:
#for i in numbers:
#    squars.append(i * i)

# Теперь:
squars = [i * i for i in numbers]
odd = [i for i in numbers if i % 2] # нечетные
points = [(x, y) for x in range(3) for y in range(3)]

print(squars)
print(odd)
print(points)

# todo: Генераторы словарей
keys = ['id', 'original_url', 'short_url']
values = ['1', 'http://hhsdufhuds', '/1']

data = {k: v for k in keys for v in values}  # потрет значения, все ключи будут со значением /1
print(data)

data = {k: v for i, k in enumerate(keys)           # ТАК НЕ ДЕЛАТЬ!!! работает
             for j, v in enumerate(values) if i == j}
print(data)

for k, v in zip(keys, values):  # zip принимает два аргумента
    print(k, v)

print(dict(zip(keys, values)))

print(data.items())

print(dict([('k1', 1), ('k2', 2), ('k3', 3)]))


# todo: Генераторы выражений

#squars = ()  # круглые скобки
squars = (i * i for i in numbers)
print(squars, type(squars), tuple(squars))


with open(__file__) as f: # текущий файл
    lines = (line.strip() for line in f)
    todos = (s for s in lines if s.startswith('# todo:'))
    todos2 = (s.replace('# todo: ', '') for s in lines if s.startswith('# todo:'))
    print('Todos:', todos, list(todos))
    print('Todos2:', todos2, list(todos2))




