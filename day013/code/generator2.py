def generator():
    print(1)
    yield 'a'
    print(2)
    yield 'b'


ret = generator()
print(ret)
for i in ret:
    print(i)
