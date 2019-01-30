# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def odd_return(obj):
    """
    检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者
    :param obj: 列表或元组对象
    :return: 奇数位列表
    """
    li_odd_return = []
    if isinstance(obj, list) or isinstance(obj, tuple):
        for i in range(0, len(obj), 2):
            li_odd_return.append(obj[i])
        return li_odd_return


print(odd_return([3, 4, 5]))
print(odd_return((3, 4, 5, 6)))
