import random
import string


def password_generator(n):
    val = string.printable[:68]
    #password = ''
    while n:
        password = str(random.choice(val))
        yield password
        n -= 1


if __name__ == '__main__':
    n = int(input())
    passw = ''
    gen = password_generator(n)
    while n:
        passw += next(gen)
        n -= 1
    print(passw)


import random
import string


def password_generator(n):
    val = string.printable[:68]
    password = ''
    while n:
        password += str(random.choice(val))
        n -= 1
    return password


if __name__ == '__main__':
    n = int(input())
    password_generator(n)