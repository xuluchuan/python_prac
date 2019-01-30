# 写函数，接收两个数字参数，返回比较大的那个数字。
def big_number(i1, i2):
    """
    接收两个数字参数，返回比较大的那个数字。
    :param i1: 第一个数字
    :param i2: 第二个数字
    :return: 返回比较大的数字
    """
    if isinstance(i1, int) and isinstance(i2, int):
        if i1 > i2:
            return i1
        else:
            return i2


print(big_number(3, 5))
