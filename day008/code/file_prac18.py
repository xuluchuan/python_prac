import os

with open('aaa.txt', encoding='utf-8') as f1, open('aaa.txt.bak', mode='w', encoding='utf-8') as f2:
    for line in f1:
        line = line.replace('hello', 'Hello')
        f2.write(line)
os.remove('aaa.txt')
os.rename('aaa.txt.bak', 'aaa.txt')
