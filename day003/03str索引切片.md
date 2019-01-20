# str索引切片

## 索引

- s = 'hello world'
- 索引从0开始
- s[0] 就是第一个字符，是一个新字符串
- s[-1] 是最后一个字符

## 切片

- s[起始位置:结束位置] 顾头不顾尾
- s[0:-1] 取所有字符除去最后一位
- s[0:] 和 s[:] 取出所有字符
- 不写起始，默认从头取，不写结束，默认取到结束
- s[0:0] 取不到，空字符串
- s[0:5:2] 第三位为步长 默认为1
- 倒着取：s[4:0:-1] 步长为-1 s[3::-1] 倒着取前四位 
- s[::-1] 倒序 s[-1::-1]

```python
s = 'hello world'
print(s[0])
print(s[-1])
print(s[2:4])
print(s[0:-1])
print(s[:])
print(s[0:])
print(s[:-1])
print(s[0:0])
print(s[0:5:2])
print(s[4:0:-1])
print(s[3::-1])
print(s[-1::-1])
print(s[::])
```

```
C:\Users\xuluchuan\AppData\Local\Programs\Python\Python36\python.exe D:/develop/my/python/day003/code/str_slice.py
h
d
ll
hello worl
hello world
hello world
hello worl

hlo
olle
lleh
dlrow olleh
hello world
```
