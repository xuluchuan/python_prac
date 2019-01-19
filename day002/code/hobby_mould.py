# 制作趣味模板程序需求：等待用户输入名字，地点，爱好，根据用户的名字和爱好进行任意显示：
# 敬爱可亲的xxx，最喜欢在xxx地方干xxx

name = input('请输入您的姓名：')
hobby = input('请输入您最喜欢做的事情：')
place = input('请输入您做最喜欢的事情所在的位置：')
print('敬爱可亲的%s，最喜欢在%s地方干%s' % (name, place, hobby))
