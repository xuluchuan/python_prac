l = ['a', 'b', 1, 'a', 'a']
l1 = list(set(l))
print(l1)
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
