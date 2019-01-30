# 注册界面
def register():
    """
    注册
    :return:
    """
    while True:
        print('<--注册界面-->')
        username = input('请输入用户名：')
        if username:
            password = input('请输入密码：')
            if password:
                password_verify = input('请再次输入密码确认：')
                if password == password_verify:
                    with open('auth', mode='a', encoding='utf-8') as f:
                        f.write('{}:{}\n'.format(username, password))
                    print('注册成功！')
                    break
                else:
                    print('两次密码输入不一致，请重新注册！')
            else:
                print('密码不能为空，请重新注册！')
        else:
            print('用户名不能为空，请重新注册！')


# 登录界面
def login():
    """
    登录，三次机会
    :return:
    """
    count = 3
    list_auth = []
    with open('auth', mode='r', encoding='utf-8') as f:
        for line in f:
            dict_auth = {}
            list_line = line.strip().partition(':')
            dict_auth['username'] = list_line[0]
            dict_auth['password'] = list_line[2]
            list_auth.append(dict_auth)
    while count > 0:
        print('<--登录界面-->')
        username = input('请输入用户名：')
        password = input('请输入密码：')
        flag = False
        for dict_auth in list_auth:
            if (username == dict_auth['username']) and (password == dict_auth['password']):
                print('登录成功！')
                flag = True
                break
        if flag:
            break
        count -= 1
        if count != 0:
            print('登录失败！请重新登录!您还有%d次输入密码的机会' % count)
    else:
        print('登录失败！您已经连续输错3次，用户名已经锁住，请联系管理员！')


register()
register()
login()
login()
