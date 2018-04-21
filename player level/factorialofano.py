u=raw_input()
u=int(u)
factorial=1
if u==0 and u==1:
	print "1"
for i in range(1,u+1):
	factorial=factorial*i
print factorial
