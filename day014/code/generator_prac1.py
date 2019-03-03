list1 = ['鸡蛋%s' % i for i in range(10)]
print(list1)
ge1 = ('鸡蛋%s' % i for i in range(10))
for i in ge1:
    print(i)
