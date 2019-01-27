def is_digit(s):
    for c in s:
        if not 48 <= ord(c) <= 57:
            return False
    else:
        return True


li = ["手机", "电脑", "鼠标垫", "游艇"]
# 方法1
# print('遍历列表方法1：')
# for i in li:
#     print("序号：%s   值：%s" % (li.index(i) + 1, i))

# print('\n遍历列表方法2：')
# 方法2
# for i in range(len(li)):
#     print("序号：%s   值：%s" % (i + 1, li[i]))

# 方法3
# print('\n遍历列表方法3：')
# for i, val in enumerate(li):
#     print("序号：%s   值：%s" % (i + 1, val))

# 方法3
# print('\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：')
# for i, val in enumerate(li, 2):
#     print("序号：%s   值：%s" % (i + 1, val))

while True:
    print('-' * 50)
    print('商品列表如下：')
    for i, val in enumerate(li):
        print(i + 1, val)
    order_num = input('请输入您要购买的商品序号(1-%d)，输入Q或q退出程序：' % len(li))
    if order_num and is_digit(order_num) and 1 <= int(order_num) <= len(li):
        print('您购买的是：%s' % li[int(order_num) - 1])
    elif order_num in ['q', 'Q']:
        break
    else:
        print('您输入有误，请重新输入')
