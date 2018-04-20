s=raw_input()
l = list('!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~')
a=list(s)
count=0
for i in a:
	if i in l:
		count=count+1
print count
	
