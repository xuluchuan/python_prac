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
