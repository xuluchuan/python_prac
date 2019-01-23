li = [1, 2, 3]
print(li[1:3])
li.append(4)
print(li)
li.insert(3, 3)
print(li)
li2 = [5, 6]
li.extend(li2)
print(li)
print(li.pop())
print(li)
print(li.pop(4))
print(li)
li.remove(3)
print(li)
li2.clear()
print(li2)
del li2
# print(li2) # NameError: name 'li2' is not defined
del li[0:2]
print(li)
li[0] = 1
li.extend([3, 4, 5])
print(li)
li[0:2] = [1, 2, 3, 4]
print(li)
for i in li:
    print(i)
print(li[2:4])
print(len(li))
print(li.count(3))
li.sort()
print(li)
li.sort(reverse=True)
print(li)
li.reverse()
print(li)
