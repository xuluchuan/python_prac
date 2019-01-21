name = 'aleX leNb'
print(name.lstrip('al'))
print(name.rstrip('Nb'))
print(name.lstrip('a').rstrip('b'))
print(name.startswith('al'))
print(name.endswith('Nb'))
print(name.replace('l', 'p'))
print(name.replace('l', 'p', 1))
print(name.split('l'))
print(name.split('l', 1))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.count('l'))
print(name.count('l', 0, 4))
print(name.index('N'))
print(name.find('N'))
print(name.find('X le'))
print(name[1])
print(name[:3])
print(name[-2:])
start = 0
index = 0
while index != -1:
    index = name.find('e', start)
    if index != -1:
        print(index)
    start = index + 1
print('badboy'[:-1])
