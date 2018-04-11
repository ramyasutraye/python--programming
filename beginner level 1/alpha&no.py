s=raw_input()
a=0
b=0
for i in s:
	if i.isdigit():
		a=1
	if i.isalpha():
		b=1
if(a==1 and b==1):
	print "Yes"
else:
	print "No"
