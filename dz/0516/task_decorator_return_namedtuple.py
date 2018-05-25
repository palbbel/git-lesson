from collections import namedtuple
from functools import wraps



def return_namedtuple(*args):
    cort = args
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, tuple) == True:
                Point = namedtuple('Point', cort)
                r = Point(*res)
                return r
        return wrapper
    return decorator



@return_namedtuple('one', 'two')
def func():
    return 1, 2


if __name__ == '__main__':
    r = func()
    print(r.one)  # 1
    print(r.two)  # 2