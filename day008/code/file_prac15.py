with open('a.txt', mode='r', encoding='utf-8') as f1, open('log', mode='w', encoding='utf-8') as f2:
    f2.write(f1.read())
