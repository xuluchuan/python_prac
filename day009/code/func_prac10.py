# 测试一个输入的字符串中，大写字母，小写字母，数字，其他符号的个数
def count_str(s):
    """
    计算字符串中，大写字母，小写字母，数字，其他符号的个数
    :param s: 字符串
    :return: 大写字母，小写字母，数字，其他符号的个数
    """
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_other = 0
    if isinstance(s, str):
        for i in str_input:
            if 65 <= ord(i) <= 90:
                count_upper += 1
            elif 97 <= ord(i) <= 122:
                count_lower += 1
            elif 48 <= ord(i) <= 57:
                count_digit += 1
            else:
                count_other += 1
        return count_upper, count_lower, count_digit, count_other


str_input = input('请输入一个字符串：')
upper_count, lower_count, digit_count, other_count = count_str(str_input)
print('该字符串中大写字母有%d个，小写字母有%d个，数字有%d个，其他字符有%d个'
      % (upper_count, lower_count, digit_count, other_count))
