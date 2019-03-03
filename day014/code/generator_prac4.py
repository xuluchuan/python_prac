dict1 = {'a': 32, 'A': 33, 'b': 34, 'C': 35}
dict2 = {k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1}
print(dict2)
