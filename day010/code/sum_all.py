def sum_all(*args):
    result = 0
    for i in args:
        result += i
    return result


print(sum_all(3, 4, 5, 6))
