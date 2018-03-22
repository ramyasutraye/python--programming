s=raw_input()
s=int(s)
if s>1:
	for i in range(2,s):
		if(s%i==0):
			print "yes"
			break
		else:
			print "no"
