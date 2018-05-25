import random
import string


val = string.ascii_letters + string.digits + '!@#$%^&*()' #printable[:68]
#dd = random.sample(val, 16)

#passw = '%s'%''.join(map(lambda a:str(a), ))
#print(dd)
#print(dd[0])
#passw = ''.join(i for i in dd)

passw = '%s' %''.join(map(lambda a:str(a), random.sample(val, 16)))
passw = '{}'.format(''.join(map(lambda a:str(a), random.sample(val, 16))))
print(passw)


