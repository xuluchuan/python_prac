count = 0
sum_result = 0
while count < 99:
	count += 1
	if count % 2 == 0:
		sum_result -= count
	else:
		sum_result += count
print(sum_result)