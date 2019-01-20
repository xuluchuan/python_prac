# int-bool-str转化

## int方法

- i.bit_length() 转换为二进制最小的位数

## bool方法

- True或False

## int-bool-str转换

- int转为str str(INT) 
- str转为int 要求str为数字型，int(STR) 转换错误ValueError
- int转为bool bool(INT) 非0为True，0为False
- bool转为int int(BOOL) True为1，False为0
- while 1比while True的效率高

```python
while 1:
    pass
```

- str转为bool bool(STR) 非空字符串为True，空字符串''为False

```python
if not s:
    print('输入为空')
else:
    pass
```

```python
i = 3
print(i.bit_length())
print(str(i))
s = '4'
print(int(s))
print(bool(i))
print(bool(0))
print(int(True))
print(int(False))
count = 0
while 1:
    count += 1
    print('hello world')
    if count == 3:
        break
name = input('请输入用户名：')
if not name:
    print('输入为空')
else:
    print('您的用户名是%s' % name)
```

```
C:\Users\xuluchuan\AppData\Local\Programs\Python\Python36\python.exe D:/develop/my/python/day003/int_bool_str.py
2
3
4
True
False
1
0
hello world
hello world
hello world
请输入用户名：
输入为空
```