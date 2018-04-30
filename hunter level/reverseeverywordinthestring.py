str=raw_input().split()
length=len(str)
for i in range(0,length):
	s=str[i]
	l=[]
	for i in range(1,len(s)):
		l.append(s[-i])
	l.append(s[0])
	print "".join(l),
		
