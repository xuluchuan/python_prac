code = 'acEQ'
print('验证码为%s' % code)
your_code = input('请输入验证码，不区分大小写：')
if code.upper() == your_code.upper():
    print('验证码输入成功')
else:
    print('验证码输入错误')
