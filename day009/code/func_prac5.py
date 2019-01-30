def func1():
    print('func1')


func1()


def func2(s):
    print(s)


func2('func2')


def sum1(a, b):
    return a + b


print(sum1(3, 5))
print(sum1(3, b=5))


def sum2(a, b, c=0):
    return a + b + c


print(sum2(3, 4))
print(sum2(3, 4, 5))


def sum3(a, b, *args):
    sum_all = a + b
    if args:
        for i in args:
            sum_all += i
    return sum_all


print(sum3(3, 4))
print(sum3(3, 4, 5))
print(sum3(3, 4, 5, 6))


def sum4(a, b, *args, **kwargs):
    sum_all = a + b
    if args:
        for i in args:
            sum_all += i
    if kwargs:
        for i in kwargs.values():
            sum_all += i
    return sum_all


print(sum4(3, 4))
print(sum4(3, 4, 5))
print(sum4(3, 4, 5, 6))
print(sum4(3, 4, 5, 6, c=3, d=4))
li4 = [5, 6]
dic4 = {'c': 3, 'd': 4}
print(sum4(3, 4, *li4, **dic4))
