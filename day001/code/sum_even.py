count = 0
sum100_even = 0
while count < 100:
	count += 1
	if count % 2 == 1:
		continue
	sum100_even += count
print(sum100_even)