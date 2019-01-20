# str操作

- 首字母大写：capitalize
- 全部变大写：upper
- 全部变小写：lower
    - 验证码不区分大小写

```python
code = 'acEQ'
print('验证码为%s' % code)
your_code = input('请输入验证码，不区分大小写：')
if code.upper() == your_code.upper():
    print('验证码输入成功')
else:
    print('验证码输入错误')
```

```
C:\Users\xuluchuan\AppData\Local\Programs\Python\Python36\python.exe D:/develop/my/python/day003/code/verify_code.py
验证码为acEQ
请输入验证码，不区分大小写：AACQ
验证码输入错误
```

- 大小写翻转：swapcase()
- 每个隔开(特殊字符或数字)的单词首字母大写：title()
- 居中对齐 center(width,fillchar=None) 默认是空格填充
- 居左对齐 ljust 居右对齐 rjust
- tab补全 expandTabs tab转换为空格 默认逢8进1
- 公共方法：长度 len(STR) 
- 以..为开头：startswith(子串) (子串, 开始, 结束)可写区间
- 以..为结尾：endswith(子串)
- 查找 find(子串) (子串,开始,结束) 返回第一个找到的索引，找不到返回-1 首选find
- 查找 index(子串) (子串,开始,结束) 返回第一个找到的索引，找不到报错
- rfind rindex 从右到左找
- 去空格 strip() 默认去掉左右的空格 (%@) 可以删除其他字符 rstrip 右 lstrip 左
- 统计个数 count() 找不到为0
- 拆分成列表 split() (分隔符) 
- 拆分成三段 partition(分隔符) 
- 格式化输出 format 完形填空

```python
s='my name is {}, my age is {}'.format('xu', 18) # 按照位置
s='my name is {0}, my age is {1}, my name is {0}'.format('xu', 18) # 按照索引
s='my name is {name}, my age is {age}, my name is {name}'.format(name='xu', age=18) # 按照键值对
```

- 替换，replace(原子串，新子串，次数) 默认全替换，可指定次数
- 是什么 isalnum(是否是字母数字) isalpha(是否是字母) isdecimal(是否是数字)

- for循环迭代字符串

```python
for i in s:
    print(i)
```

- 判断是否有子串 

```python
if i in s:
    print("敏感字符")
```


```python
s = 'hello World'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.center(20, '*'))
print(s.ljust(20, '*'))
print(s.rjust(20, '*'))
print('hello\tWorld'.expandtabs())
print(len(s))
print(s.startswith('he'))
print(s.endswith('l', 7, -1))
print(s.find('e'))
print(s.index('e'))
print(s.rfind('l'))
print(' hello world '.strip())
print('* hello world *'.rstrip('* '))
print('* hello world *'.lstrip('* '))
print(s.count('l'))
print(s.count('l', 3, 6))
print(s.split())
print('hello world !'.partition(' '))
f1 = 'my name is {}, my age is {}'.format('xu', 18)
print(f1)
f2 = 'my name is {0}, my age is {1}, my name is {0}'.format('xu', 18)
print(f2)
f3 = 'my name is {name}, my age is {age}, my name is {name}'.format(name='xu', age=18)
print(f3)
print(s.replace('l', 'L'))
print(s.replace('l', 'L', 1))
print(s.isalnum())
print(s.isalpha())
print(s.isdecimal())
for i in s:
    print(i, end=' ')
    print()
if 'o' in s:
    print('敏感字符')
```

```
C:\Users\xuluchuan\AppData\Local\Programs\Python\Python36\python.exe D:/develop/my/python/day003/code/str_count.py
Hello world
HELLO WORLD
hello world
HELLO wORLD
****hello World*****
hello World*********
*********hello World
hello   World
11
True
True
1
1
9
hello world
* hello world
hello world *
3
1
['hello', 'World']
('hello', ' ', 'world !')
my name is xu, my age is 18
my name is xu, my age is 18, my name is xu
my name is xu, my age is 18, my name is xu
heLLo WorLd
heLlo World
False
False
False
h 
e 
l 
l 
o 
  
W 
o 
r 
l 
d 
敏感字符
```