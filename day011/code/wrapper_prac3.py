import time
import random


def wait_random(func):
    def inner(*args, **kwargs):
        rnd = random.randrange(1, 10)
        time.sleep(rnd)
        print('函数睡眠了%d秒' % rnd)
        ret = func(*args, **kwargs)
        return ret

    return inner


@wait_random
def f():
    print('函数执行')


f()
