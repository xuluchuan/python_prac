import os


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
    :return: 登录是否成功
    """
    if os.path.exists('auth'):
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
            for dict_auth in list_auth:
                if (username == dict_auth['username']) and (password == dict_auth['password']):
                    print('登录成功！')
                    return True
            count -= 1
            if count != 0:
                print('登录失败！请重新登录!您还有%d次输入密码的机会' % count)
        else:
            print('登录失败！您已经连续输错3次，用户名已经锁住，请联系管理员！')
            return False
    else:
        print('您是我们网站的第一个用户，请先注册')


def is_digit(s):
    """
    判断一个字符串是否全为数字组成
    :param s: 字符串
    :return: 是否全为数字组成
    """
    for c in s:
        if not 48 <= ord(c) <= 57:
            return False
    else:
        return True


def recharge(money):
    """
    充值
    :param money: 充值前的钱
    :return: 充值后的钱
    """
    while True:
        add_money = input('请输入您要充值的钱：')
        if add_money and is_digit(add_money):
            money += int(add_money)
            print('您的余额有%d元' % money)
            return money
        else:
            print('输入错误，请重新输入')


def print_shopping_list():
    """
    打印商品列表
    :return: None
    """
    print('-' * 50)
    print('商品列表如下：')
    for index, value in enumerate(shopping_list):
        print(index + 1, '\t', value['name'], '\t', value['price'])


def input_shopping_count(order_name, order_num):
    """
    输入商品数量
    :param order_name: 要输入的商品名称
    :param order_num: 要输入的商品序号
    :return: None
    """
    order_count = input('请输入您要购买的%s数量：' % order_name)
    if order_count and is_digit(order_count):
        order_count = int(order_count)
        order_sum = order_count * shopping_list[int(order_num) - 1]['price']
        print('您要购买%d个%s, 总价格为%.2f元' % (order_count, order_name, order_sum))
        if not shopping_cart.get(order_name):
            shopping_cart[order_name] = [order_count, order_sum]
        else:
            shopping_cart[order_name][0] += order_count
            shopping_cart[order_name][1] += order_sum
    else:
        print('您输入有误，请重新输入')


def clear_shopping_cart():
    """
    清空购物车
    :return: None
    """
    shopping_cart.clear()


def print_shopping_cart():
    """
    打印购物车
    :return: None
    """
    print('-' * 50)
    print('购物车列表如下：')
    if shopping_cart:
        sum_cart = 0
        for k, v in shopping_cart.items():
            print("品名, %s 数量 %d, 总价%.2f " % (k, v[0], v[1]))
            sum_cart += v[1]
        print('订单总金额为：%.2f' % sum_cart)
    else:
        print('购物车为空')


def print_shopping_money(money):
    """
    打印余额
    :param money: 余额
    :return: None
    """
    print('您当前的余额为：%.2f' % money)


def checkout_bill(money):
    """
    结账
    :param money: 余额
    :return: 余额
    """
    if shopping_cart:
        sum_cart = 0
        for k, v in shopping_cart.items():
            sum_cart += v[1]
        print('订单总金额为：%.2f' % sum_cart)
        if sum_cart > money:
            print('余额不足，购买失败')
        else:
            money -= sum_cart
            print('购买成功')
            clear_shopping_cart()
        print('您的当前余额为%.2f' % money)
        return money
    else:
        print('购物车为空，无法结账')
        return money


def shopping(money):
    """
    购物程序
    :param money: 余额
    :return: 余额
    """
    while True:
        print_shopping_list()
        order_num = input('请输入您要购买的商品序号(1-%d)，输入c清空购物车，输入p查看购物车，输入r充值，输入m查看余额，输入b结账，输入q返回：' % len(shopping_list))
        if order_num and is_digit(order_num) and 1 <= int(order_num) <= len(shopping_list):
            order_name = shopping_list[int(order_num) - 1]['name']
            print('您购买的是：%s' % order_name)
            input_shopping_count(order_name, order_num)
        elif order_num == 'q':
            break
        elif order_num == 'c':
            clear_shopping_cart()
        elif order_num == 'p':
            print_shopping_cart()
        elif order_num == 'r':
            money = recharge(money)
        elif order_num == 'm':
            print_shopping_money(money)
        elif order_num == 'b':
            money = checkout_bill(money)
        else:
            print('您输入有误，请重新输入')
    return money


def shopping_web(money):
    while True:
        print("1.注册")
        print("2.登录")
        print("q.退出")
        choice = input("请选择：")
        if choice == '1':
            register()
        elif choice == '2':
            auth = login()
            if auth:
                while True:
                    print("1.充值")
                    print("2.购物")
                    print("3.查看余额")
                    print("q.返回")
                    choice = input("请选择：")
                    if choice == '1':
                        money = recharge(money)
                    elif choice == '2':
                        money = shopping(money)
                    elif choice == '3':
                        print_shopping_money(money)
                    elif choice == 'q':
                        break
        elif choice == 'q':
            break
        else:
            print('输入错误，请重新输入')
    return money


shopping_list = [
    {'name': '手机', 'price': 3250},
    {'name': '电脑', 'price': 5500},
    {'name': '鼠标垫', 'price': 35.5},
    {'name': '游艇', 'price': 10000},
]
shopping_cart = {}
shopping_money = 0
shopping_money = shopping_web(shopping_money)
print_shopping_money(shopping_money)
print_shopping_cart()
