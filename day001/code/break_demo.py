i = 0
flag = False
while i < 100:
    j = 0
    while j < i:
        print('*', end='')
        if j == 8:
            flag = True
            break
        j += 1
    if flag:
        break
    print()
    i += 1
