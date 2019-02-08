def wrapper1(func):
    def inner1(*args, **kwargs):
        print('before wrapper1')
        ret = func(*args, **kwargs)
        print('after wrapper1')
        return ret

    return inner1


def wrapper2(func):
    def inner2(*args, **kwargs):
        print('before wrapper2')
        ret = func(*args, **kwargs)
        print('after wrapper2')
        return ret

    return inner2


@wrapper1
@wrapper2
def f():
    print('f')


f()
