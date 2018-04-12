s=raw_input()
a=0
for i in s:
	if s.isdigit():
		a=1
	else:
		a=2
if a==1:
	print "Yes"
else:
	print "No"
