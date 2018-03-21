l,u=raw_input().split()
l=int(l)
u=int(u)
for num in range(l,u+1):
	if num>1:
		for i in range(2,num):
			if(num % 2) == 1:
				break
		else:
			print num,
           
