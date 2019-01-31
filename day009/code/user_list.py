# (1)
# 员工的账号密码存储在这种数据类型中：
#
# user_list = [
#
#     {'username': 'barry', 'password': '1234'},
#
#     {'username': 'alex', 'password': 'asdf'},
#     .........
#
# ]
# (2)
# 非法字符模板：board = ['张三', '李小四', '王二麻子']
# (3)
# HR输入用户名，密码（可持续输入，如果想终止程序，那就在输入用户名时输入Q或者q退出程序），
# 在Hr输入用户名时，检测此用户名是否有board里面的非法字符，
# 如果有非法字符，则将非法字符替换成同数量的 *（如王二麻子替换成 ** ** ），然后添加到user_list中，
# 如果没有非法字符，则直接添加到user_list中，每次添加成功后，打印出刚添加的用户名，密码。
user_list = [
    {'username': 'barry', 'password': '1234'},
    {'username': 'alex', 'password': 'asdf'},
]

board = ['张三', '李小四', '王二麻子']
while True:
    username = input('请输入用户名，输入Q或q退出程序：')
    if username:
        if username.upper() == 'Q':
            break
        elif username in board:
            username = '*' * len(username)
            user_list.append({'username': username})
        else:
            user_list.append({'username': username})
    else:
        print('用户名不能为空，请重新输入')
        continue
    while True:
        password = input('请输入密码：')
        if password:
            user_list[-1]['password'] = password
            print('添加成功！用户名为{}，密码为{}'.format(username, password))
            break
        else:
            print('密码不能为空，请重新输入')
print(user_list)
