li = [1, 2, 3, 4]
li2 = list(reversed(li))
print(li2)
si = slice(2, 3)
print(li2[si])
print(format('23', '>20'))
print(bytes('你好', encoding='utf-8'))
print(ord('a'))
print(chr(97))
print('%r' % 'hello world')
print(repr('hello world'))
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1, 1):
    print(index, item)
print(any(['1', None]))
print(all(['1', None]))
for i in zip(li, li2):
    print(i)


def lower(x):
    if x < 3:
        return x


def x2(x):
    return 2 * x


for i in filter(lower, li):
    print(i)

for i in map(x2, li):
    print(i)

li3 = sorted(li, reverse=True)
print(li3)
