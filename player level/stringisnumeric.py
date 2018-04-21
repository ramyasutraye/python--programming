n=raw_input()
s=0
for i in n:
	if i.isdigit():
		s=1
	else:
		s=2
if s==1:
	print "yes"
else:
	print "no"
