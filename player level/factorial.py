s=raw_input()
s=int(s)
factorial=1
if s==0 and s==1:
	print "1"
for i in range(1,s+1):
	factorial=factorial*i
print factorial
