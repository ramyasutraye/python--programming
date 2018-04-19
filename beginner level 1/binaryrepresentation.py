s=raw_input()
a=len(s)
k=0
l=['1','0']
for i in range(a):
	if s[i] in l:
		continue
	else:
		k=1
		break
if k!=1:
	print "yes"
else:
	print "no"
