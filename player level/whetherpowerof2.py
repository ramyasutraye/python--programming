num=raw_input()
num=int(num)
a=(num&(num-1))
if a==0:
	print "yes"
else:
  print "no"
