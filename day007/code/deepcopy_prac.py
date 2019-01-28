import copy

l1 = [1, 2, 3, [11, 22, 33]]
l2 = copy.deepcopy(l1)
print(l1, '>>>', l2)
l2[3][0] = 1111
print(l1, ">>>", l2)
