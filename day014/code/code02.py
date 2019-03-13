# li = [1, 1, 2, 3, 4, 4]
# new_li = []
# for i in li:
#     if i not in new_li:
#         new_li.append(i)
# print(new_li)
li = [1, 1, 2, 3, 4, 4]
new_li = list(set(li))
print(new_li)
