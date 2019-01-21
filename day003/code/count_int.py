content = input('请输入字符串：')
count = 0
number_list = []
for i in range(48, 58):
    number_list.append(chr(i))
for i in content:
    if i in number_list:
        count += 1
print(count)
