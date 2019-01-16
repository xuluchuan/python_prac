count = 0
sum100_odd = 0
while count < 100:
	count += 1
	if count % 2 == 0:
		continue
	sum100_odd += count
print(sum100_odd)