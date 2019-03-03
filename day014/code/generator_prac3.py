dict1 = {11: '22', 33: '44'}
dict2 = {dict1[k]: k for k in dict1}
print(dict2)
