## 列表嵌套

- `li=[1,2,[1,2]]` 列表嵌套
- `print(li[2][0])` 连续取值

## 元组

- 只读列表 只能查询，不能修改，可以切片
- `tu = (1, 2)`
- 一个元素 `tu = (1,)`
- 儿子不能改，孙子可以改

## join

- 列表转换为字符串使用join方法
- join方法 字符串.join(可迭代对象) 将可迭代对象用字符串连接起来

## range

- 列表，数字范围 range(start,end,step) 0开始不用写start 
- 顾头不顾尾
- range(1, 10, -1) 无输结果

## 循环打印嵌套列表

```python
from collections import Iterable

li = [0, 1, 2, [3, 4, 5]]
for i in li:
    if isinstance(i, Iterable):
        for j in i:
            print(j)
    else:
        print(i)
```

```
C:\Users\xuluchuan\AppData\Local\Programs\Python\Python36\python.exe D:/develop/my/python/day004/code/for_list.py
0
1
2
3
4
5
```