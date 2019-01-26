dic = {
    'name': ['jason', 'tiko'],
    'py': [{'num': 71, 'age': 18}]
}
print(dic)
dic['high'] = 185
print(dic)
dic.setdefault('weight')
print(dic)
dic.setdefault('weight', 3)
print(dic)
print(dic.pop('high'))
print(dic)
print(dic.popitem())
print(dic)
dic['name'] = 'jason'
print(dic)
dic1 = {'name': 'lion', 'age': 13}
dic.update(dic1)
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
for k in dic:
    print(k)
for v in dic.values():
    print(v)
for k, v in dic.items():
    print(k, ':', v)
print(dic.get('weight'))
print(dic.get('age'))
print(dic.get('weight', 100))
