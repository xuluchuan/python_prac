def sum_num(a, b, *args):
    """
    求数字的和
    :param a: 第一个数字
    :param b: 第二个数字
    :param args: 更多数字
    :return: 所有数字的和
    """
    sum_all = a + b
    if args:
        for i in args:
            sum_all += i
    return sum_all


print(sum_num(3, 4))
print(sum_num(3, 4, 5))
print(sum_num(3, 4, 5, 6))
