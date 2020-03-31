#逢7跳过

for n in range(1,100):
	if n%7==0:
		continue
	elif n%10==7:
		continue
	elif n//10==7:
		continue
	else:
		print(n)
