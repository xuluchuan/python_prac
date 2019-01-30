# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 字典中的value只能是字符串或列表


def check_len(dic):
    """
    检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
    :param dic: 传入的字典
    :return: 保留2个长度的新字典
    """
    if isinstance(dic, dict):
        for k, v in dic.items():
            if isinstance(v, (str, list)) and len(v) > 2:
                dic[k] = v[0:2]
        return dic


print(check_len({'k1': 'v1'}))
print(check_len({'k1': 'v1', 'k2': 'v23'}))
print(check_len({'k1': 'v1', 'k2': 'v2', 'k3': [1, 2, 3, 4]}))
