import time
import re
from email.utils import parseaddr

date = '1.9.2017 12:00'
date = date.replace('/','-').replace('.','-').replace('  ',' ').strip()
if len(date) <= 10:
    date += ' 00:00:00'
elif 14<=len(date)<=16:
    date += ':00'
result = re.match(r'\d{4}', date)

try:
    if date.index('-') != 4:
        valid_date = time.strptime(date, '%d-%m-%Y %H:%M:%S')
    else:
        valid_date = time.strptime(date, '%Y-%m-%d %H:%M:%S')
    print('Ok')
except ValueError:
    print('Error')



d = 'inf=Jo@itTo-it.Org'

print(d.lower())

'''
год-месяц-день (2017-09-01, 2017-09-1, 2017-9-1)


год-месяц-день часы:минуты (2017-09-01 12:00)
год-месяц-день часы:минуты:секунды (2017-09-01 12:00:00)


день.месяц.год (1.9.2017, 1.09.2017, 01.09.2017)
день.месяц.год часы:минуты (1.9.2017 12:00)
день.месяц.год часы:минуты:секунды (1.9.2017 12:00:00)
день/месяц/год (1/9/2017, 1/09/2017, 01/09/2017)
день/месяц/год часы:минуты (1/9/2017 12:00)
день/месяц/год часы:минуты:секунды (1/9/2017 12:00:00)
'''

value = value.lower()
resault = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', value)
# [A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}
# [a - zA - Z0 - 9] + @ [a - zA - Z0 - 9] +\.[a - zA - Z0 - 9] +
print(parseaddr('info@itmo-it.org'))