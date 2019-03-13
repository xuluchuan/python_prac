import time


# 写一个装饰器，可以打印输出方法执行时长的信息(8分)
def timer(func):
    def inner(*args, **kwargs):
        begin_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        elapse_time = end_time - begin_time
        print('总共消耗了%f秒' % elapse_time)
        return ret

    return inner


@timer
def print_line():
    for i in range(1, 100000):
        print(i)


print_line()
