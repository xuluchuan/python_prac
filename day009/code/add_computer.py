# 实现一个整数加法计算器
# 如：content = input(‘请输入内容:’)
# 如用户输入：5+8+7....(最少输入两个数相加)，
# 然后进行分割再进行计算，将最后的计算结果添加到此字典中(替换None)：
# dic={‘最终计算结果’:None}。


def is_int(number):
    for n in number:
        if not 48 <= ord(n) <= 57:
            return False
    else:
        return True


def add_int(content):
    result = 0
    if content and '+' in content:
        li_content = content.split('+')
        for i in li_content:
            i = i.strip()
            if i and is_int(i):
                result += int(i)
            else:
                print('最少输入两个整数相加')
                return
    else:
        print('最少输入两个整数相加')
        return
    return result


input_content = input('请输入整数加法的内容：')
dic = {'最终计算结果': add_int(input_content)}
print(dic)
