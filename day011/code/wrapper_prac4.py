import time


def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        elapse_time = end_time - start_time
        print('函数执行了%.2f秒' % elapse_time)
        return ret

    return inner


@timer
def f():
    time.sleep(0.1)
    print('函数执行')


f()
