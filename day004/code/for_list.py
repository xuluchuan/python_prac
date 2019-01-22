from collections import Iterable

li = [0, 1, 2, [3, 4, 5]]
for i in li:
    if isinstance(i, Iterable):
        for j in i:
            print(j)
    else:
        print(i)
