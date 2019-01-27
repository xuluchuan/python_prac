dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33]}
for k in dic:
    print(k)
for v in dic.values():
    print(v)
for k, v in dic.items():
    print(k, ':', v)
dic['k4'] = 'v4'
print(dic)
dic['k1'] = 'alex'
print(dic)
dic['k3'].append(44)
print(dic)
dic['k3'].insert(0, 18)
print(dic)
