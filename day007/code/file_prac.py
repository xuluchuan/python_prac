with open('a.txt', encoding='utf-8') as f1, open('b.txt', mode='w', encoding='utf-8') as f2:
    li = []
    for line in f1:
        line = line.replace('\n', '')
        if line not in li:
            li.append(line)
    f2.write('\n'.join(li))
