set1 = {1, 2, 3, 3}
print(set1)
set1.add(4)
print(set1)
set1.update([4, 5, 6])
print(set1)
print(set1.pop())
print(set1)
set1.remove(2)
print(set1)
for i in set1:
    print(i)
set2 = {1, 2, 3}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
set3 = {1}
print(set3.issubset(set2))
print(set2.issuperset(set3))
li = [3, 3, 4, 4, 5, 5]
print(list(set(li)))
s = frozenset({3, 4, 5})
print(s)
