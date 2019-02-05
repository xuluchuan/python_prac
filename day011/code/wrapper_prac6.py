def record(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        with open('record', mode='a', encoding='utf-8') as f:
            f.write(func.__name__ + '\n')
        return ret

    return inner


@record
def f1():
    print('f1')


@record
def f2():
    print('f2')


@record
def f3():
    print('f3')


f1()
f2()
f3()
f1()
f2()
f3()
