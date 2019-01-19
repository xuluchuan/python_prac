# 计算1 - 2 + 3 - ... - 99 中除了 88所有数的和

count = 0
sign = 1
sum_result = 0
while count < 99:
    count += 1
    if count == 88:
        continue
    sum_result += count * sign
    sign = -sign
print(sum_result)
