import datetime
from datetime import time
# Exception исключения
'''
try:
    i = int(input())
    print(i[0])
except ValueError:
    print('Не корректное число')
except:
    print('Любое исключение отловлено')
finally:
    print('Выполняется всегда')



raise KeyError('Мое сообщение об ошибке')
'''
dateStart = '2014.13.01'

#startDateFormat = time.strptime(dateStart, "%Y.%m.%d")
try:
    datetime.datetime.strptime(dateStart, "%Y.%m.%d")
    print('of')
except:
    print('error')