import random
import string


def password_generator(n):
    val = string.ascii_letters + string.digits + '!@#$%^&*()' #printable[:68]
    while 1:
        passw = '{}'.format(''.join(map(lambda a:str(a), random.sample(val, n))))
        #print(passw)
        yield passw



if __name__ == '__main__':
    #n = int(input())
    password_generator(16)

"""
============================
import random
import string


def password_generator(n):
    val = string.ascii_letters + string.digits + '!@#$%^&*()' #printable[:68]
    while n:
        passw = str(random.choice(val))
        yield  passw
        n -= 1

if __name__ == '__main__':
    n = int(input())
    ''.join(i for i in password_generator(n))

"""
#=========================