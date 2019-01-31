# 计算用户输入内容中索引为奇数并且对应的元素为数字的个数（没有则个数为零）
s = input('请输入字符串：')
count = 0
if s:
    s_odd = s[::2]
    for char in s_odd:
        if 48 <= ord(char) <= 57:
            count += 1
print(count)
