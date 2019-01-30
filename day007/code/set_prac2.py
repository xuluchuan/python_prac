pythons = {'alex', 'egon', 'yuanhao', 'wupeiqi', 'gangdan', 'biubiu'}
linuxs = {'wupeiqi', 'oldboy', 'gangdan'}

# 1. 求出即报名python又报名linux课程的学员名字集合

print(pythons.intersection(linuxs))

# 2. 求出所有报名的学生名字集合
print(pythons.union(linuxs))

# 3. 求出只报名python课程的学员名字
print(pythons.difference(linuxs))

# 4. 求出没有同时这两门课程的学员名字集合
print(pythons.symmetric_difference(linuxs))
