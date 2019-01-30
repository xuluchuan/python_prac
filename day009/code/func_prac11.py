# 写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否是空白字符，并返回结果。
def is_have_space(obj):
    """
    检查用户传入的对象（字符串、列表、元组）的每一个元素是否是空白字符
    :param obj: 用户传入的对象（字符串、列表、元组）
    :return: 每一个元素是否是空白字符
    """
    if isinstance(obj, (str, list, tuple)):
        for i in obj:
            i = str(i)
            if i.isspace():
                return True
        else:
            return False


print(is_have_space('Hello World'))
print(is_have_space('Hello'))
print(is_have_space(['hello', ' world']))
print(is_have_space(['hello', 'world', ' ']))
print(is_have_space((1, 2, '    ', 'Hello')))
