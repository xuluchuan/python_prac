# 大于66保存在字典第一个key，小于第二个
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
li_gt_66 = []
li_lt_66 = []
for i in li:
    if i > 66:
        li_gt_66.append(i)
    elif i < 66:
        li_lt_66.append(i)
dic = {'k1': li_gt_66, 'k2': li_lt_66}
print(dic)
