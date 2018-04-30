n=raw_input()
n=int(n)
b=1
a=1
c=0
print b,
print a,
for i in range(1,n-1):
	c=b+a
	print c,
	b=a
	a=c
