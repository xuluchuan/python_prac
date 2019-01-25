li = ['alex', 'wusir', 'eric', 'rain', 'alex']
print(len(li))
li.append('seven')
print(li)
li.insert(0, 'Tony')
print(li)
li[1] = 'kelly'
print(li)
l2 = [1, 'a', 3, 4, 'heart']
li.extend(l2)
print(li)
s = 'qwert'
li[0:0] = s
print(li)
li.remove('eric')
print(li)
removed_unit = li.pop(1)
print(removed_unit)
print(li)
del li[1:4]
print(li)
li.reverse()
print(li)
print(li.count('alex'))
