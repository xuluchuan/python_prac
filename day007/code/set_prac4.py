l = [
    {'name': 'egon', 'age': 18, 'sex': 'male'},
    {'name': 'alex', 'age': 73, 'sex': 'male'},
    {'name': 'egon', 'age': 20, 'sex': 'female'},
    {'name': 'egon', 'age': 18, 'sex': 'male'},
    {'name': 'egon', 'age': 18, 'sex': 'male'},
]

l2 = []
for dic in l:
    if dic not in l2:
        l2.append(dic)
print(l2)
