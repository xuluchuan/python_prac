def print_list(li):
    if not isinstance(li, list):
        print(li)
    else:
        for i in li:
            print_list(i)


lis = [2, 3, 'k', ['qwe', 20, ['k1', ['tt', 3, '1'], 89], 'ab', 'adv']]
print_list(lis)
