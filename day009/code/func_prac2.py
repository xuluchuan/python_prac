def func1():
    li = ['你', '好']
    for i in li:
        if i == '你':
            print('找到你')
            return
        print(i)
    print('后面的代码不会运行')


func1()
