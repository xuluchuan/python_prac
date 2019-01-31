# 有如下值li = [11, 22, 33, 44, 55, 77, 88, 99, 90]，
# 将所有大于66的值保存至字典的第一个key中，
# 将小于66的值保存至第二个key的值中。

li = [11, 22, 33, 44, 55, 77, 88, 99, 90]
result = {}
for row in li:
    if row > 66:
        if 'gt66' not in result:
            result['gt66'] = []
        result['gt66'].append(row)
    elif row < 66:
        if 'lt66' not in result:
            result['lt66'] = []
        result['lt66'].append(row)
print(result)
