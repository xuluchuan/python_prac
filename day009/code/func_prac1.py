s = '123456'


def my_len():  # 定义函数
    i = 0
    for k in s:
        i += 1
    print(i)


my_len()  # 调用函数 函数定义时不执行，调用时才执行
length = my_len()  # 函数的意义就是可以重复执行
print(length)  # 函数默认没有返回值，返回None


def my_len2():
    i = 0
    for k in s:
        i += 1
    return i  # return可以返回


length2 = my_len2()  # length2接收返回值
print(length2)
