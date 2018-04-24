n=raw_input()
n=int(n)
a=bin(n)
b=a[2:]
if b==0000:
	print "0"
else:
	l=len(b)
	print l
