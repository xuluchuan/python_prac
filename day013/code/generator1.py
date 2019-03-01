def generator():
    print(1)
    yield 'a'


ret = generator()
print(ret)
