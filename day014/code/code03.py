# - 斐波那契数列1,1,2,3,5,8,13,21…根据这样的规律，编程求出400万以内最大的斐波那契数，并求出它是第几个斐波那契数
def fib(n):
    if n == 1:
        result = 1
        return result
    if n == 2:
        result = 1
        return result
    result = fib(n - 1) + fib(n - 2)
    return result


i = 0
while True:
    i += 1
    res = fib(i)
    if res > 4000000:
        print(fib(i - 1))
        print(i - 1)
        break
