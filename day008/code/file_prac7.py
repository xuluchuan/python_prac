f = open('a.txt', mode='r+', encoding='utf-8')
content = f.read()
print(content)
f.write('你好吗？')
f.close()