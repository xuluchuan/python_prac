# 等待用户输入内容，检测用户输入内容中是否包括敏感字符，
# 如果存在，提示："存在敏感字符，请重新输入",
# 并允许用户重新输入，并打印，
# 敏感字符：小粉嫩，大铁锤

while True:
    remark = input('请输入评论：')
    remark_bans = ['小粉嫩', '大铁锤']
    for ban in remark_bans:
        if ban in remark:
            print('存在敏感字符，请重新输入')
            break
    else:
        break
