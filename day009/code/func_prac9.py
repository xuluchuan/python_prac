# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def check_len(li):
    if isinstance(li, list):
        if len(li) > 2:
            li_new = li[0:2]
            return li_new
        else:
            return li


print(check_len([1]))
print(check_len([1, 2]))
print(check_len([1, 2, 3]))
