def is_digit(s):
    for c in s:
        if not 48 <= ord(c) <= 57:
            return False
    else:
        return True


li = [
    {'name': '手机', 'price': 3250},
    {'name': '电脑', 'price': 5500},
    {'name': '鼠标垫', 'price': 35.5},
    {'name': '游艇', 'price': 10000},
]
shopping_cart = {}
while True:
    money = input('请输入您要充值的钱：')
    if money and is_digit(money):
        money = int(money)
        print('您的余额有%d元' % money)
        break
    else:
        print('输入错误，请重新输入')
while True:
    print('-' * 50)
    print('商品列表如下：')
    for index, value in enumerate(li):
        print(index + 1, '\t', value['name'], '\t', value['price'])
    order_num = input('请输入您要购买的商品序号(1-%d)，输入c清空购物车，输入l查看购物车，输入m查看余额，输入b结账，输入q退出程序：' % len(li))
    if order_num and is_digit(order_num) and 1 <= int(order_num) <= len(li):
        order_name = li[int(order_num) - 1]['name']
        print('您购买的是：%s' % order_name)
        order_count = input('请输入您要购买的%s数量：' % order_name)
        if order_count and is_digit(order_count):
            order_count = int(order_count)
            order_sum = order_count * li[int(order_num) - 1]['price']
            print('您要购买%d个%s, 总价格为%.2f元' % (order_count, order_name, order_sum))
            if not shopping_cart.get(order_name):
                shopping_cart[order_name] = [order_count, order_sum]
            else:
                shopping_cart[order_name][0] += order_count
                shopping_cart[order_name][1] += order_sum
        else:
            print('您输入有误，请重新输入')
    elif order_num == 'q':
        break
    elif order_num == 'c':
        shopping_cart = {}
    elif order_num == 'l':
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
    elif order_num == 'm':
        print('您当前的余额为：%.2f' % money)
    elif order_num == 'b':
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
                shopping_cart = {}
            print('您的当前余额为%.2f' % money)
        else:
            print('购物车为空，无法结账')
    else:
        print('您输入有误，请重新输入')
