l1 = [1, 2, 3, ['aa', 'bb']]
l2 = l1
l2[0] = 'aaa'
l2[3][0] = 'bbb'
print(l1)  # ['aaa', 2, 3, ['bbb', 'bb']]
print(l2)
print(id(l1) == id(l2))  # True
print(l1 is l2)
