def replace_str_to_upper(li, s):
    if isinstance(li, list):
        for i in li:
            replace_str_to_upper(i, s)
        while li.count(s) != 0:
            li[li.index(s)] = s.upper()


def replace_a_to_b(li, a, b):
    if isinstance(li, list):
        for i in li:
            replace_a_to_b(i, a, b)
        while li.count(a) != 0:
            li[li.index(a)] = b


lis = [2, 3, 'k', ['qwe', 20, ['k1', ['tt', 3, '1'], 89], 'ab', 'adv']]
ss = 'tt'
# lis[-1][2][1][0] = lis[-1][2][1][0].upper()
replace_str_to_upper(lis, ss)
print(lis)
a1 = 3
b1 = '100'
# lis[1] = '100'
# lis[3][2][1][1] = '100'
replace_a_to_b(lis, a1, b1)
print(lis)
a2 = '1'
b2 = 101
# lis[3][2][1][2] = 101
replace_a_to_b(lis, a2, b2)
print(lis)
