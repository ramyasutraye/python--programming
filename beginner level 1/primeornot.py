n=raw_input()
n=int(n)
a=0
if n>1:
	for i in range(2,n):
		if(n%i)==0:
			a=1
			break
		else:
			a=2
if a==1:
	print "no"
else:
	print "yes"
