import os

with open('a.txt', mode='r', encoding='utf-8') as f1, open('a.txt.bak', mode='w', encoding='utf-8') as f2:
    for line in f1:
        if '你好' in line:
            line = line.replace('你好', 'nihao')
        f2.write(line)
os.remove('a.txt')
os.rename('a.txt.bak', 'a.txt')
