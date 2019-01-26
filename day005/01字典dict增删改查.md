# 字典dict增删改查

## 数据类型划分

- 不可变数据类型(可哈希) tuple bool int str
- 可变数据类型(不可哈希) list dict set

## 字典的key与value

- 字典的key必须是不可变数据类型，可哈希，tuple，bool，int，str
- 字典的value，任意数据类型
- 字典优点：1. 二分查找查询 2. 存储关系
- 字典特点：1. 字典无序 2. 键唯一

```
dic = {
    'name': ['jason', 'tiko'],
    'py': [{'num': 71, 'age': 18}]
}
```

## 增

- dic['high'] = 185 键值对对应，没有键值对时才增加，存在键则覆盖
- dic.setdefault('weight') 只有一个参数，没有键则增加None
- dic.setdefault('weight', 15) 有两个参数，没有键值对则新增,存在键则不改变

## 删

- dic.pop('age') 删除键 返回值为value 不存在键则报错 pop('age', None) 没有键是返回而不报错
- dic.popitem() 3.5随机删除一项 3.6删除最后一项 返回值为键值对的元组
- dic.clear() 清空字典
- del dic['name'] 删除键
- del dic 删除整个字典

## 改

- dic['high'] = 185 
- dic2.update(dic1) dic2更新 存在的覆盖，不存在的新增

## 查

- dic.keys() 键对象 dict_keys 列表
- dic.values() 值对象 dict_values 列表
- dic.items() 键值对对象 dict_items 列表，元素是元组键值对
- 默认循环是键，for k in dic 等于 for k in dic.keys()
- 遍历值 for v in dic.values()
- 分别赋值 a, b = 1, 2 a, b = [1, 2] 
- 交换a b  a, b = b, a
- for k, v in dic.items(): print(k, v)
- 通过键查有可能报错
- get可以在没有时默认 不报错 dic.get('names') 找不到默认是None
- dic.get('names', None) 可以设置找不到设置为None

```python
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
```

```
C:\Users\xuluchuan\AppData\Local\Programs\Python\Python36\python.exe D:/develop/my/python/day005/dict_prac1.py
{'name': ['jason', 'tiko'], 'py': [{'num': 71, 'age': 18}]}
{'name': ['jason', 'tiko'], 'py': [{'num': 71, 'age': 18}], 'high': 185}
{'name': ['jason', 'tiko'], 'py': [{'num': 71, 'age': 18}], 'high': 185, 'weight': None}
{'name': ['jason', 'tiko'], 'py': [{'num': 71, 'age': 18}], 'high': 185, 'weight': None}
185
{'name': ['jason', 'tiko'], 'py': [{'num': 71, 'age': 18}], 'weight': None}
('weight', None)
{'name': ['jason', 'tiko'], 'py': [{'num': 71, 'age': 18}]}
{'name': 'jason', 'py': [{'num': 71, 'age': 18}]}
{'name': 'lion', 'py': [{'num': 71, 'age': 18}], 'age': 13}
dict_keys(['name', 'py', 'age'])
dict_values(['lion', [{'num': 71, 'age': 18}], 13])
dict_items([('name', 'lion'), ('py', [{'num': 71, 'age': 18}]), ('age', 13)])
name
py
age
lion
[{'num': 71, 'age': 18}]
13
name : lion
py : [{'num': 71, 'age': 18}]
age : 13
None
13
100
```
