def generator():
    print('hello1')
    content = yield 1
    print(content)
    yield 2


g = generator()
ret1 = g.__next__()
print(ret1)
ret2 = g.send('hello2')
print(ret2)
