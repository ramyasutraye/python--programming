n=raw_input()
n=int(n)
a=(n&(n-1))
if a==0:
	print "yes"
else:
	print "no"
