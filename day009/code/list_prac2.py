# 查找列表li中的元素，移除每个元素的空格，
# 并找出以’A’或者’a’开头，并以’c’结尾的所有元素，
# 并添加到一个新列表中,最后循环打印这个新列表。
li = ['taibai ', 'alexC', 'AbC ', 'egon', ' Ritian', ' Wusir', ' aqc']
li_new = []
for s in li:
    s = s.strip()
    if (s.startswith('A') or s.startswith('a')) and s.endswith('c'):
        li_new.append(s)
for s in li_new:
    print(s)
