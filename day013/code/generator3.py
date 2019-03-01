def wahaha():
    for i in range(2000000):
        yield '娃哈哈%s' % i


ret = wahaha()
for i in ret:
    print(i)
