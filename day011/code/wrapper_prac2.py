def wrapper(func):
    def inner(*args, **kwargs):
        # 函数执行之前运行的代码
        ret = func(*args, **kwargs)
        # 函数执行之后运行的代码
        return ret

    return inner


@wrapper
def f():
    pass
