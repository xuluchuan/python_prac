from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret

    return inner


@wrapper
def f():
    print('f')


print(f.__name__)
