li = []
with open('aa.txt', encoding='utf-8') as f:
    for line in f:
        dic_line = {}
        line = line.replace('\n', '')
        list_line = line.split(' ')
        dic_line['goods_name'] = list_line[0]
        dic_line['price'] = float(list_line[1])
        dic_line['number'] = float(list_line[2])
        li.append(dic_line)
goods_sum = 0
for goods in li:
    goods_sum += goods['price'] * goods['number']
print('这次购物的总价值为%.2f元' % goods_sum)
