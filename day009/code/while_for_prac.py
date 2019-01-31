# 分别使用while循环，和for循环打印1-2+3-4+5.......+99的结果
i = 1
sign = 1
sum_result = 0
while i < 100:
    sum_result += i * sign
    sign = -sign
    i += 1
print(sum_result)
sum_result = 0
sign = 1
for i in range(1, 100):
    sum_result += i * sign
    sign = -sign
print(sum_result)
