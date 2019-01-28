li = [1, 2, 3]
for i in li:
    print(li.index(i), i)
print('-' * 20)
for index, i in enumerate(li):
    print(index, i)
print('-' * 20)
for index, i in enumerate(li, 1):
    print(index, i)
