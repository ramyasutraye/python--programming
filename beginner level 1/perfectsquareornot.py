s,t=raw_input().split()
s=int(s)
t=int(t)
x=s*t
ans = 0
if x >= 0:
    while ans*ans < x:
        ans = ans + 1
    if ans*ans != x:
	print "no" 
    else:
	print "yes"
