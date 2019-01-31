list3 = [

    {"name": "alex", "hobby": "抽烟"},

    {"name": "alex", "hobby": "喝酒"},

    {"name": "alex", "hobby": "烫头"},

    {"name": "alex", "hobby": "Massage"},

    {"name": "wusir", "hobby": "喊麦"},

    {"name": "wusir", "hobby": "街舞"},

]
list4 = []
name_list = []
for i in list3:
    if i['name'] not in name_list:
        name_list.append(i['name'])
for i in name_list:
    list4.append({'name': i, 'hobby_list': []})
for i in list4:
    for j in list3:
        if i['name'] == j['name']:
            i['hobby_list'].append(j['hobby'])
print(list4)
