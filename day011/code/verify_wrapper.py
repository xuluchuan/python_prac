# 编写装饰器，为多个函数加上认证的功能，用户的账号密码来自于文件
# 要求登录成功一次，后续的函数无需再输入用户名和密码

auth = False


def verify(func):
    """
    认证，密码来自文件
    :return: 是否认证成功
    """

    def inner(*args, **kwargs):
        global auth
        if auth:
            ret = func(*args, **kwargs)
            return ret
        with open('auth', encoding='utf-8') as f:
            li_verify = []
            for line in f:
                li = line.split(':', 1)
                username = li[0].strip()
                password = li[1].strip()
                li_verify.append({'username': username, 'password': password})
            username = input('请输入用户名：')
            password = input('请输入密码：')
            for i in li_verify:
                if i['username'] == username and i['password'] == password:
                    print('认证成功')
                    auth = True
                    ret = func(*args, **kwargs)
                    return ret
            else:
                print('认证失败')

    return inner


@verify
def f1():
    print('f1')


@verify
def f2():
    print('f2')


@verify
def f3():
    print('f3')


f1()
f2()
f3()
