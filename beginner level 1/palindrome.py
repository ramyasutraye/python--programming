num=raw_input()
if num.isdigit():
	num=int(num)
	v = num
	sum=0
	while(num!=0):
		a=num%10
		sum=sum*10+a
		num=num/10
	if(sum==v):
		print("yes")
	else:
		print("no")
else:
	print("Invalid")
