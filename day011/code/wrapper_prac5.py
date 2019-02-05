def verify(func):
    def inner(*args, **kwargs):
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if username == 'xuluchuan' and password == '123456':
            ret = func(*args, **kwargs)
            return ret

    return inner


@verify
def f():
    print('函数执行')


f()
