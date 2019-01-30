# 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def is_gt_5(obj):
    """
    判断用户传入的对象（字符串、列表、元组）长度是否大于5
    :param obj: 用户传入的对象
    :return: 对象长度是否大于5
    """
    if isinstance(obj, str) or isinstance(obj, list) or isinstance(obj, tuple):
        return len(obj) > 5


print(is_gt_5([3, 4]))
print(is_gt_5('hello'))
print(is_gt_5((1, 2, 3, 4, 5, 6)))
print(is_gt_5(355))
