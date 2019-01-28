# 删除字典中key含有k元素的键
dic = {'k1': 'v1', 'k2': 'v2', 'a3': 'v3'}
li = []
for i in dic:
    if 'k' in i:
        li.append(i)
for i in li:
    del dic[i]
print(dic)
