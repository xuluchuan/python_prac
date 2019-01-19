# 计算1 - 2 + 3 - ... + 99 中除了 88所有数的和

count = 0
sum_result = 0
while count < 99:
    count += 1
    if count == 88:
        continue
    if count % 2 == 0:
        sum_result -= count
    else:
        sum_result += count
print(sum_result)
