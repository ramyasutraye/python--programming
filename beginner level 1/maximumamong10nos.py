num=raw_input().split()
l=len(num)
largest=int(num[0])
for i in range(1,l):
	if(largest<int(num[i])):
		largest=int(num[i])
print largest
