def ge():
    a = 'hello'
    b = 'world'
    yield from a
    yield from b


g = ge()
for i in g:
    print(i)
