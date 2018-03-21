num=raw_input()
if num.isdigit():
	num=int(num)
	power=len(str(num))
	sum=0
	b=num
	while b>0:
		digit=b%10
		sum=sum+digit**power
		b=b/10
	if(sum==num):
		print("yes")
	else:
 		print("no")
else:
	print "invalid"
 	
	
