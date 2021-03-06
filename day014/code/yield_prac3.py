def init(ge):
    def inner(*args, **kwargs):
        ret = ge(*args, **kwargs)
        ret.__next__()
        return ret

    return inner


@init
def ma():
    count = 0
    sum_all = 0
    avg = 0
    while True:
        num = yield avg
        sum_all += num
        count += 1
        avg = sum_all / count


ma_ge = ma()
ma_result = ma_ge.send(20)
print(ma_result)
ma_result = ma_ge.send(30)
print(ma_result)
ma_result = ma_ge.send(40)
print(ma_result)
