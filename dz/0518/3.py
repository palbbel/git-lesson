import random
import string

def password_generator():
    val = string.ascii_letters + string.digits + '!@#$%^&*()'
    yield str(random.choice(val))


def generator(n):
    pwd = ''
    while n:
        gen = password_generator()
        pwd += str(next(gen))

        n -= 1

    return pwd


if __name__ == '__main__':
    n = int(input())
    print(generator(n))
