import random
import string

def generator(n):
    val = string.ascii_letters + string.digits + '!@#$%^&*()'  # printable[:68]
    while n:
        m = random.choice(val)
        yield m
        n -= 1


def password_generator(n):
    passw = ''
    while n:
        gen = generator(n)
        passw += next(gen)
        n -= 1
    return passw


if __name__ == '__main__':
    n = int(input())
    print(password_generator(n))


"""
===================================
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