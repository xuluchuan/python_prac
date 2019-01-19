count = 3
while count > 0:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if (username == 'xuluchuan') and (password == '123456'):
        print('登录成功！')
        break
    count -= 1
    if count != 0:
        print('登录失败！请重新登录!您还有' + str(count) + '次输入密码的机会')
else:
    print('您的用户名已经锁住，请联系管理员！')
