def func():
    print('func')


print(func)
func2 = func
print(func2)
func2()
func_list = [func, func2]
print('-' * 20)
for i in func_list:
    i()
print('-' * 20)


def func3(your_func):
    your_func()
    return your_func


func4 = func3(func2)
func4()
