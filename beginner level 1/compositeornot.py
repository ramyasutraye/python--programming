num=raw_input()
num=int(num)
a=0
if num>1:
	for i in range(2,num):
		if(num%i)==0:
			a=1
			break
		else:
			a=2
if a==1:
	print "yes"
else:
	print "no"
