import time


def timer(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        elapse_time = end_time - start_time
        print('运行函数用了%.2f秒' % elapse_time)

    return inner


def func():
    time.sleep(0.1)
    print('这是函数的主体')


func = timer(func)
func()
