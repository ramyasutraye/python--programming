n,k=raw_input().split()
n=int(n)
k=int(k)
arr=[]
a=0
for i in range(n):
	a=raw_input()
	b=int(a)
	arr.append(b)
for i in range(n):
	if (k==arr[i]):
		a=1
		break
	else:
		a=2
if a==1:
	print "yes"
else:
	print "no"
