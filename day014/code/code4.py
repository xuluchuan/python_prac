# 要求写一段代码，实现两个字典的相加，不同的key对应的值保留，相同的key对应的值相加后保留，如果是字符串就拼接，如上示例得到的结果应为：
def dict_plus(dict_a, dict_b):
    set_dict_a_key = set(dict_a.keys())
    set_dict_b_key = set(dict_b.keys())
    diff_keys = set_dict_a_key.symmetric_difference(set_dict_b_key)
    same_keys = set_dict_a_key.intersection(set_dict_b_key)
    new_dict = {}
    for k in diff_keys:
        if k in set_dict_a_key:
            new_dict[k] = dict_a[k]
        else:
            new_dict[k] = dict_b[k]
    for k in same_keys:
        new_dict[k] = dict_a[k] + dict_b[k]
    return new_dict


dicta = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 'hello'}
dictb = {'b': 3, 'd': 5, 'e': 7, 'm': 9, 'k': 'world'}
add_new_dict = dict_plus(dicta, dictb)
print(add_new_dict)
