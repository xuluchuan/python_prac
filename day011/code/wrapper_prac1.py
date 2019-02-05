import time


def timer(f):
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = f(*args, **kwargs)
        end_time = time.time()
        elapse_time = end_time - start_time
        print('运行函数用了%.2f秒' % elapse_time)
        return ret

    return inner


@timer
def func(a):
    time.sleep(0.1)
    print('这是函数的主体')
    return a


result = func(1)
print(result)
