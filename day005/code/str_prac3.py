# 测试一个输入的字符串中，大写字母，小写字母，数字，其他符号的个数
list_upper = []
for i in range(65, 91):
    list_upper.append(chr(i))
list_lower = []
for i in range(97, 123):
    list_lower.append(chr(i))
list_digit = []
for i in range(48, 58):
    list_digit.append(chr(i))
count_upper = 0
count_lower = 0
count_digit = 0
count_other = 0
str_input = input('请输入一个字符串：')
if str_input:
    for i in str_input:
        if i in list_upper:
            count_upper += 1
        elif i in list_lower:
            count_lower += 1
        elif i in list_digit:
            count_digit += 1
        else:
            count_other += 1
else:
    print('字符串为空，请重新输入')
print('该字符串中大写字母有%d个，小写字母有%d个，数字有%d个，其他字符有%d个'
      % (count_upper, count_lower, count_digit, count_other))
