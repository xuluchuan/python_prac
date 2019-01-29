s = 'Hello 世界'
b = s.encode('utf-8')
print(b)
s1 = b.decode('utf-8')
print(s1)
s2 = b.decode('gbk')
print(s2)
